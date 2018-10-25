# encoding:utf-8

import cv2
import numpy as np

width = 400
height = 300

# uint8で0埋めの配列を作る。
# 幅16、高さ24のサイズ
# zeros(shape, type) shapeは配列の大きさ
# 配列の（行数、列数）になっている
# 画像はwidth,heightの慣習があるが、ココは逆なので気をつけること
imageArray = np.zeros((height, width, 3), np.uint8)

# これでサイズを確認できます
'''
size = imageArray.shape[:2]
print(size)
'''

text = "J M"
number = "12"

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imageArray,text,(140,100),font, 2,(255,255,255),5)
cv2.putText(imageArray,number,(160,200),font, 2,(255,255,255),5)
# 0で埋められた配列を画像として保存します
cv2.imwrite("blank.bmp", imageArray);

# ここに
# for h in range(0, height):
# 	for w in range(0, width):
# 		imageArray[h, w] = [128, 64, 32]

# これでimageArrayの中身を表示できる
# '''
# print(imageArray)
# '''

# cv2.imwrite("R32_G64_B128_16x24.bmp", imageArray)
