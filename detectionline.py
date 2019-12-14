import cv2                
import numpy as np

img=cv2.imread("/home/shikha/Documents/road1.jpeg")  # read rgb image
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # convert bgr image to gray


blur=cv2.GaussianBlur(gray,(5,5),0)  #use 5*5 Gaussian kernel for image smoothing 

edges=cv2.Canny(blur,75,150)         # use canny for edge detection in smooth image

width=img.shape[1]
height=img.shape[0]

mask = np.zeros([height, width])     # create a mask so that we take only detected region point(edge) on it

def region(mask):         
    for i in range(height):
        for j in range(width):
            if i > -(height/width)*j + height and i > (height/width)*j: 
               mask[i,j] = 1
    return mask       # sensor light only detect downhalf area edge so we find those edges


mask1 = region(mask)   # call region
detected_edge = edges*mask1     # then we multply edge with mask


cv2.imshow("IMG", detected_edge)
cv2.waitKey(0)
