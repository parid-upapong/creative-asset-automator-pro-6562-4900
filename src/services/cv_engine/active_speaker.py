import mediapipe as mp
import numpy as np

class ActiveSpeakerDetector:
    """
    Detects which person is talking based on lip movement synchronization.
    """
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=4,
            refine_landmarks=True,
            min_detection_confidence=0.5
        )
        # Lip landmarks indices in MediaPipe FaceMesh
        self.LIP_UPPER = [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291]
        self.LIP_LOWER = [146, 91, 181, 84, 17, 314, 405, 321, 375, 291]

    def get_mouth_opening_ratio(self, landmarks, image_width, image_height):
        """
        Calculates the distance between upper and lower lips.
        """
        upper_y = np.mean([landmarks[i].y for i in self.LIP_UPPER])
        lower_y = np.mean([landmarks[i].y for i in self.LIP_LOWER])
        return abs(lower_y - upper_y)

    def identify_speaker(self, frame):
        results = self.face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if not results.multi_face_landmarks:
            return None
            
        scores = []
        for face_landmarks in results.multi_face_landmarks:
            ratio = self.get_mouth_opening_ratio(
                face_landmarks.landmark, 
                frame.shape[1], 
                frame.shape[0]
            )
            scores.append(ratio)
            
        # Returns index of the face with the largest mouth movement
        return np.argmax(scores) if scores else None