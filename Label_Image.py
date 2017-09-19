# -*- coding:utf-8 -*-

import cv2
import glob
import os

if __name__ == "__main__":
    all_file = glob.iglob(r'../../RAW_PIC/zhenlushaojiu2/*.bmp')
    for bmp in all_file:
      image = cv2.imread(bmp)
      xmin = 2850
      ymin = 750
      xmax = 3350
      ymax = 1250
      image = image[ymin:ymax,xmin:xmax]

      new_name = bmp.replace('.bmp', '_NEW.jpg')
      new_name = new_name.replace(r'../../RAW_PIC/zhenlushaojiu2', r'.')
      image=cv2.resize(image,(600,600))
      print(new_name)

      cv2.imwrite(new_name,image)



    all_file = glob.iglob(r'../../RAW_PIC/zhenlushaojiu2/box/*.bmp')
    for bmp in all_file:
      image = cv2.imread(bmp)
      xmin = 2800
      ymin = 150
      xmax = 3300
      ymax = 650
      image = image[ymin:ymax,xmin:xmax]

      new_name = bmp.replace('.bmp', '_NEW.jpg')
      new_name = new_name.replace(r'../../RAW_PIC/zhenlushaojiu2/box', r'.')
      image=cv2.resize(image,(600,600))
      print(new_name)

      cv2.imwrite(new_name,image)


    i  = 0
    all_file = glob.iglob(r'../../RAW_PIC/zhenlushaojiu2/box/*.bmp')
    for bmp in all_file:
      i = i + 1
      image = cv2.imread(bmp)
      xmin = 2800
      ymin = 0
      xmax = 3300
      ymax = 1000
      image = image[ymin:ymax,xmin:xmax]

      new_name = bmp.replace('.bmp', '_NEW.jpg')
      new_name = new_name.replace(r'../../RAW_PIC/zhenlushaojiu2/box', r'./test')
      image=cv2.resize(image,(600,1000))
      print(new_name)

      cv2.imwrite(new_name,image)

      if i>30:
          break



    all_file = glob.iglob(r'./test/*.jpg')
    for bmp in all_file:
        image = cv2.imread(bmp)
        new_name = bmp.replace('_NEW.jpg', '_NEW_1000.jpg')
        new_name = new_name.replace(r'./test', r'./test1000')
        print(new_name)
        cv2.imwrite(new_name,image)
