from array import *
import urllib
import cv2
import numpy as np
import os
from apiclient.discovery import build

neg_dir = 'neg'
urls = []

def search(keyword='face', pageSize=10):
    service = build('customsearch', 'v1',
                   developerKey='AIzaSyBp3hgyJhHb0eqzRSYNl-_a0AHw_EToLBk')

    for i in range(10):
        res = service.cse().list(
            q=keyword,
            cx='006837971229697054245:dwfstyb2fvc',
            searchType='image',
            num=pageSize,
            imgType='clipart',
            fileType='png',
            safe='off',
            start=pageSize*i+1
        ).execute()

        if not 'items' in res:
            print 'No result !!\nres is: {}'.format(res)
        else:
            for item in res['items']:
                # print('=================================================')
                # print(item['title'])
                # print(item['link'])
                urls.append(item['link'])


def download(urls):
    if not os.path.exists(neg_dir):
        os.makedirs(neg_dir)

    pic_num = 1

    for i in urls:
        try:
            print('Downloading => pic {}, {}\n'.format(pic_num, i))
            urllib.urlretrieve(i, neg_dir + '/' + str(pic_num) + '.png')
            img = cv2.imread(neg_dir + '/' + str(pic_num) + '.png', cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite(neg_dir + '/' + str(pic_num) + '.png', resized_image)
            pic_num = pic_num + 1
        except Exception as e:
            print(str(e))

search('trees', 10)
download(urls)