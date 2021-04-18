from os import path
from PIL import ImageGrab
from PIL import Image
import tkinter
from tkinter import messagebox

# スクショを取得（書き換え予定）
screenshot = ImageGrab.grabclipboard()

# 取得した内容が画像であるか？
if isinstance(screenshot, Image.Image):
    # パスを指定し画像を保存（書き換え予定）
    imagePath = path.abspath(__file__+"/..")
    screenshot.save(imagePath+"/00.png")
else:
    # 画像でないことを通知
    root = tkinter.Tk()
    root.withdraw() # tkinterの背景を削除

    messagebox.showinfo(title="error", message="NoImage")