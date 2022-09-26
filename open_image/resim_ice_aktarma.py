import cv2 

img = cv2.imread("bulut.jpg", 0) #içe aktarma
 
cv2.imshow("ilk resim", img) #görselleştirme

k = cv2.waitKey(0) &0xFF #harfe işlev atama 

if k ==27: #esc 
    cv2.destroyAllWindows() #kapat
elif k == ord("s"):
    cv2.imwrite("bulut_gray.png", img) #kaydet
    cv2.destroyAllWindows()