import tkinter

root = tkinter.Tk()                 #オブジェクト生成
root.title('初めてのウィンドウ')        #ウィンドウのタイトル
root.geometry('800x600')                #ウィンドウのサイズ

label = tkinter.Label(root, text='ラベルの文字列', font=('System', 24))
label.place(x=200, y=100)


root.mainloop()