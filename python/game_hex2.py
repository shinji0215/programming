import tkinter
import math



#キャンパスに図形を書く
#座標はキャンパス基準
length = 20+20
a = length
b = (length / 2)*math.sqrt(3)
c = length / 2

cx, cy = 50, 50     #(0,0)位置の中心描画座標
def byouga_zahyou(x, y):
    #管理座標->描画座標変換
    dx = cx
    dy = cy
    if x % 2 != 0:      #xが奇数ならy座標をb分ずらす
        dy += b

    dx += (a+c)*x 
    dy += (2*b)*y

    return dx, dy

def hex_disp(x, y):
    global length
    global a, b, c

    #管理座標->描画座標変換
    cx, cy = byouga_zahyou(x, y)

    x1,y1 = cx+c, cy-b
    x2,y2 = cx+a, cy
    x3,y3 = cx+c, cy+b
    x4,y4 = cx-c, cy+b
    x5,y5 = cx-a, cy
    x6,y6 = cx-c, cy-b

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


p_x, p_y = 3, 3         #自分の位置(仮)
def kyori_zahyou(x, y):
    #管理座標->距離座標に変換
    if x % 2 != 0:      #x座標が奇数の場合
        dy = (y*2)+1
    else:
        dy = y*2
    dx = x

    return dx, dy

def distance(s_x, s_y, e_x, e_y):
    #距離計算
    #管理座標を距離座標に変換
    d_x, d_y = kyori_zahyou(e_x, e_y)
    d_p_x, d_p_y = kyori_zahyou(s_x, s_y)

    #距離計算
    d_x2 = abs(d_p_x-d_x)
    d_y2 = abs(d_p_y-d_y)

    if d_y2 < d_x2:
        dis = d_x2
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

    x1,y1 = cx+c, cy-b
    x2,y2 = cx+a, cy
    x3,y3 = cx+c, cy+b
    x4,y4 = cx-c, cy+b
    x5,y5 = cx-a, cy
    x6,y6 = cx-c, cy-b

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

    xtmp, ytmp = byouga_zahyou(p_x, p_y)
    canvas.coords('RZ', xtmp, ytmp)         #キャラ表示
    
    root.after(300, main_proc)




root = tkinter.Tk()                 #オブジェクト生成
root.title('初めてのウィンドウ')        #ウィンドウのタイトル
root.geometry('2400x1200')                #ウィンドウのサイズ

#キャンパス
canvas = tkinter.Canvas(root, width=2400, height=1200, bg='skyblue')
canvas.pack()
#キャラ(image)を表示
img = tkinter.PhotoImage(file='test_red.png')
c_x, c_y = byouga_zahyou(p_x, p_y)
canvas.create_image(c_x, c_y, image=img, tag='RZ')

root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)

#20x20のマスを描く
for y in range(10):
    for x in range(10):
        hex_disp(x, y)              #HEXマップを描画
        distance(p_x, p_y, x, y)    #自分からの距離を計算


main_proc()
root.mainloop()