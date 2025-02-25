import cv2
# выход из проги "q"

cap = cv2.VideoCapture('data/video2.mp4')
cap.set(3,300)
cap.set(4,200)


i=0
while True:

    i = + 1
    if i // 2 != i % 2:


        ret, img_orig = cap.read()

        # Изменение фрейма  видео
        #img = cv2.GaussianBlur(img, (9,9), 0)

        img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
        #img = cv2.Canny(img, 100, 150)
        # подключает данные ИИ
        faces = cv2.CascadeClassifier('data/ai.xml')
        # поиск координат объектов
        result = faces.detectMultiScale(img, scaleFactor=2, minNeighbors=3)
        # строим по найденным координатам квадратики
        for (x, y, w, h) in result:
            cv2.rectangle(img_orig, (x, y), (x + w, y + h), (0, 0, 255), 2)



    # вывод

    cv2.imshow('Rezult', img_orig)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
