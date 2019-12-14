import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("/home/shikha/Documents/road1.jpeg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("hello")
blur=cv2.GaussianBlur(gray,(5,5),0)
edges=cv2.Canny(blur,75,150)
width=img.shape[1]
height=img.shape[0]
print(edges.shape)
cv2.imshow("IMAGE", edges)


mask = np.zeros([height, width])

for i in range(height):
    for j in range(width):
        if i > -(height/width)*j + height and i > (height/width)*j:
           mask[i,j] = 1

edge = edges*mask
cv2.imshow("IMG", edge)

#polygens=np.array([[(1260,height),(1330,height),(1300,1020)]])

#def region_of_interest(edges,polygens):
#    height=img.shape[0]
#    mask=np.zeros_like(img)
#    masks=cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
#    print(masks.shape)
#    cv2.fillPoly(masks, polygens, 255)
#    print(masks)
#    if edges.shape==masks.shape:
#       masked_image=cv2.bitwise_and(edges,masks)
#    else:
#       masked_image=cv2.bitwise_not(edges,masks)
#    return masked_image
#polygens=np.array([[(400,height),(970,height),(450,854)]])
#print(polygens)
#masking=region_of_interest(edges,polygens)
#print(masking)

#cv2.imshow("masking",masking)
#cv2.imshow("canny",edges)
cv2.waitKey(0)
#cv2.destroyAllwindows()
#lines=cv2.HoughLinesP(edges,1,np.pi/180,30,maxLineGap=250)
#p=len(lines)
#print(lines)
#print(p)

#for i in range(len(lines)):
 #    x1,x2,y1,y2=lines[i][0][0],lines[i][0][1],lines[i][0][2],lines[i][0][3]
 #    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3)


