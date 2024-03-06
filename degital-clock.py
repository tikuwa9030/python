import tkinter as tk
import datetime as dt


# def clock():
# 曜日のリスト
def clock():
    weeklist = {0: "月曜日", 1: "火曜日", 2: "水曜日",
                3: "木曜日", 4: "金曜日", 5: "土曜日", 6: "日曜日"}

    now = dt.datetime.now()
    week1 = now.weekday()

    for i in weeklist:
        if week1 == i:
            week2 = weeklist[i]
            d = ('{0:%Y}年{0:%m}月{0:%d}日'.format(now) + " " + week2)
            t = ('{0:%p} {0:%I}時{0:%M}分{0:%S}秒'.format(now))

    label1['text'] = d
    label2['text'] = t
    
    root.after(100, clock)


# ウィンドウを画面表示する
root = tk.Tk()

root.title("デジタル時計")

label1 = tk.Label(root, font=("MSゴシック", "20", "bold"))
label2 = tk.Label(root, font=("MSゴシック", "20", "bold"))

label1.pack()
label2.pack()

# datetimeで現在時刻を取得
clock()

# ウインドウを出力し続ける
root.mainloop()
