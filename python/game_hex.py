import tkinter
import math




root = tkinter.Tk()                 #オブジェクト生成
root.title('初めてのウィンドウ')        #ウィンドウのタイトル
root.geometry('800x800')                #ウィンドウのサイズ

#キャンパス
canvas = tkinter.Canvas(root, width=800, height=800, bg='skyblue')
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

p_x, p_y = 10, 10         #自分の位置(仮)
def kyori_zahyou(x, y):
    #管理座標->距離座標に変換
    if y % 2 != 0:      #y座標が奇数の場合
        dx = (x*2)+1
    else:
        dx = x*2
    dy = y

    return dx, dy

def distance(s_x, s_y, e_x, e_y):
    #距離計算
    #管理座標を距離座標に変換
    d_x, d_y = kyori_zahyou(e_x, e_y)
    d_p_x, d_p_y = kyori_zahyou(s_x, s_y)

    #距離計算
    d_x2 = abs(d_p_x-d_x)
    d_y2 = abs(d_p_y-d_y)

    if d_y2 > d_x2:
        dis = d_y2
    else :
        dis = (d_x2+d_y2)/2
    
    #ラベル
    label = tkinter.Label(root, text='{:.0f}'.format(dis), font=('System', 8))
    label.place(x=dx, y=dy)

    return dis


#20x20のマスを描く
cx, cy = 50, 50

dy = cy
for y in range(20):
    dx = cx
    if y % 2 != 0:      #奇数ならx座標をb分ずらす
        dx += b

    for x in range(20):
        hex_disp(dx, dy)
        distance(p_x, p_y, x, y)
        dx += 2*b 

    dy += length+c



root.mainloop()