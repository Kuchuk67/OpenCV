import cv2

# вывод картинки
"""img = cv2.imread('data/foto2.jpg')
cv2.imshow('Rezult', img)
cv2.waitKey(5000)"""

# Вывод видео
"""cap = cv2.VideoCapture('data/video.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Rezult', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break"""

cap = cv2.VideoCapture(0)
cap.set(3,300)
cap.set(4,200)
while True:
    ret, img = cap.read()








    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Rezult', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
