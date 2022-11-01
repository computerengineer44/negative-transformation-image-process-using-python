import cv2
import matplotlib.pyplot as plt

# Resim okuma
img_bgr = cv2.imread('fenerbahce.jfif', 1)
plt.imshow(img_bgr)
plt.show()

#  Resmin histogram çizimi
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histr = cv2.calcHist([img_bgr],
                         [i], None,
                         [256],
                         [0, 256])

    plt.plot(histr, color=col)


    plt.xlim([0, 256])

plt.show()

# görüntünün yüksekliğini ve genişliğini al
height, width, _ = img_bgr.shape

for i in range(0, height - 1):
    for j in range(0, width - 1):
        # piksel değerini al
        pixel = img_bgr[i, j]

        # 1. dizin kırmızı piksel içeriyor
        pixel[0] = 255 - pixel[0]

        # 2.dizin yeşil piksel içeriyor
        pixel[1] = 255 - pixel[1]

        # 3.dizin mavi piksel içeriyor
        pixel[2] = 255 - pixel[2]

        # Yeni değerleri pikselde saklayın
        img_bgr[i, j] = pixel

# Negatif dönüştürülmüş görüntüyü göster
plt.imshow(img_bgr)
plt.show()

# Histogram çizimi negatif dönüştürülmüş görüntü
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histr = cv2.calcHist([img_bgr],
                         [i], None,
                         [256],
                         [0, 256])

    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.show()
