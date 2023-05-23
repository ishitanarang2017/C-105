import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
#print(len(images))
count = len(images)
frame = cv2.imread(images[0])
h,w, channel = frame.shape
size = (w,h)
output = cv2.VideoWriter('myproject.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),5,size)
#sunrise
#for i in range(count-1,0,-1):
#sunset
for i in range(0,count -1):
    frame=cv2.imread(images[i])
    cv2.imshow("myvideo",frame)
    output.write(frame)
    if(cv2.waitKey(25)==32):
        break

    
output.release()