import sys
import cv2
from model_impl import My_LicensePlate_Model
from logger import get_logger

logger = get_logger()


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

    logger.info(f"Processing video: {input_path}")

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

    logger.info(f"Saved output: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python video_processor.py input.mp4 output.mp4")
        exit()

    process_video(sys.argv[1], sys.argv[2])