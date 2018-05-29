import cv2
import values as val

try:
    cap = cv2.VideoCapture(val.inputPath+val.videoName)
except:
    print'Video not found!!'

frame_counter = 0
while(True):
    ret, frame = cap.read()

    #If the last frame is reached, reset the capture and the frame_counter
    if ret==False:
        cap = cv2.VideoCapture(val.inputPath + val.videoName)
        continue

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#release the capture and destroy the frames
cap.release()
cv2.destroyAllWindows()