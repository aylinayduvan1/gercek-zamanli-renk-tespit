import cv2
import numpy as np

#kameradan görüntü alabilmemiz için bu fonksiyonu kullanıyoruz..
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hvs_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#RED COLOR:
    #Alt değer.
    red_lower = np.array([161, 155, 84])
    #Üst değer.
    #Bu renkler arasındaki tüm tonları korusun geriye kalanları atsın.
    red_upper = np.array([179, 255, 255])
    red_mask = cv2.inRange(hvs_frame, red_lower, red_upper)
    #ekrana gösterilen kırmızı renkli objenin kırmızı olarak görünmesi için.
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

#YELLOW COLOR:
    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hvs_frame, yellow_lower, yellow_upper)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

#GREEN COLOR:
    green_lower = np.array([45, 100, 50])
    green_upper = np.array([75, 255, 255])
    green_mask = cv2.inRange(hvs_frame, green_lower, green_upper)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    cv2.imshow("Kamera", frame)
    #cv2.imshow("Kirmizi rengi gosteren ekran", red)
    cv2.imshow("Sari rengi gosteren ekran", yellow)
    #cv2.imshow("Yesil rengi gosteren ekran", green)

    #q tuşuna basıldığı zaman program dursun.
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
