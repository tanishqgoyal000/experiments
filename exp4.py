import cv2

# Load OpenCV's built-in classifiers for faces and eyes
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    status = "No Face"

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Slice upper 60% of the face region (where eyes are located)
        roi_gray = gray[y : y + int(h * 0.6), x : x + w]
        roi_color = frame[y : y + int(h * 0.6), x : x + w]

        # Detect eyes inside the face region
        eyes = eye_cascade.detectMultiScale(
            roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30)
        )

        
        if len(eyes) >= 1:
            status = "Eyes Open"
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        else:
            status = "Eyes Closed"

    
    color = (0, 255, 0) if status == "Eyes Open" else (0, 0, 255)
    cv2.putText(frame, f"Status: {status}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Eye Open/Closed Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
