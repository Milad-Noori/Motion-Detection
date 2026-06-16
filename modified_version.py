import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import cv2
from ultralytics import YOLO, solutions

input_video_path = ""
output_video_path = ""


def get_video_properties(video_capture):

    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    actual_fps = fps if fps > 0 else 24
    return width, height, actual_fps


def generate_video_heatmap(input_path: str, output_path: str, target_classes: list):

    try:

        status_label.config(text="Status: Initializing YOLO & Video...", fg="blue")
        start_button.config(state=tk.DISABLED)


        cap = cv2.VideoCapture(input_path)
        if not cap.isOpened():
            messagebox.showerror("Error", f"Could not open source video:\n{input_path}")
            reset_ui_status()
            return

        frame_width, frame_height, fps = get_video_properties(cap)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

        # Load AI models
        yolo_model = YOLO("yolov8l.pt")
        heatmap_overlay = solutions.Heatmap(
            model=yolo_model,
            colormap=cv2.COLORMAP_AUTUMN,
            show=False,
            classes=target_classes
        )

        status_label.config(text="Status: Processing Video (Press 'q' in video window to stop)...", fg="orange")

        while cap.isOpened():
            success, current_frame = cap.read()
            if not success:
                break
            processed_frame = heatmap_overlay.generate_image(current_frame)


            cv2.imshow("Traffic Analytics - Heatmap Engine", processed_frame)


            video_writer.write(processed_frame)

            # Break if user presses 'q' inside the OpenCV window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        messagebox.showerror("Processing Error", f"An error occurred during execution:\n{str(e)}")

    finally:

        cap.release()
        video_writer.release()
        cv2.destroyAllWindows()
        reset_ui_status()
        messagebox.showinfo("Success", "Video processing completed successfully!")


def reset_ui_status():

    status_label.config(text="Status: Idle", fg="black")
    start_button.config(state=tk.NORMAL)




def select_video():
    global input_video_path
    chosen_file = filedialog.askopenfilename(
        title="Select Input Video",
        filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")]
    )
    if chosen_file:
        input_video_path = chosen_file
        # Truncate text if too long for the label
        display_text = input_video_path if len(input_video_path) < 60 else f"...{input_video_path[-57:]}"
        video_label.config(text=display_text, fg="green")


def select_output():
    global output_video_path
    chosen_path = filedialog.asksaveasfilename(
        title="Save Processed Video As",
        defaultextension=".mp4",
        filetypes=[("MP4 Video", "*.mp4")]
    )
    if chosen_path:
        output_video_path = chosen_path
        display_text = output_video_path if len(output_video_path) < 60 else f"...{output_video_path[-57:]}"
        output_label.config(text=display_text, fg="green")


def start_processing():
    if not input_video_path:
        messagebox.showerror("Error", "Please select an input video first!")
        return

    if not output_video_path:
        messagebox.showerror("Error", "Please choose an output save path!")
        return


    tracking_thread = threading.Thread(
        target=generate_video_heatmap,
        args=(input_video_path, output_video_path, [0, 2]),
        daemon=True
    )
    tracking_thread.start()


root = tk.Tk()
root.title("YOLO Real-Time Traffic Heatmap Analytics")
root.geometry("650x380")
root.resizable(False, False)


main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

title_label = tk.Label(main_frame, text="YOLO Video Heatmap Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=(0, 20))


input_btn = tk.Button(main_frame, text="📁 Select Input Video", command=select_video, width=20, font=("Arial", 10))
input_btn.pack(pady=5)

video_label = tk.Label(main_frame, text="No input file selected", font=("Arial", 9, "italic"), fg="gray")
video_label.pack(pady=(0, 15))


output_btn = tk.Button(main_frame, text="💾 Select Output Path", command=select_output, width=20, font=("Arial", 10))
output_btn.pack(pady=5)

output_label = tk.Label(main_frame, text="No output destination selected", font=("Arial", 9, "italic"), fg="gray")
output_label.pack(pady=(0, 20))


separator = ttk.Separator(main_frame, orient='horizontal')
separator.pack(fill='x', pady=10)


start_button = tk.Button(
    main_frame,
    text="Start AI Processing",
    command=start_processing,
    bg="#2ecc71",
    fg="white",
    font=("Arial", 11, "bold"),
    activebackground="#27ae60",
    activeforeground="white",
    width=25,
    pady=5
)
start_button.pack(pady=10)

status_label = tk.Label(main_frame, text="Status: Idle", font=("Arial", 10, "bold"), fg="black")
status_label.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))


root.mainloop()