import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    frame_small = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    gray_small = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame_small)
    cv2.imshow('gray', gray_small)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
