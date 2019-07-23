import requests
import cv2
import numpy as np
import os

imageList = [
        "https://w.wallhaven.cc/full/mp/wallhaven-mpe271.jpg",
        "https://w.wallhaven.cc/full/zx/wallhaven-zx1qoo.jpg",
        "https://w.wallhaven.cc/full/mp/wallhaven-mp5668.jpg",
        "https://w.wallhaven.cc/full/vm/wallhaven-vmogqm.jpg",
        "https://w.wallhaven.cc/full/r7/wallhaven-r7q9gj.jpg",
        "https://w.wallhaven.cc/full/6q/wallhaven-6qoodl.jpg",
        ]

picNum = 1
for ind, link in enumerate(imageList):
    try:
        response = requests.get(link)
        with open('./largeNegs/' + str(ind) + '.jpg', 'wb') as f:
            f.write(response.content)
        img = cv2.imread('largeNegs/' + str(ind) + '.jpg', cv2.IMREAD_GRAYSCALE)
        for r in range(img.shape[0] // 100):
            for c in range(img.shape[1] // 100):
                x = r * 100
                y = c * 100
                cv2.imwrite('neg/' + str(picNum) + '.jpg', img[x:x + 100, y:y + 100])
                picNum += 1
    except Exception as e:
        print(str(e))

for ind in range(1, picNum):
    size = os.path.getsize('neg/' + str(ind) + '.jpg')
    if size < 2000:
        os.remove('neg/' + str(ind) + '.jpg')
