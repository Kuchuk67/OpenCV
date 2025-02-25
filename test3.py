import cv2
import numpy as np

img_0 = cv2.imread('data/foto3.jpg')
img = cv2.cvtColor(img_0, cv2.COLOR_BGR2GRAY)
#img = cv2.GaussianBlur(img,(9, 9), 0)

# подключает данные ИИ
faces = cv2.CascadeClassifier('data/ai.xml')
# поиск координат объектов
result = faces.detectMultiScale(img, scaleFactor=1.2, minNeighbors=3)

# строим по найденным координатам квадратики
for (x, y, w, h) in result:
    cv2.rectangle(img_0, (x, y), (x+w, y+h), (255, 0, 0), 2)

    #roi_gray = img[y:y+h, x:x+w]
    #roi_color = img[y:y+h, x:x+w]

cv2.imshow('Rezult', img_0)
cv2.waitKey(5000)

new_img= np.zeros(img.shape, dtype='uint8')


