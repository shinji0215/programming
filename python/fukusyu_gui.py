import tkinter


def click_btn():
    button['text'] = 'クリックしました'


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

root.mainloop()