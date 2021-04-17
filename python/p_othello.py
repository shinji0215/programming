

f_pass = False   #パス実行有無


NONE = 0
BLACK = 1
WHITE = 2
ban = [
    [0, 0, 0, 0, 0, 0, 0,0 ], 
    [0, 0, 0, 0, 0, 0, 0,0 ], 
    [0, 0, 0, 0, 0, 0, 0,0 ], 
    [0, 0, 0, 2, 1, 0, 0,0 ], 
    [0, 0, 0, 1, 2, 0, 0,0 ], 
    [0, 0, 0, 0, 0, 0, 0,0 ], 
    [0, 0, 0, 0, 0, 0, 0,0 ], 
    [0, 0, 0, 0, 0, 0, 0,0 ]
]


chk_ban = [
    [0, 0, 0, 0, 0, 0, 0,0 ], 
    [0, 0, 0, 0, 0, 0, 0,0 ], 
    [0, 0, 0, 0, 0, 0, 0,0 ], 
    [0, 0, 0, 0, 0, 0, 0,0 ], 
    [0, 0, 0, 0, 0, 0, 0,0 ], 
    [0, 0, 0, 0, 0, 0, 0,0 ], 
    [0, 0, 0, 0, 0, 0, 0,0 ], 
    [0, 0, 0, 0, 0, 0, 0,0 ]
]

def checkBan(x, y, now_koma):
    """駒が置けるか？"""
    #引数 x,y 位置

    num = 0         #返す数
    #チェック用リスト   l_chk[][]
    #全方向の駒をチェックするためのオフセット値
    l_chk = [
        #y, x
        [ 1,  0],        #上
        [ 1, -1],        #右上
        [ 0,  1],        #右
        [-1,  1],        #右下
        [-1,  0],        #下
        [-1, -1],        #左下
        [ 0, -1],        #左
        [ 1, -1],        #左上
    ]   


    #既に駒が置いてあるか？
    #置いてあれば、返せる数は0
    if ban[y][x] != NONE:
        #print('すでに駒がある')
        return 0 

    #盤の最後までチェックしたか？
    #全方位の盤の端までチェックする
    for brg in range(8):
        #print(f'brg={brg}')
        ix = x + l_chk[brg][1]
        iy = y + l_chk[brg][0]
        tmp = 0         #相手の駒の数。自分の駒があれば返せる駒の数

        while (-1 < ix < 8) and (-1 < iy < 8):
            #駒の種類確認
            if ban[iy][ix] == NONE:
                #print('駒がない')
                break

            elif ban[iy][ix] == now_koma:
                #print('自分の駒')
                #すでに相手の駒があれば返し確定
                num += tmp
                break

            else:
                #print('相手の駒')
                tmp += 1


            #次のマスへ
            ix += l_chk[brg][1]
            iy += l_chk[brg][0]

    #print(f'返せる数={num}')
    return num
    #



def display(ban):
    """盤面を表示する"""
    for y in range(8):
        print(f"{y+1}", end='')
        for x in range(8):
            if ban[y][x] == NONE:
                print('_', end='')
            elif ban[y][x] == BLACK:
                print('O', end='')
            elif ban[y][x] == WHITE:
                print('+', end='')
            else:
                pass   #何もしない
        print("")

#盤表示(デバッグ用)
def disp_ban(ban):
    """盤面を表示する"""
    for y in range(8):
        print(f"{y+1}", end='-')
        for x in range(8):
            #print(ban[y][x].format(), end=',')
            print('{:>2d}'.format(ban[y][x]), end=',') 
        print("")


def othello_loop():
    global f_pass

    now_koma = BLACK            #現在の順番(最初は黒から)
    while True:
        #駒が置けるかすべてのマスを判定する
        for y in range(8):
            for x in range(8):
                chk_ban[y][x] = checkBan(x, y, now_koma)

                #ひっくり返せるマスがあるならパスは無し
                if chk_ban[y][x] != 0:
                    f_pass = False
        
        #disp_ban(chk_ban)

        #置ける場所がないならパス
        if f_pass == True:
            print("passする")
            continue

    
        # 駒を置く位置を入力する
        x, y = map(int, input("駒を置いてください.(x y):").split())  #mapで数字に変換
        print(f"{x} {y}")

        # 駒が置けるか判定
        #ret = checkBan(x-1, y-1)
        if chk_ban[y-1][x-1] > 0:
            #print('駒が置ける')

            # 駒をひっくり返す
            ban[y-1][x-1] = now_koma
        
        else :
            #置けなければやり直し
            print('置けません')
            continue
            

        #盤面表示更新
        display(ban)

        #ゲーム終了判定

        #終了でなければ次プレーヤに移行
        if now_koma == BLACK:
            now_koma = WHITE
        else:
            now_koma = BLACK
        


    #結果発表

#
#メイン
#
#オセロ盤表示
display(ban)

#ゲーム開始
othello_loop()





