import tkinter
import math
from tkinter import scrolledtext        #スクロールバー付きテキストエリア

#キャンパスに図形を書く
#座標はキャンパス基準
length = 20
a = length
b = (length / 2)*math.sqrt(3)
c = length / 2

cx, cy = 30, 30     #(0,0)位置の中心描画座標
MAP_X_MAX = 52
MAP_Y_MAX = 30

cursor_x, cursor_y = 0, 0       #カーソル位置（管理座標)
unit_x, unit_y = 10, 10         #ユニットAの位置(仮)(管理座標)
unit_angle = 0                  #ユニットAの向き

def byouga_zahyou(x, y):
    #管理座標->描画座標変換
    dx = cx
    dy = cy
    if x % 2 != 0:      #xが奇数ならy座標をb分ずらす
        dy += b

    dx += (a+c)*x 
    dy += (2*b)*y

    return dx, dy

def draw_hex(x, y):
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
    canvas.create_text(dx, dy, text='{:.0f}'.format(dis), font=('System', 6))

    return dis

rect1,rect2,rect3,rect4,rect5,rect6 = '','','','','',''
def draw_cursor(x, y):
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

    #カーソル位置(管理座標)表示
    lbl_cur_pos['text'] = f'cursor: x={cursor_x} y={cursor_y}'
    lbl_cur_pos.update()

def draw_unit(x, y, ang):
    #ユニット(仮)表示
    canvas.delete('RZ')
    xtmp, ytmp = byouga_zahyou(x, y)
    canvas.create_image(xtmp, ytmp, image=img_unit[ang], tag='RZ')


key = ''
def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global key
    key = ''

def main_proc():
    #global key
    global cursor_x, cursor_y

    if key == 'Up':
        cursor_y -= 1
    if key == 'Down':
        cursor_y += 1    
    if key == 'Left':
        cursor_x -= 1
    if key == 'Right':
        cursor_x += 1
    
    if cursor_x >= MAP_X_MAX:
        cursor_x = MAP_X_MAX-1
    if cursor_x < 0:
        cursor_x = 0
    if cursor_y >= MAP_Y_MAX:
        cursor_y = MAP_Y_MAX-1
    if cursor_y < 0:
        cursor_y = 0    

    draw_cursor(cursor_x, cursor_y)         #カーソル表示

    root.after(300, main_proc)

#方向変換
def click_angle():
    global unit_angle
    unit_angle += 1
    if unit_angle > 5:
        unit_angle = 0

    draw_unit(unit_x, unit_y, unit_angle)       #ユニット表示

    #デバッグ文
    text_area.insert(tkinter.END, f'方向変換[{unit_angle}]\n')
    text_area.see('end')    #最終行にスクロールする


#直進
def click_go():
    global unit_x
    global unit_y

    x = unit_x
    y = unit_y

    valid = 1
    if unit_angle == 0:
        y -= 1
    elif unit_angle == 1:
        if x % 2 == 0:  #x軸が偶数の場合
            y -= 1
        x += 1
    elif unit_angle == 2:
        if x % 2 != 0:  #x軸が奇数の場合
            y += 1
        x += 1
    elif unit_angle == 3:
        y += 1            
    elif unit_angle == 4:
        if x % 2 != 0:  #x軸が奇数の場合
            y += 1
        x -= 1
    elif unit_angle == 5:
        if x % 2 == 0:  #x軸が偶数の場合
            y -= 1
        x -= 1

    #範囲外の場合は無効
    if 0 > x or MAP_X_MAX <= x:
        valid = 0
    if 0 > y or MAP_Y_MAX <= y:
        valid = 0  

    if valid == 1:
        unit_x = x
        unit_y = y
        draw_unit(unit_x, unit_y, unit_angle)       #ユニット表示
        #デバッグ文
        text_area.insert(tkinter.END, f'move x={unit_x} y={unit_y}\n')
        text_area.see('end')    #最終行にスクロールする      
    else:
        #デバッグ文
        text_area.insert(tkinter.END, f'移動不可！ x={unit_x} y={unit_y}\n')
        text_area.see('end')    #最終行にスクロールする       

root = tkinter.Tk()                 #オブジェクト生成
root.title('初めてのウィンドウ')        #ウィンドウのタイトル
root.geometry('1900x1200')                #ウィンドウのサイズ
root.title('NEW TYPE ver0.1')

#進行状況表示エリア
frame_info = tkinter.Frame(root, bg='green')
frame_info.place(x=0, y=0, width=1900, height=50)
#カーソル位置表示
lbl_cur_pos = tkinter.Label(frame_info, text=f'cursor: x={cursor_x} y={cursor_y}', bg='gray')
lbl_cur_pos.place(x=0, y=0, width=100, height=20)

#マップエリア
canvas = tkinter.Canvas(root, bg='skyblue')
canvas.place(x=0, y=50, width=1600, height=1080)

#状況表示エリア
text_area = scrolledtext.ScrolledText(root, wrap=tkinter.WORD)
text_area.place(x=0, y=50+1080, width=1600, height=(1200-(50+1080)))
text_area.insert(tkinter.END, 'AABBCC\n')

#ステータス表示エリア
frame_status = tkinter.Frame(root, bg='gray', relief='groove', bd=5)
frame_status.place(x=1600, y=0, width=300, height=800)

#操作エリア
frame_ctrl = tkinter.Frame(root, bg='azure', relief='raised', bd=5)
frame_ctrl.place(x=1600, y=800, width=300, height=400)
#方向変更ボタン
button = tkinter.Button(frame_ctrl, text='方向変更', command=click_angle)
button.place(x=20, y=20, width=80, height=40)
#直進ボタン
btn_go = tkinter.Button(frame_ctrl, text='直進', command=click_go)
btn_go.place(x=20, y=70, width=80, height=40)

#マップ上にキャラ(image)を表示
img_unit = [
    tkinter.PhotoImage(file='test_red.png'),        # 
    tkinter.PhotoImage(file='test_red-ne.png'),     #
    tkinter.PhotoImage(file='test_red-se.png'),
    tkinter.PhotoImage(file='test_red-s.png'),
    tkinter.PhotoImage(file='test_red-sw.png'),
    tkinter.PhotoImage(file='test_red-nw.png')
]
draw_unit(unit_x, unit_y, unit_angle)           #ユニット表示

root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)

#52x30のマスを描く
for y in range(MAP_Y_MAX):
    for x in range(MAP_X_MAX):
        draw_hex(x, y)              #HEXマップを描画
        distance(unit_x, unit_y, x, y)    #自分からの距離を計算


main_proc()
root.mainloop()