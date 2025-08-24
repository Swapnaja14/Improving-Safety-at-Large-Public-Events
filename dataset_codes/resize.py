# OpenCV
# Resizing images into 640x640 with YOLO-compatibility

import cv2
import os
import numpy as np

# Input and output folder paths
input_folder = "c:\\Users\\hp\\Downloads\\input"
output_folder = "c:\\Users\\hp\\Downloads\\output"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

def letterbox_image(image, size=(640, 640)):
    h, w = image.shape[:2]
    scale = min(size[0] / w, size[1] / h)  # scale factor
    new_w, new_h = int(w * scale), int(h * scale)

    # Resize image with aspect ratio preserved
    resized_image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_LINEAR)

    # Create new image (black background)
    new_image = np.full((size[1], size[0], 3), 0, dtype=np.uint8)

    # Compute padding (centered)
    top = (size[1] - new_h) // 2
    left = (size[0] - new_w) // 2

    # Place resized image inside black background
    new_image[top:top + new_h, left:left + new_w] = resized_image

    return new_image

# Process all images
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        if img is None:
            print(f"⚠️ Skipping {filename}, could not read image.")
            continue

        # Letterbox resize
        resized = letterbox_image(img, size=(640, 640))

        # Save output
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, resized)
        print(f"✅ Saved {output_path}")

print("🎉 All images resized with letterbox (YOLO format)!")
