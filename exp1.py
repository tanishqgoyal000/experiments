import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Define HSV range for green color
LOWER_GREEN = np.array([0, 0, 0])
UPPER_GREEN = np.array([210, 210, 210])

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    mask = cv2.inRange(hsv, LOWER_GREEN, UPPER_GREEN)
    
    
    masked_result = cv2.bitwise_and(frame, frame, mask=mask)
    
    
    

    cv2.imshow("Tracking", frame)
    cv2.imshow("Masked Output", masked_result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
