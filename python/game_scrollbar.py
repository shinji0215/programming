import tkinter as tk

root = tk.Tk()
root.geometry('400x200')

#Canvasを生成
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH)

#Scrollbarを生成して配置
vbar = tk.Scrollbar(root, orient=tk.VERTICAL)
vbar.pack(side=tk.RIGHT, fill=tk.Y)
hbar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
hbar.pack(side=tk.BOTTOM, fill=tk.X)

#Scrollbarの制御をCanvasに通知
vbar.config(command=canvas.yview)
hbar.config(command=canvas.xview)

#Canvasのスクロール範囲を設定
canvas.config(scrollregion=(-200, -100, 400, 400))

#Canvasの可動域をscrollbarに通知
canvas.config(yscrollcommand=vbar.set, xscrollcommand=hbar.set)

#Canvas上に適当な図を書く
id = canvas.create_oval(10, 10, 370, 370)
canvas.itemconfigure(id, fill='red')

root.mainloop()

