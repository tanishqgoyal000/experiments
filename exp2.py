import cv2

cap = cv2.VideoCapture(0)

# Load OpenCV's built-in Haar Cascade face classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract face region
        face_roi = frame[y:y+h, x:x+w]
        
        # Apply heavy Gaussian blur to the face ROI
        blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)
        
        # Overlay blurred ROI back into frame
        frame[y:y+h, x:x+w] = blurred_face
        

    cv2.imshow("Privacy Blur Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
