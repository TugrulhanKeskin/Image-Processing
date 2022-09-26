import cv2
import numpy as np


#içe aktar 
img = cv2.imread("bulut.png")
cv2.imshow("orjinal", img)


#yatay birleştirme 
hor = np.hstack((img, img)) #matrisin yatay eklenmesi
cv2.imshow("Horizontal", hor ,)


#dikey birleştirme 
ver = np.vstack((img,img)) #matrsin dikey eklenmesi 
cv2.imshow("Dikey", ver)

k =  cv2.waitKey(0) & 0xFF 
if k == 27: cv2.destroyAllWindows()
elif k == ord("s"): 
    cv2.imwrite("bulut.png", img)
    cv2.destroyAllWindows()