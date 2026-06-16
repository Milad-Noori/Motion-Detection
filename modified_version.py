import cv2
from ultralytics import YOLO, solutions


def get_video_properties(video_capture):
    """Extracts and returns video metadata dynamically."""
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))

    # Fallback to 24 FPS if metadata is corrupted
    actual_fps = fps if fps > 0 else 24
    return width, height, actual_fps


def generate_video_heatmap(input_path: str, output_path: str, target_classes: list):
    """
    Processes the input video, tracks specified classes using YOLO,
    generates a real-time heatmap overlay, and writes the output to a file.
    """
    # Initialize video capture
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"[Error] Could not open source video: {input_path}")
        return

    # Get dynamic video configurations
    frame_width, frame_height, fps = get_video_properties(cap)

    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Initialize YOLO model and Heatmap tool
    yolo_model = YOLO("yolov8l.pt")
    heatmap_overlay = solutions.Heatmap(
        model=yolo_model,
        colormap=cv2.COLORMAP_AUTUMN,
        show=False,
        classes=target_classes
    )

    print(f"[Info] Processing started. Exporting to: {output_path}")

    try:
        while cap.isOpened():
            success, current_frame = cap.read()
            if not success:
                break

            # Core processing: tracking and heatmap extraction combined
            processed_frame = heatmap_overlay.generate_image(current_frame)

            # Display real-time output in a GUI window
            cv2.imshow("Traffic Analytics - Heatmap Engine", processed_frame)

            # Stream frame to the output video file
            video_writer.write(processed_frame)

            # Standard exit on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("[Info] Process interrupted by user.")
                break
    finally:
        # Safe resource cleanup
        cap.release()
        video_writer.release()
        cv2.destroyAllWindows()
        print("[Info] Resources released. Processing complete.")


if __name__ == "__main__":
    # Project configurations
    VIDEO_SOURCE = "images/Highway.mp4"
    VIDEO_OUTPUT = "Highway_Resize_result.mp4"
    CLASSES_TO_TRACK = [0, 2]  # 0: Person, 2: Car

    # Execute main pipeline
    generate_video_heatmap(
        input_path=VIDEO_SOURCE,
        output_path=VIDEO_OUTPUT,
        target_classes=CLASSES_TO_TRACK
    )