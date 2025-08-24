import cv2
import os

# Input and output folders
input_folder = "c:\\Users\\hp\\Downloads\\enhanced"
output_folder = "c:\\Users\\hp\\Downloads\\dark"

os.makedirs(output_folder, exist_ok=True)

def unsharp_mask(image, kernel_size=(5,5), sigma=1.0, amount=1.5, threshold=0):
    """
    Apply unsharp masking to sharpen the image naturally.
    - kernel_size: size of Gaussian blur
    - sigma: Gaussian blur sigma
    - amount: how much to add the sharpness
    - threshold: ignore sharpening for low-contrast pixels
    """
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = cv2.addWeighted(image, 1 + amount, blurred, -amount, 0)

    if threshold > 0:
        # Create mask to limit sharpening to significant edges
        low_contrast_mask = cv2.absdiff(image, blurred) < threshold
        sharpened = image.copy()
        sharpened[~low_contrast_mask] = sharpened[~low_contrast_mask]

    return sharpened

# Process all images
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        if img is None:
            print(f"⚠️ Skipping {filename}, could not read image.")
            continue

        # Apply unsharp mask for natural sharpening
        sharpened = unsharp_mask(img, amount=1.5, sigma=1.0)

        # Save output
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, sharpened)
        print(f"✅ Saved {output_path}")

print("🎉 All images naturally sharpened successfully!")



