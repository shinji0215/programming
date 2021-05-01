import tkinter
import math




root = tkinter.Tk()                 #オブジェクト生成
root.title('初めてのウィンドウ')        #ウィンドウのタイトル
root.geometry('800x600')                #ウィンドウのサイズ

#キャンパス
canvas = tkinter.Canvas(root, width=800, height=600, bg='skyblue')
canvas.pack()



#キャンパスに図形を書く
#座標はキャンパス基準
length = 20
a = length
b = (length / 2)*math.sqrt(3)
c = length / 2

def hex_disp(x, y):
    global length
    global a, b, c

    x1,y1 = x, y-a
    x2,y2 = x+b, y-c
    x3,y3 = x+b, y+c
    x4,y4 = x, y+a
    x5,y5 = x-b, y+c
    x6,y6 = x-b, y-c

    #位置1
    #canvas.create_line(x, y, x1, y1, fill='navy', width=1)
    #位置2
    #canvas.create_line(x, y, x2, y2, fill='navy', width=1)
    #位置3
    #canvas.create_line(x, y, x3, y3, fill='navy', width=1)
    #位置4
    #canvas.create_line(x, y, x4, y4, fill='navy', width=1)
    #位置5
    #canvas.create_line(x, y, x5, y5, fill='navy', width=1)
    #位置6
    #canvas.create_line(x, y, x6, y6, fill='navy', width=1)

    #位置1->2
    canvas.create_line(x1, y1, x2, y2, fill='navy', width=1)
    #位置2->3
    canvas.create_line(x2, y2, x3, y3, fill='navy', width=1)
    #位置3->4
    canvas.create_line(x3, y3, x4, y4, fill='navy', width=1)
    #位置4->5
    canvas.create_line(x4, y4, x5, y5, fill='navy', width=1)
    #位置5->6
    canvas.create_line(x5, y5, x6, y6, fill='navy', width=1)
    #位置6->1
    canvas.create_line(x6, y6, x1, y1, fill='navy', width=1)

x, y = 200, 200
hex_disp(x, y)
hex_disp(x+b, y+a+c)
hex_disp(x-b, y+a+c)
hex_disp(x-(2*b), y)
hex_disp(x-b, y-(a+c))
hex_disp(x+b, y-(a+c))
hex_disp(x+(2*b), y)

root.mainloop()