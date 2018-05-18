import urllib
import cv2 as cv
import numpy as np
import os

def pull_images():
    neg_images_link = 'https://www.google.com.hk/search?hl=en&biw=1863&bih=990&tbm=isch&sa=1&ei=nG_6Wue3BYL-8QXHwL6ICQ&q=life&oq=life&gs_l=img.3..0l10.2768.3880.0.4000.5.5.0.0.0.0.107.389.2j2.4.0....0...1c.1.64.img..1.4.388.0..35i39k1j0i67k1.0.MoOGbEMrbvw'
    neg_image_urls = urllib.urlopen(neg_images_link).read()
    img_num = 1

    if not os.path.exists('neg'):
        os.makedirs('neg')

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.urlretrieve(i, "neg/"+str(img_num)+".jpg")
            img = cv2.imread("neg/" + str(pic_num) + ".jpg", cv.IMREAD_GRAYSCALE)
            resized_image = cv.resize(img, (100, 100))
            cv2.imwrite("neg/" + str(img_num) + ".jpg", resized_image)
            img_num += 1
        except Exception as e:
            print(str(e))

pull_images()