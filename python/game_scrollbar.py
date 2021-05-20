import tkinter as tk

root = tk.Tk()
root.geometry('400x300')

#Canvasを生成
canvas = tk.Canvas(root, bg='white')
canvas.place(x=0, y=0, width=200, height=300)

#Scrollbarを生成して配置
vbar = tk.Scrollbar(canvas, orient=tk.VERTICAL)
vbar.pack(side=tk.RIGHT, fill=tk.Y)
hbar = tk.Scrollbar(canvas, orient=tk.HORIZONTAL)
hbar.pack(side=tk.BOTTOM, fill=tk.X)

#Scrollbarの制御をCanvasに通知
vbar.config(command=canvas.yview)
hbar.config(command=canvas.xview)

#Canvasのスクロール範囲を設定
canvas.config(scrollregion=(0, 0, 300, 500))

#Canvasの可動域をscrollbarに通知
canvas.config(yscrollcommand=vbar.set, xscrollcommand=hbar.set)

#Canvas上に適当な図を書く
#id = canvas.create_oval(10, 10, 370, 370)
#canvas.itemconfigure(id, fill='red')
canvas.create_rectangle(10, 10, 100, 100, fill='green')

root.mainloop()

