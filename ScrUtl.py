import sys
from os import path

from PIL import ImageGrab
from PIL import Image

import tkinter
from tkinter import messagebox
from tkinter import filedialog

import cv2
import numpy

import datetime

import json

config_exists = False
if path.isfile(path.abspath(__file__ +"/.." "/ScrUtl_config.py")):
    import ScrUtl_config
    config_exists = True

##### 関数定義 #####
# サムネイルを表示（書き換え予定）
def show_image(x: int, input_image: Image.Image):
    image = numpy.asarray(input_image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    y = int(x * (input_image.size[1] / input_image.size[0]))
    image = cv2.resize(image, dsize=(x, y))

    cv2.imshow("thumbnail", image)

# スクショを取得（書き換え予定）
def screenshot():
    image = ImageGrab.grabclipboard()
    if isinstance(image, Image.Image) != True:
        image = ImageGrab.grab()

    return image

# フォルダ選択
def select_dir():
    # 設定ファイルの存在確認
    config_path = __file__+"/../ScrUtl.config.json"
    if path.isfile(config_path):

        # 初期ディレクトリの読み込み
        config_data = open(config_path, encoding="utf-8")
        ini_dict = json.load(config_data)
        
        if "ini_dir" in ini_dict and path.isdir(ini_dict["ini_dir"]):
            # 初期ディレクトリを指定してのフォルダ選択
            directory = filedialog.askdirectory(initialdir=ini_dict["ini_dir"])
        else:
            directory = filedialog.askdirectory()

    else:
        directory = filedialog.askdirectory()

    config_data.close()
    return directory

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

# 前処理、tkinterの背景を削除
root = tkinter.Tk()
root.withdraw()

# コマンドライン引数処理
if config_exists == True and len(sys.argv) > 1:
    for arg in sys.argv:
        if arg == "-c" or arg == "--config":
            ScrUtl_config.set_ini_dir()
        if arg == "-h" or arg == "--help":
            ScrUtl_config.display_help()
    sys.exit()

# スクショを取得
image = screenshot()

# 取得した内容が画像であるか？
if isinstance(image, Image.Image):
    # 画像プレビュー
    show_image(320, image.copy())

    # フォルダ選択
    directory = select_dir()

    if len(directory) != 0:
        image.save(naming(directory))
else:
    # 画像でないことを通知
    messagebox.showinfo(title="error", message="NoImage")