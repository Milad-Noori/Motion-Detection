Motion Detection & Vehicle Tracking System (YOLOv8)

A real-time computer vision system for vehicle detection, tracking, and heatmap generation using YOLOv8 and OpenCV.

This project demonstrates object detection, tracking, and motion analysis for vehicles in video streams.




🚀 Features
🚗 Real-time vehicle detection using YOLOv8
🎯 Vehicle tracking across video frames
📊 Heatmap generation for movement analysis
📹 Video processing with OpenCV
📍 Counting line for vehicle analytics (custom implementation)
⚡ Fast inference using pretrained YOLO models
🧠 Tech Stack
Python
Ultralytics YOLOv8
OpenCV
NumPy
YOLO Tracking & Heatmap (Ultralytics Solutions)
📂 Project Structure
motion-detection/
│
├── main.py
├── modified_version.py
├── model/
│   └── yolov8l.pt (not included)
├── images/
│   └── sample videos/images
├── results/
├── requirements.txt
└── README.md
⚠️ Important Note (Models & Data)

Pretrained YOLO models and video files are not included in this repository due to their large size.

You can download YOLOv8 models automatically via Ultralytics:

yolo download model=yolov8l.pt

Or they will be downloaded automatically on first run.

🔗 Installation
1. Clone the repository
git clone https://github.com/Milad-Noori/Car_Motion-Detection.git
cd Car_Motion-Detection
2. Create virtual environment (recommended)
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt

Or manually:

pip install ultralytics opencv-python numpy
▶️ Run Project
Vehicle Detection & Tracking
python main.py
Heatmap Generation (Motion Analysis)
python modified_version.py
📊 How It Works
🔹 Detection Pipeline
Input Video
    ↓
YOLOv8 Object Detection
    ↓
Vehicle Filtering (Car, Bus, Truck, Motorcycle)
    ↓
Tracking IDs Assignment
    ↓
Motion Analysis
    ↓
Visualization (Bounding Boxes + Heatmap)
🚗 Vehicle Classes Used
Class ID	Object
2	Car
3	Motorcycle
5	Bus
7	Truck
📈 Features Explained
🎯 Vehicle Tracking

Tracks vehicles across frames using YOLO tracking.

📍 Counting Line

A horizontal baseline is drawn to analyze vehicle movement.

🔥 Heatmap Visualization

Generates movement intensity heatmap using Ultralytics solutions.

🧪 Example Output
Bounding boxes around vehicles
Real-time tracking IDs
Motion heatmap visualization
Video output saved with detections
🐳 Future Improvements
Vehicle speed estimation
Lane detection system
Real-time dashboard (Flask / Streamlit)
License plate recognition (ANPR)
Database logging system
API deployment
👨‍💻 Author

Milad Noori

GitHub: https://github.com/Milad-Noori
Machine Learning & Computer Vision Developer
⭐ If you like this project

Give it a ⭐ on GitHub and follow for more AI / CV projects.
