from os import path
from PIL import ImageGrab
from PIL import Image
import tkinter
from tkinter import messagebox
from tkinter import filedialog
import cv2
import numpy
import datetime

##### 関数定義 #####
# サムネイルを表示（書き換え予定）
def showImage(x: int, screenshot: Image.Image):
    image = numpy.asarray(screenshot)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    y = int(x * (screenshot.size[1] / screenshot.size[0]))
    image = cv2.resize(image, dsize=(x, y))

    cv2.imshow("thumbnail", image)

# 保存先のパスを生成
def naming(filepath: str):
    date = datetime.datetime.now()
    epifix = 0
    result = filepath + "/" + date.strftime("%y%m%d_%H%M") + "_" + format(epifix) +".png"
    
    while(path.exists(result) == True):
        epifix += 1
        result = filepath + "/" + date.strftime("%y%m%d_%H%M") + "_" + format(epifix) +".png"

    return result

##### 本文 #####
# スクショを取得（書き換え予定）
screenshot = ImageGrab.grabclipboard()
if isinstance(screenshot, Image.Image) != True:
    screenshot = ImageGrab.grab()

# tkinterの背景を削除
root = tkinter.Tk()
root.withdraw()

# 取得した内容が画像であるか？
if isinstance(screenshot, Image.Image):
    # 画像プレビュー
    showImage(320, screenshot.copy())

    # フォルダ選択ダイアログ表示
    directory = filedialog.askdirectory()

    screenshot.save(naming(directory))
else:
    # 画像でないことを通知
    messagebox.showinfo(title="error", message="NoImage")