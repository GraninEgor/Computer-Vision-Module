# License Plate Detection System

## Author

**Full Name:** Гранин Егор Вадимович
**Group:** 972401

---

# Project Description

This project implements a computer vision system for **license plate detection (ALPR/ANPR)** using the **YOLOv8 architecture (Ultralytics)**.

The system is designed for real-time and offline processing scenarios and includes a full machine learning pipeline:

* Dataset preparation and annotation
* Model training (YOLOv8 fine-tuning)
* Experiment tracking with ClearML
* Evaluation (mAP, precision, recall, latency)
* Inference on video files
* Real-time webcam detection
* Logging system for debugging and monitoring

---

# Project Structure

```
LicensePlateDetection/
│
├── src/
│   ├── model_impl.py        # YOLO wrapper class
│   ├── train.py             # training script (ClearML)
│   ├── video_processor.py   # video inference
│   ├── camera.py            # webcam inference
│   ├── logger.py            # logging system
│
├── weights/
│   └── best.pt              # trained model weights
│
├── data/
│   ├── log_file.log         # logs
│   └── dataset.yaml         # dataset config
│
├── Dockerfile
├── docker-compose.yaml
├── pyproject.toml
└── README.md
```

---

# Requirements

* Python 3.10+
* Poetry
* Docker (optional)
* NVIDIA GPU (recommended for training)

Main libraries:

* ultralytics (YOLOv8)
* opencv-python
* numpy
* clearml
* logging (built-in)

---

# Installation (Without Docker)

Clone repository:

```bash
git clone <repo_url>
cd LicensePlateDetection
```

Install dependencies:

```bash
poetry install
```

Activate environment:

```bash
poetry env activate
```

---

# Training Model (Deep Learning Part)

Training is performed using YOLOv8 with ClearML experiment tracking.

### Run training:

```bash
python src/train.py
```

### Training process includes:

* Loading pretrained YOLOv8 model
* Fine-tuning on custom dataset
* Logging metrics to ClearML
* Saving best weights to `weights/best.pt`

---

# Model Evaluation

Evaluation metrics:

* mAP@0.5
* mAP@0.5:0.95
* Precision
* Recall
* Latency (FPS)

### Run validation:

(implemented inside training or separately via Ultralytics)

---

# Video Processing (Inference)

Process a video file and save results:

```bash
python src/video_processor.py input.mp4 output.mp4
```

Output video will contain bounding boxes around detected license plates.

---

# Real-Time Camera Inference

Run webcam detection:

```bash
python src/camera.py
```

Press `Q` to exit.

## Build image

```bash
docker build -t license-plate-detection .
```

## Run container

### Video mode:

```bash
docker run -v $(pwd)/data:/app/data -v $(pwd)/weights:/app/weights license-plate-detection
```

---


# Metrics Explanation

### mAP (mean Average Precision)

Measures detection accuracy and bounding box quality.

### Precision

How many detected objects are correct.

### Recall

How many real objects were detected.

### Latency

Processing time per frame (FPS).

---

# How to Run Project

## Training

```bash
python src/train.py
```

## Video inference

```bash
python src/video_processor.py input.mp4 output.mp4
```

## Webcam inference

```bash
python src/camera.py
```

