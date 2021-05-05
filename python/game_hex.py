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

cx, cy = 50, 50     #(0,0)位置の中心描画座標
def byouga_zahyou(x, y):
    #管理座標->描画座標変換
    dx = cx
    dy = cy
    if y % 2 != 0:      #奇数ならx座標をb分ずらす
        dx += b
    dx += 2*b*x 

    dy += (length+c)*y

    return dx, dy

def hex_disp(x, y):
    global length
    global a, b, c

    #管理座標->描画座標変換
    cx, cy = byouga_zahyou(x, y)

    x1,y1 = cx, cy-a
    x2,y2 = cx+b, cy-c
    x3,y3 = cx+b, cy+c
    x4,y4 = cx, cy+a
    x5,y5 = cx-b, cy+c
    x6,y6 = cx-b, cy-c

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
    
    #ラベル（デバッグ用)
    dx, dy = byouga_zahyou(e_x, e_y)
    label = tkinter.Label(root, text='{:.0f}'.format(dis), font=('System', 8))
    label.place(x=dx, y=dy)

    return dis

rect1,rect2,rect3,rect4,rect5,rect6 = '','','','','',''
def hex_disp2(x, y):
    global length
    global a, b, c
    global rect1,rect2,rect3,rect4,rect5,rect6

    #前回のline描画を消す
    if rect1 != '':
        canvas.delete(rect1)
        canvas.delete(rect2)
        canvas.delete(rect3)
        canvas.delete(rect4)
        canvas.delete(rect5)
        canvas.delete(rect6)

    #管理座標->描画座標変換
    cx, cy = byouga_zahyou(x, y)

    x1,y1 = cx, cy-a
    x2,y2 = cx+b, cy-c
    x3,y3 = cx+b, cy+c
    x4,y4 = cx, cy+a
    x5,y5 = cx-b, cy+c
    x6,y6 = cx-b, cy-c

     #位置1->2
    rect1 = canvas.create_line(x1, y1, x2, y2, fill='red', width=3)
    #位置2->3
    rect2 = canvas.create_line(x2, y2, x3, y3, fill='red', width=3)
    #位置3->4
    rect3 = canvas.create_line(x3, y3, x4, y4, fill='red', width=3)
    #位置4->5
    rect4 = canvas.create_line(x4, y4, x5, y5, fill='red', width=3)
    #位置5->6
    rect5 = canvas.create_line(x5, y5, x6, y6, fill='red', width=3)
    #位置6->1
    rect6 = canvas.create_line(x6, y6, x1, y1, fill='red', width=3)



#20x20のマスを描く

for y in range(20):
    for x in range(20):
        hex_disp(x, y)              #HEXマップを描画
        distance(p_x, p_y, x, y)    #自分からの距離を計算

#hex_disp2(p_x, p_y)
key = ''
def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global key
    key = ''

def main_proc():
    #global key
    global p_x, p_y
    hex_disp(p_x, p_y)          #カーソルを消す

    if key == 'Up':
        p_y = p_y-1
    if key == 'Down':
        p_y = p_y+1    
    if key == 'Left':
        p_x = p_x-1
    if key == 'Right':
        p_x = p_x+1
    
    hex_disp2(p_x, p_y)         #カーソル表示
    root.after(300, main_proc)

root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)
main_proc()
root.mainloop()