import cv2

# вывод картинки
"""img = cv2.imread('data/foto2.jpg')
cv2.imshow('Rezult', img)
cv2.waitKey(5000)"""

# Вывод видео
# выход из проги "q"
"""cap = cv2.VideoCapture('data/video.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Rezult', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break"""

cap = cv2.VideoCapture('data/video.mp4')
cap.set(3,300)
cap.set(4,200)

# Обработка  каждого кадра в видео

while True:

    ret, img = cap.read()

    # Изменение фрейма  видео
    img = cv2.GaussianBlur(img, (9,9), 0)


    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, 100, 100)

    cv2.imshow('Rezult', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
