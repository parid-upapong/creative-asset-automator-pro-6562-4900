import cv2
import numpy as np
from typing import Tuple, List

class SmartReframer:
    """
    Handles the intelligent transformation of video aspect ratios
    by tracking subjects of interest.
    """
    def __init__(self, target_ratio: float = 9/16):
        self.target_ratio = target_ratio
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        self.smoothing_window = []
        self.max_smoothing = 10

    def get_focal_point(self, frame: np.ndarray) -> Tuple[int, int]:
        """
        Identifies the X, Y coordinate of the most important subject.
        Defaults to center if no subject is found.
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        height, width = frame.shape[:2]
        center_x, center_y = width // 2, height // 2

        if len(faces) > 0:
            # Pick the largest face (closest to camera)
            largest_face = max(faces, key=lambda f: f[2] * f[3])
            x, y, w, h = largest_face
            return (x + w // 2, y + h // 2)
        
        return (center_x, center_y)

    def calculate_crop_window(self, frame: np.ndarray, focal_point: Tuple[int, int]) -> Tuple[int, int, int, int]:
        """
        Calculates the bounding box for the crop based on the target ratio.
        """
        f_x, f_y = focal_point
        h, w = frame.shape[:2]
        
        # Calculate target width based on target ratio and current height
        # For 9:16, target_width = height * (9/16)
        target_w = int(h * self.target_ratio)
        
        # Ensure target width is not wider than source
        target_w = min(target_w, w)
        
        # Center the window on focal_point.x
        start_x = f_x - (target_w // 2)
        
        # Keep window within frame boundaries
        start_x = max(0, min(start_x, w - target_w))
        
        return (start_x, 0, target_w, h)

    def smooth_coordinate(self, x: int) -> int:
        self.smoothing_window.append(x)
        if len(self.smoothing_window) > self.max_smoothing:
            self.smoothing_window.pop(0)
        return int(sum(self.smoothing_window) / len(self.smoothing_window))

    def process_frame(self, frame: np.ndarray) -> np.ndarray:
        focal_x, focal_y = self.get_focal_point(frame)
        smooth_x = self.smooth_coordinate(focal_x)
        
        x, y, w, h = self.calculate_crop_window(frame, (smooth_x, focal_y))
        return frame[y:y+h, x:x+w]