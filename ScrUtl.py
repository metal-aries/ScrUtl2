from os import path
from PIL import ImageGrab
from PIL import Image
import tkinter
from tkinter import messagebox
import cv2
import numpy

##### 関数定義 #####
def showImage(x: int, screenshot: Image.Image):
    image = numpy.asarray(screenshot)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    y = int(x * (screenshot.size[1] / screenshot.size[0]))
    image = cv2.resize(image, dsize=(x, y))
    print(y)
    cv2.imshow("thumbnail", image)

##### 本文 #####
# スクショを取得（書き換え予定）
screenshot = ImageGrab.grab()

# tkinterの背景を削除
root = tkinter.Tk()
root.withdraw()

# 取得した内容が画像であるか？
if isinstance(screenshot.copy(), Image.Image):
    # 画像プレビュー
    showImage(320, screenshot)

    # ダイアログ表示
    answer = messagebox.askyesnocancel("画像の保存","aフォルダに保存しますか？")

    if answer == tkinter.YES:
        # パスを指定し画像を保存（書き換え予定）
        imagePath = path.abspath(__file__+"/..")
        screenshot.save(imagePath+"/00.png")
    elif answer == tkinter.NO:
        imagePath = path.abspath(__file__+"/..")
        screenshot.save(imagePath+"/01.png")
else:
    # 画像でないことを通知
    messagebox.showinfo(title="error", message="NoImage")