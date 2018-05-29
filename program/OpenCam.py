import cv2

cap=cv2.VideoCapture(0)

outputPath='../output/'
outputVideoName='output.mp4'

ret,frame=cap.read()
h,w=frame.shape[:2]

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(outputPath+outputVideoName,fourcc, 10.0, (w,h))

while True:
    ret,frame=cap.read()
    cv2.imshow("image",frame)

    out.write(frame)

    if cv2.waitKey(33)&0xff==27:
        break

cap.release()
out.release()