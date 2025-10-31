from ultralytics import YOLO
import cv2

# Modeli indir (önceden eğitilmiş COCO)
model = YOLO("yolov8n.pt")  # küçük model, hızlı

cap = cv2.VideoCapture("video.mp4")

# Pencereyi tam ekran yap (video bende yanlış acıldığı için tam ekran yaptım bu kısım olmadan da çalışır)
cv2.namedWindow("insan Tespiti", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("insan Tespiti", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Ekran çözünürlüğü (monitörüne göre değiştirebilirsin)
screen_res = 1920, 1080

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # İnsanları tespit et
    results = model(frame)
    person_count = 0

    for r in results:
        boxes = r.boxes.xyxy.cpu().numpy()  # kutular
        class_ids = r.boxes.cls.cpu().numpy()  # sınıf id
        for i, cls in enumerate(class_ids):
            if int(cls) == 0:  # COCO'da 0 = person (sadece insan olanları kutuluyoruz)
                person_count += 1
                x1, y1, x2, y2 = map(int, boxes[i])  
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2) #kutuların cevresini yeşile boyadık

    cv2.putText(frame, f"insan Sayisi: {person_count}", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Tam ekran göstermek için ölçekle
    scale_width = screen_res[0] / frame.shape[1]
    scale_height = screen_res[1] / frame.shape[0]
    scale = min(scale_width, scale_height)
    window_width = int(frame.shape[1] * scale)
    window_height = int(frame.shape[0] * scale)
    frame_resized = cv2.resize(frame, (window_width, window_height))

    cv2.imshow("insan Tespiti", frame_resized)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC ile çık
        break

cap.release()
cv2.destroyAllWindows()
