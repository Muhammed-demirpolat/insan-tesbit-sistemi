# 🧠 İnsan Tespit Sistemi

Gerçek zamanlı insan tespiti! Bu proje, **YOLOv8** ve **OpenCV** kullanarak videolarda, kameradan alınan görüntülerde veya fotoğraflarda insanları hızlı ve doğru bir şekilde tespit eden bir görüntü işleme sistemi sunar.

## 🚀 Özellikler

- **Gerçek zamanlı insan tespiti:** Kamera veya video dosyası üzerinden çalışır.
- **Otomatik işaretleme:** Tespit edilen kişileri belirgin dikdörtgen kutularla gösterir.
- **Hızlı ve optimize algoritma:** Yüksek performans ve düşük gecikme.
- **Kolay genişletilebilirlik:** Sadece insanları değil, başka nesneleri de tespit edecek şekilde kolayca uyarlanabilir.

## 🧩 Gerekli Kütüphaneler

Python ortamınıza aşağıdaki kütüphaneleri yükleyin:

```bash
pip install ultralytics
pip install opencv-python
```

## ⚙️ Gereksinimler

- Python 3.8 veya üzeri
- İnternet bağlantısı (model ilk kez indirileceği zaman gerekli)
- Kamera (gerçek zamanlı test için) veya video dosyası

## 🧠 Kullanılan Teknolojiler

- **YOLOv8 (Ultralytics):** Nesne tespiti için son teknoloji derin öğrenme modeli
- **OpenCV:** Görüntü işleme ve video yönetimi
- **Python:** Projenin ana programlama dili

## 📁 Proje Yapısı

```
insan-tespit-sistemi
│ 
├── main.py               # Ana çalışma dosyası
├── video.mp4             # Test videosu (isteğe bağlı)
├── COCO.names            # sınıflandırma dosyası 
└── README.md             # Proje açıklaması
```

## 🎬 Tanıtım Videosu

Projenin nasıl çalıştığını görmek için [YouTube videosunu izleyin](https://youtu.be/SBviMNmq9ec).

---
Daha fazla bilgi ve katkı için repoyu inceleyebilir, sorularınızı iletebilirsiniz!
