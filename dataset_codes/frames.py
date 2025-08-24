# OpenCV
# For extracting frames from videos--> 1 frame per second

import cv2
import os
import math

# List of video file paths
video_paths = [
    r"c:\Users\hp\Downloads\EDI\video1.mp4",
    r"c:\Users\hp\Downloads\EDI\video2.mp4"
]

# Output folder for extracted frames
output_folder = "dataset/safe"
os.makedirs(output_folder, exist_ok=True)

frame_count = 0  # Counts across all videos
frame_rate = 1   # seconds between frames

for video_path in video_paths:
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_seconds = math.ceil(total_frames / fps)  # round UP to capture last frame

    print(f"Processing {video_path} ({duration_seconds} seconds)")

    for sec in range(duration_seconds):
        cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
        ret, frame = cap.read()
        if ret:
            frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved {frame_filename}")
            frame_count += 1

    cap.release()

print("✅ Frame extraction completed for all videos.")
