# https://docs.ultralytics.com/models/yolov8
from ultralytics import YOLO

# path = "images/sampleImage.jpg"
# model = YOLO("model/yolov10x.pt")
#  5 persons, 16 cars, 409.4ms - Speed: 2.2ms

# model = YOLO("model/yolov8x.pt")
#  5 persons, 22 cars, 1 truck, 1 traffic light, 519.7ms Speed: 1.7ms

# region Method 1


# region Step 1 ...

# results = model.predict(source=path)
# results[0].show()
# print(results[0].names)

# endregion

# region Step 2 ...

# path = "images/sampleImage.jpg"
# model = YOLO("yolov8n.pt")
# results = model.predict(source=path, classes=[2])
# results[0].show()

# endregion

# region Step 3 ...

# path = "images/sampleImage.jpg"
# model = YOLO("model/yolov8x.pt")
# selected_class = [0,2]
# results = model.predict(source=path, classes=selected_class, save=True, conf = 0.7)
# results[0].show()

# endregion

# region Step 4 ...

# path = "images/sampleImage.jpg"
# model = YOLO("model/yolov8x.pt")
# selected_class = [0,2]
# results = model.predict(source=path, classes=selected_class, save=True, conf = 0.7)
# results[0].show()
# results[0].save(filename="result.jpg")

# endregion


# endregion
# ---------------------------------------------------------------
# region Method 2

# import cv2
# from ultralytics import YOLO
#
#
# def process_video(path: str):
#     vs = cv2.VideoCapture(path)
#     model = YOLO("model/yolov8x.pt")
#
#     while True:
#         (grabbed, frame) = vs.read()
#         if not grabbed:
#             break
#         results = model.predict(frame, stream=False)
#         detection_classes = results[0].names
#         # results[0].show()
#         for result in results:
#             for data in result.boxes.data.tolist():
#                 # print(data)
#                 code = data[5]
#                 draw_box(data=data, image=frame, name=detection_classes[code])
#         cv2.imshow("Frame", frame)
#         cv2.waitKey(1)
#
#
# def draw_box(data, image, name):
#     (x1, y1, x2, y2, confidence, code) = data
#     p1 = (int(x1)-3, int(y1)-2)
#     p2 = (int(x2)+2, int(y2)+1)
#     cv2.rectangle(image, p1, p2, (0, 0, 255), 3)
#     cv2.putText(image, name, p1, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
#     return image
#
#
# process_video(path='images/traffic.mp4')

# endregion
# ------------------------------------------------------------------

import numpy as np
from ultralytics import YOLO
import cv2 as cv


class VehicleTracker:
    def __init__(self):
        self.counter_cache = []
        self.vehicle_count = 0
        self.track_history = {}

        # Load YOLO Model
        print("Loading YOLO model ...")
        self.model = YOLO('model/yolov8x.pt')
        print("Model loaded successfully ...")

        # 2: Car, 3: Motorcycle, 5: Bus, 7: Truck
        self.vehicle_classes = [2, 3, 5, 7]
    def process_video(self, video_path):
        cap = cv.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Error!!! => Could not open video  {video_path}")
            return

        # Get Video properties
        fps = int(cap.get(cv.CAP_PROP_FPS))  # نرخ فریم در ثانیه
        width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        print(f"Video Info: {width}x{height} and FPS: {fps}")

        cv.namedWindow('Vehicle Tracking and Counting', cv.WINDOW_NORMAL)

        while True:
            # Read Frame
            ret, frame = cap.read()
            if not ret:
                break
            display_frame = frame.copy()
            self.draw_counting_line(display_frame)
            #TODO: ...


    def draw_counting_line(self, frame):
        height, width = frame.shape[:2]
        # پا تهی گشتن به است از کفش تنگ

        line_y = height // 2
        cv.line(frame, (0, line_y), (width, line_y), (255, 0, 0), 2)

        cv.putText(frame, 'Base Line', (width // 2 - 300, line_y - 5),
                   cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2 )
        return frame


    # CNN











