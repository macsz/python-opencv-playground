import cv2
import os

cap = cv2.VideoCapture(0)
output_file = "recording.avi"

camera_x = int(cap.get(3))
camera_y = int(cap.get(4))
camera_fps = int(cap.get(5))

# List of codecs:
# https://gist.github.com/takuma7/44f9ecb028ff00e2132e
#
# Windows:
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# OSX
fourcc = cv2.VideoWriter_fourcc(*'avc1')

# to avoid "mMovieWriter.status: 3. Error: Cannot Save" delete output file (if exists)
if os.path.exists(output_file):
    os.remove(output_file)
out = cv2.VideoWriter(output_file, fourcc, camera_fps, (camera_x, camera_y))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(gray)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
