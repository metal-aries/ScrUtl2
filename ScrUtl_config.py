from os import path

import tkinter
from tkinter import filedialog

import json

def set_ini_dir():
    # 設定ファイルの存在確認
    config_path = __file__+"/../ScrUtl.config.json"
    if path.isfile(config_path):
        config_data = open(config_path, encoding="utf-8")
        config_dict = json.load(config_data)
        config_data.close()
    else:
        config_dict = {}

    directory = filedialog.askdirectory()
    if len(directory) != 0:
        config_data2 = open(config_path, "w", encoding="utf-8")
        config_dict["ini_dir"] = directory
        json.dump(config_dict, config_data2)
        config_data2.close()
