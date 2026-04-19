import cv2
from model_impl import My_LicensePlate_Model
from logger import get_logger

logger = get_logger()

def run_camera():
    logger.info("Starting camera mode")

    model = My_LicensePlate_Model("weights/best.pt")
    logger.info("Model loaded")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        logger.error("Camera not opened")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            logger.error("Failed to read frame")
            break

        detections = model.detect_plates(frame)

        for det in detections:
            x1, y1, x2, y2 = map(int, det["bbox"])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    logger.info("Camera stopped")


if __name__ == "__main__":
    run_camera()