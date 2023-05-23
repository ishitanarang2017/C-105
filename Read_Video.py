import cv2
video = cv2.VideoCapture("AnthonyShkraba.mp4")
if(video.isOpened()==False):
    print("unable to open the video")
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(video.get(cv2.CAP_PROP_FPS))
output = cv2.VideoWriter('AnthonyShkraba.mp4', cv2.VideoWriter_fourcc(*'DIVX'),30,(w,h))
while(True):
    ret,frame = video.read()
    cv2.imshow("my video",frame)
    output.write(frame)
    if(cv2.waitKey(25)==32):
        break
video.release()
output.release()
cv2.destroyAllWindows()