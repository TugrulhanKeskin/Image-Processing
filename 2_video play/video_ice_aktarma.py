import cv2
import time

video_name = "MOT17-04-DPM.mp4" #içe aktarıcağımız video ismi

cap = cv2.VideoCapture(video_name) #video içe aktar: capture: cap:

print("Genişlik : ", cap.get(3))
print("Yükseklik :", cap.get(4))

if cap.isOpened() == False: #video açıldı mı kontrol
    print("Hata")


while True: #resmi ard arda okuma işlemi
    ret, frame = cap.read() #cap.read() bize 2 şey döndürür return : işlem başarısı , : frame : kare sayısı

    if ret == True:

        time.sleep(0.01) #resimlerin ard arda hızlı şekilde oynamasını engellemek için
        cv2.imshow("Video", frame)
    else : break  #sıralıcak resim kalmadığında döngüden çık

    if cv2.waitKey(1) & 0xFF == ord("q"): #çıkma tuşu  q
        break

cap.relase() #stop capture
cv2.destroyAllWindows() # açık pencereleri kapat
