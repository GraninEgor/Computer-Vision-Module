import numpy as np
from ultralytics import YOLO


class My_LicensePlate_Model:
    def __init__(self, model_path: str):
        self.model = YOLO(model_path)

    def detect_plates(self, frame: np.ndarray) -> list[dict]:
        results = self.model(frame)[0]

        detections = []

        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = float(box.conf[0])

            detections.append({
                "bbox": [x1, y1, x2, y2],
                "confidence": conf
            })

        return detections