## to convert image into water color painting
## input image and resize it 
# we will resize the image so that any algo can work on it 
# like when we apply kernel(matrix) of 3x3 on a picture of 300px and on a picture on 500px it will result different
## clear the impurities 
# the impurities may be color variations due to which filters may lag. gaussian filter or median blur etc.
## apply filtering 
# create the effect that is desired on image --> gausian or bilateral filtering
## tune the art
# Tuning may include sharpening,dehazing,contrast enhancement etc.

import cv2
import numpy as np

# ------phase 1
# reading the image
image=cv2.imread('shruti.jpg')

# resizing the image
# interpolation is cubic for best results
image_resized=cv2.resize(image,None,fx=0.5,fy=0.5)

# ------phase 2
# removing impurities from image
# here we have applied median blur function for three times for better bluring 
# function put 3x3 matrix all over the image and try to put median of all the values of matrix at centre of matrix
image_cleared=cv2.medianBlur(image_resized,3)
image_cleared=cv2.medianBlur(image_cleared,3)
image_cleared=cv2.medianBlur(image_cleared,3)

#edgePreservingFilter() will constant the picture that means constant the color variations all over the image
# sigma_s is that extent upto which it will merge the colors it should be small to get less blurry image
image_cleared=cv2.edgePreservingFilter(image_cleared,sigma_s=5)

## -----phase 3
# bilateral image filtering -> isme gaussian space ke sath gausian intensity bhi consider hota h

# diameter =3 mtlb kitne diameter tkk milana h 
# sigma color=10 hai mtlb ki kitne extent tk clor ko mila deta h and slowly we will increase it
image_filtered=cv2.bilateralFilter(image_cleared,3,10,5)

for i in range(2):
    image_filtered=cv2.bilateralFilter(image_filtered,3,20,10)

for i in range(3):
    image_filtered=cv2.bilateralFilter(image_filtered,5,30,10)

## more filtering more will be cartoonified image

# for i in range(3):
#     image_filtered=cv2.bilateralFilter(image_filtered,5,40,10)

# for i in range(2):
#     image_filtered=cv2.bilateralFilter(image_filtered,3,40,5)


#------phase 4
#sharpening the image by addweighted()
gaussian_mask=cv2.GaussianBlur(image_filtered,(7,7),2)
# we have to make result=1 
# image_filtered*1.5+gaussian_mask*-0.5+0=1 --------  1.5-0.5+0
image_sharp=cv2.addWeighted(image_filtered,1.5,gaussian_mask,-0.5,0)

image_sharp=cv2.addWeighted(image_sharp,1.4,gaussian_mask,-0.2,10)


# displaying image
cv2.imshow('Final image',image_sharp)
cv2.imshow('clear impurities',image_cleared)
cv2.imshow('original',image_resized)
cv2.imwrite('test1.jpg',image_sharp)
cv2.waitKey(0)
