from ultralytics import YOLO
from ultralytics import solutions
import cv2


def track_create_heatmap():
    writer = None
    path = "images/cartracking_Resize.mp4"
    vs = cv2.VideoCapture(path)

    model = YOLO("yolov8l.pt")

    (grabbed, frame) = vs.read()
    if not grabbed:
        print("Failed to read video")
        return

    vs.set(cv2.CAP_PROP_POS_FRAMES, 0)

    heatmap_obj = solutions.Heatmap(
        model=model,
        colormap=cv2.COLORMAP_AUTUMN,
        show=False,
        # classes=[0, 2]
    )

    classes_for_heatmap = [0, 2]

    while True:

        (grabbed, frame) = vs.read()
        if not grabbed:
            break

        results = model.track(frame, persist=True, classes=classes_for_heatmap)

        if results and results[0].boxes is not None:

            heatmap_result = heatmap_obj(frame)

            if hasattr(heatmap_result, 'plot_im'):
                frame = heatmap_result.plot_im


            elif isinstance(heatmap_result, tuple) and len(heatmap_result) > 0:
                frame = heatmap_result[0]


            else:
                frame = heatmap_result

        cv2.imshow('Heatmap', frame)

        if writer is None:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            writer = cv2.VideoWriter("cartracking_Resize_result.mp4", fourcc, 24,
                                     (frame.shape[1], frame.shape[0]))
        writer.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vs.release()
    if writer:
        writer.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    track_create_heatmap()