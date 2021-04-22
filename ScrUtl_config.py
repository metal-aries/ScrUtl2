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

    directory = filedialog.askdirectory(title="初期ディレクトリの設定")
    if len(directory) != 0:
        config_data2 = open(config_path, "w", encoding="utf-8")
        config_dict["ini_dir"] = directory
        json.dump(config_dict, config_data2)
        config_data2.close()

def display_help():
    print("ScrUtl2")
    print("")
    print("概要")
    print("　ショートカットキーでスクショを撮るアプリです。")
    print("")
    print("使い方")
    print("　.batアプリをショートカットキーに指定して起動すると、現在のスクリーンを画像として出力します。")
    print("　このとき、サムネイルとフォルダ選択ダイアログが表示されます。")
    print("　画像は、選択したフォルダ下にyymmddyymm_xx.pngの形で保存されます。xxは、1分以内にスクショを複数回取った時のための対策です。")
    print("")
    print("コマンドライン引数")
    print("　-cのコマンドライン引数で、コンフィグモードを起動します。")
    print("　コンフィグモードは、ScrUtl_config.pyがScrUtl.pyと同じディレクトリ上に存在している場合のみ起動します。")
    print("　現在は、スクショ保存時の初期ディレクトリの変更機能だけが実装されています。")
    print("")
    print("　-hのコマンドライン引数で、説明を表示します。")
    print("")
    print("動作環境・操作方法")
    print("　pythonを実行できる環境下で動きます。")
    print("　ScrUtl.py、ScrUtl.batを最低限ダウンロードしてください。")
    print("　ScrUtl_config.pyは、コンフィグモードを起動したいときにダウンロードしてください。")
    print("　コンフィグモードを起動したとき、ScrUtl.config.jsonが自動生成されます。")
