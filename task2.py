import numpy as np
import cv2

I = cv2.imread('sign.jpg')

p1 = (135,105)
p2 = (331,143)
p3 = (356,292)
p4 = (136,290)

points1 = np.array([p1,p2,p3,p4], dtype=np.float32)

p11 = (0,0)
p22 = (480, 0)
p33 = (480,320)
p44 = (0, 320)

points2 = np.array([p11,p22,p33,p44], dtype=np.float32)

n = 480
m = 320
output_size = (n,m)

H = cv2.getPerspectiveTransform(points1, points2)
J = cv2.warpPerspective(I,H, output_size)

# mark corners of the plate in image I
for i in range(4):
    cv2.circle(I, (int(points1[i,0]), int(points1[i,1])), 5, [0,0,255],2)

cv2.imshow('I', I);
cv2.waitKey(0)

cv2.imshow('J', J);
cv2.waitKey(0)
