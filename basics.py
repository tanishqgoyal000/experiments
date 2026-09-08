import cv2

# 1. Read Image
# Loads image from disk into a 3D NumPy array (BGR format)
img = cv2.imread("sample.jpg")

# 2. Color Space Conversions
# BGR to Grayscale (reduces 3 channels to 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# BGR to HSV (separates color tint from brightness)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 3. Resizing & Cropping
# cv2.resize uses (width, height) order
resized = cv2.resize(img, (400, 300))
# Cropping uses standard NumPy array slicing: img[y1:y2, x1:x2]
cropped = img[50:200, 100:300]

# 4. Drawing Annotations
# Draw Rectangle: (img, top_left, bottom_right, color_BGR, thickness)
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 2)

# Draw Circle: (img, center, radius, color_BGR, thickness=-1 for filled)
cv2.circle(img, (125, 125), 30, (0, 0, 255), -1)

# Write Text: (img, text, origin, font, scale, color_BGR, thickness)
cv2.putText(
    img,
    "OpenCV Basics",
    (50, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (255, 255, 255),
    2,
)

# 5. Display & Save
cv2.imshow("Original Annotated", img)
cv2.imshow("Grayscale", gray)

# Save processed image back to disk
cv2.imwrite("output_gray.jpg", gray)

# Wait until any key is pressed before closing windows
cv2.waitKey(0)
cv2.destroyAllWindows()
