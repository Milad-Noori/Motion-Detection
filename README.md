# 🚗 Car Motion Detection & Vehicle Tracking System

A real-time computer vision project for vehicle detection, tracking, and motion analysis using YOLOv8 and OpenCV.

This system can detect vehicles in videos, track their movement across frames, generate motion heatmaps, and serve as a foundation for traffic monitoring and intelligent transportation applications.

---

## 🚀 Features

- Real-time vehicle detection using YOLOv8
- Multi-object vehicle tracking
- Motion heatmap generation
- Vehicle movement visualization
- Video processing with OpenCV
- Counting line implementation
- Support for cars, motorcycles, buses, and trucks
- Export processed video results

---

## 🧠 Technologies Used

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- NumPy

---

## 📂 Project Structure

```text
Car_Motion-Detection/
│
├── main.py
├── modified_version.py
├── model/
│   └── yolov8x.pt
│
├── images/
│   ├── sampleImage.jpg
│   └── traffic.mp4
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Milad-Noori/Car_Motion-Detection.git
cd Car_Motion-Detection
```

### 2. Create a virtual environment (optional)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

```txt
ultralytics
opencv-python
numpy
torch
torchvision
matplotlib
```

---

## ▶️ Running the Project

### Vehicle Detection and Tracking

```bash
python main.py
```

### Heatmap Generation

```bash
python modified_version.py
```

---

## 🚗 Supported Vehicle Classes

| Class ID | Vehicle Type |
|-----------|-------------|
| 2 | Car |
| 3 | Motorcycle |
| 5 | Bus |
| 7 | Truck |

---

## 🔄 Detection Pipeline

```text
Input Video
     │
     ▼
YOLOv8 Detection
     │
     ▼
Vehicle Filtering
     │
     ▼
Object Tracking
     │
     ▼
Motion Analysis
     │
     ▼
Heatmap / Visualization
```

---

## 📊 Example Applications

- Traffic monitoring
- Vehicle counting
- Smart city analytics
- Parking management systems
- Transportation research
- Road surveillance

---

## ⚠️ Note

Pretrained YOLO models (`.pt`) and large video files are not included in this repository due to their size.

The required model will be downloaded automatically by Ultralytics when running the project for the first time.

---

## 🔮 Future Improvements

- Vehicle speed estimation
- License plate recognition (ANPR)
- Lane detection
- Traffic density analysis
- Flask/FastAPI deployment
- Real-time webcam support

---

## 👨‍💻 Author

**Milad Noori**

Machine Learning Engineer | Computer Vision Developer

GitHub:
https://github.com/Milad-Noori

---

## 📜 License

This project is licensed under the MIT License.
