import tkinter as tk
import sys
from tkinter import messagebox
from tokenize import Double


# ボタン押下時の処理
def fnc_click():

    # 税込価格のテキストボックスに値が入っていないかチェックする
    zeikomi_str = calc_resultBox.get()

    # 税込価格ボックスの入力値が税抜価格かどうか判定
    if zeikomi_str != "":
        ret = messagebox.askyesno('確認', '税込価格欄に入力された金額は税抜価格でよろしいですか？')
        # 税込価格=税抜価格の場合:税込価格ボックスの値を税抜価格ボックスにセットする
        # 税込価格≠税抜価格の場合:税込価格ボックスと税抜価格ボックスを初期化する
        if ret == True:
            einuki_str = zeikomi_str
            zeinuki_txtBox.delete(0, tk.END)
            zeinuki_txtBox.insert(0, zeinuki_str)
        else:
            calc_resultBox.delete(0, tk.END)
            zeinuki_txtBox.delete(0, tk.END)
            messagebox.showinfo('メッセージ', '税抜価格を入力して、計算ボタンを押してください。')
    else:
        zeinuki_str = zeinuki_txtBox.get()

    # 計算の前処理を行う
    zeinuki_int = int(zeinuki_str)

    # 消費税を代入
    zei = 1.10

    # 税込計算
    zeikomi_float = zeinuki_int * zei

    # 画面上に表示するために、int型に変換
    zeikomi = int(zeikomi_float)

    # 税込価格のテキストボックスを初期化して、表示
    calc_resultBox.delete(0, tk.END)
    calc_resultBox.insert(0, zeikomi)


# ウィンドウ作成
root = tk.Tk()

# ウィンドウタイトルの設定
root.title("消費税計算")

# ウィンドウ枠の大きさ設定
root.geometry("320x180")

# ラベル名「価格(税抜)」を設定
input_zeinuki_label = tk.Label(root, text="税抜価格", font=("MS ゴシック", 14, "bold"))

# ラベル名「価格(税抜)」の配置
input_zeinuki_label.grid(row=0, column=0, sticky="wens")

# テキストボックスの定義
zeinuki_txtBox = tk.Entry()

# テキストボックスの配置場所定義
zeinuki_txtBox.grid(row=0, column=1, sticky="wens")

# ラベル名「価格(税込)」を設定
output_zeikomi_label = tk.Label(root, text="税込価格", font=("MSゴシック", 14, "bold"))

# ラベル名「価格(税込)」の配置場所定義
output_zeikomi_label.grid(row=1, column=0, sticky="wens")

# 計算ボタン定義
calc_button = tk.Button(root, text="計算", command=fnc_click)

# 計算ボタン配置場所定義
calc_button.grid(row=2, column=0, sticky="wens")

# ラベル名「価格(税込)」の計算結果を表示
calc_resultBox = tk.Entry()

# 計算結果の配置場所を設定
calc_resultBox.grid(row=1, column=1, sticky="wens")

# ウィンドウを表示し続ける
root.mainloop()
