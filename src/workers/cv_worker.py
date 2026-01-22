import celery
from src.services.cv_engine.reframer import SmartReframer
from src.services.cv_engine.scene_detector import SceneProcessor
import cv2

app = celery.Celery('cv_tasks', broker='redis://localhost:6379/0')

@app.task(name="pipeline.reframer.execute")
def process_video_reframe(input_path: str, output_path: str):
    """
    Worker task to perform end-to-end reframing on a video file.
    """
    cap = cv2.VideoCapture(input_path)
    reframer = SmartReframer(target_ratio=9/16)
    
    # Get original properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Peek first frame to get dimensions
    ret, frame = cap.read()
    if not ret: return False
    
    reframed_sample = reframer.process_frame(frame)
    h, w = reframed_sample.shape[:2]
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))
    
    # Reset capture and process
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        
        processed = reframer.process_frame(frame)
        out.write(processed)
        
    cap.release()
    out.release()
    return {"status": "success", "output": output_path}

@app.task(name="pipeline.scenes.detect")
def analyze_scenes(video_path: str):
    processor = SceneProcessor()
    scenes = processor.detect_scenes(video_path)
    return {"scenes_count": len(scenes), "timestamps": scenes}