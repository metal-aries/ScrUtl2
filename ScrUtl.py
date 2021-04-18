from os import path
from PIL import ImageGrab
from PIL import Image
import tkinter
from tkinter import messagebox
import cv2
import numpy

# スクショを取得（書き換え予定）
screenshot = ImageGrab.grab()

# tkinterの背景を削除
root = tkinter.Tk()
root.withdraw()

# 取得した内容が画像であるか？
if isinstance(screenshot, Image.Image):
    cv2.imshow("画像の確認", numpy.asarray(screenshot))

    answer = messagebox.askyesnocancel("画像の保存","aフォルダに保存しますか？")

    if answer == tkinter.YES:
        # パスを指定し画像を保存（書き換え予定）
        imagePath = path.abspath(__file__+"/..")
        screenshot.save(imagePath+"/00.png")
    elif answer == tkinter.NO:
        # パスを指定し画像を保存（書き換え予定）
        imagePath = path.abspath(__file__+"/..")
        screenshot.save(imagePath+"/01.png")
else:
    # 画像でないことを通知
    messagebox.showinfo(title="error", message="NoImage")