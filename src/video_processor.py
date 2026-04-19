import cv2
from src.model_impl import My_LicensePlate_Model


def process_video(input_path: str, output_path: str):
    model = My_LicensePlate_Model("weights/best.pt")

    cap = cv2.VideoCapture(input_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(
        output_path,
        fourcc,
        30.0,
        (int(cap.get(3)), int(cap.get(4)))
    )

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        detections = model.detect_plates(frame)

        for det in detections:
            x1, y1, x2, y2 = map(int, det["bbox"])

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

        out.write(frame)

    cap.release()
    out.release()