# 🚦 Traffic Violation Detection using YOLOv3

This project detects traffic signal violations using YOLOv3.

YoloV3 is optimized code data runner to identify the signal and traffic violation lines.
Traffic Violation Detection using YOLOv3

Real-time traffic violation detection using YOLOv3 for object detection (vehicles, persons, riders, helmets, traffic lights) plus rule engines for:

Helmet violation (rider without helmet)

Triple riding / pillion count

No seatbelt (if using car driver crops)

Red-light jump (line crossing + signal state)

Wrong-way / lane discipline

Overspeeding (speed estimation via tracking + calibration)

Supports webcam/RTSP, offline videos, and images. Includes optional DeepSORT/OC-SORT tracking, automatic license plate capture frames, and CSV/JSON logging.

✨ Features

YOLOv3 detector (COCO / custom classes).

Pluggable tracker (DeepSORT or OC-SORT).

Region of Interest (ROI) & virtual lines for red-light / lane rules.

Speed estimation with simple homography calibration.

Per-violation snapshots, short clips (optional), and structured logs.

Easy config via configs/enhanced_config.yaml.
🔧 Requirements

Python 3.8–3.11

OpenCV (with FFMPEG support)

PyTorch or Darknet backend (choose one; PyTorch default here)

NumPy, SciPy, pyyaml, tqdm

For tracking: filterpy, lap, sklearn (DeepSORT) or OC-SORT deps

Optional: CUDA 11+ for GPU inference
## 📥 Pretrained Weights

This project requires `yolov3.weights` (~236 MB).  
Download using Python gdown:

```bash
pip install gdown
python -m gdown "https://drive.google.com/uc?export=download&id=1D8X26t2PJxuKI2B7XMJfmwbaywXN5jIz" -O yolov3.weights
