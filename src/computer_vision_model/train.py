from ultralytics import YOLO
from clearml import Task
from logger import get_logger

logger = get_logger()


def train():
    logger.info("Starting training")

    task = Task.init(
        project_name="LicensePlateDetection",
        task_name="YOLOv8 training"
    )

    model = YOLO('yolov8s.pt')

    results = model.train(
        data="dataset/data.yaml",
        epochs=100,
        imgsz=640,
        batch=8,
        project="runs/train",
        name="exp"
    )

    logger.info("Training finished")

    return results


if __name__ == "__main__":
    train()