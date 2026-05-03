import cv2
import numpy as np

# Load image with alpha channel
img = cv2.imread('logo.png', cv2.IMREAD_UNCHANGED)

# If image has no alpha channel, add one
if img.shape[2] == 3:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

# Define the background color and a tolerance
bg_color = np.array([223, 220, 217, 255]) # BGR for (217,220,223)
tolerance = 30

# Create mask for background
lower_bound = np.clip(bg_color - tolerance, 0, 255)
upper_bound = np.clip(bg_color + tolerance, 0, 255)
bg_mask = cv2.inRange(img, lower_bound, upper_bound)

# Set background to transparent
img[bg_mask != 0] = [0, 0, 0, 0]

# Now let's make the dark text white so it's readable on dark mode
# Find dark pixels (text is usually black/dark blue)
dark_mask = cv2.inRange(img, np.array([0, 0, 0, 0]), np.array([100, 100, 100, 255]))

# Only modify pixels that are not transparent
valid_mask = img[:, :, 3] > 0
final_dark_mask = cv2.bitwise_and(dark_mask, dark_mask, mask=valid_mask.astype(np.uint8))

img[final_dark_mask != 0] = [255, 255, 255, 255]

# Trim the transparent borders
# Get bounding box of non-transparent pixels
coords = cv2.findNonZero(img[:, :, 3])
x, y, w, h = cv2.boundingRect(coords)
trimmed_img = img[y:y+h, x:x+w]

cv2.imwrite('logo_clean.png', trimmed_img)
print("Saved logo_clean.png")
