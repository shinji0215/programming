import tkinter


def click_btn():
    txt = entry.get()          #テキスト入力の文字取得
    button['text'] = txt


root = tkinter.Tk()                 #オブジェクト生成
root.title('初めてのウィンドウ')        #ウィンドウのタイトル
root.geometry('800x600')                #ウィンドウのサイズ

#キャンパス
canvas = tkinter.Canvas(root, width=400, height=600, bg='skyblue')
canvas.pack()

#ラベル
label = tkinter.Label(root, text='ラベルの文字列', font=('System', 24))
label.place(x=100, y=100)

#ボタン
button = tkinter.Button(root, text='ボタンの文字列', font=('Times New Roman', 24), command=click_btn)
button.place(x=100, y=200)

#キャンパスに図形を書く
#座標はキャンパス基準
#文字列
canvas.create_text(50, 300, text='文字列', fill='green', font=('Times New Roman', 12))
#ライン
canvas.create_line(30, 330, 70, 380, fill='navy', width=5)
#矩形
canvas.create_rectangle(40, 390, 160, 400, fill='lime')
#楕円 create_oval(x1, y1, x2, y2, fill=塗り色,outline=枠線の色, width=枠線の太さ)
canvas.create_oval(250-80, 200-40, 250+40, 100+40, fill='pink', outline='purple')

#テキスト入力 Entry()
entry = tkinter.Entry(width=20)         #半角20文字分
entry.place(x=10, y=10)


root.mainloop()