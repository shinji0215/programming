

f_pass = False   #パス実行有無


NONE = 0
BLACK = 1
WHITE = 2
now_koma = BLACK            #現在の順番(最初は黒から)
pass_status = None          #誰もパスはしていない

ban = [
    [0, 0, 0, 0, 0, 0, 0, 0 ], 
    [0, 0, 0, 0, 0, 0, 0, 0 ], 
    [0, 0, 0, 0, 0, 0, 0, 0 ], 
    [0, 0, 0, 2, 1, 0, 0, 0 ], 
    [0, 0, 0, 1, 2, 0, 0, 0 ], 
    [0, 0, 0, 0, 0, 0, 0, 0 ], 
    [0, 0, 0, 0, 0, 0, 0, 0 ], 
    [0, 0, 0, 0, 0, 0, 0, 0 ]
]


chk_ban = [
    [0, 0, 0, 0, 0, 0, 0, 0 ], 
    [0, 0, 0, 0, 0, 0, 0, 0 ], 
    [0, 0, 0, 0, 0, 0, 0, 0 ], 
    [0, 0, 0, 0, 0, 0, 0, 0 ], 
    [0, 0, 0, 0, 0, 0, 0, 0 ], 
    [0, 0, 0, 0, 0, 0, 0, 0 ], 
    [0, 0, 0, 0, 0, 0, 0, 0 ], 
    [0, 0, 0, 0, 0, 0, 0, 0 ]
]

def checkBan(x, y, now_koma, exe=False):
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

                if((exe == True) and (tmp != 0)):
                    #ひっくり返し実行
                    ix2 = ix
                    iy2 = iy

                    #駒を置いた座標まで戻りながら駒を返す
                    while (iy2 != y) or (ix2 != x):
                        ix2 = ix2 - l_chk[brg][1]
                        iy2 = iy2 - l_chk[brg][0]
                        ban[iy2][ix2] = now_koma
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

def koma_status():
    blk_num = 0
    whi_num = 0
    for i in range(8):
        blk_num += ban[i].count(BLACK)
        whi_num += ban[i].count(WHITE)

    return blk_num, whi_num


def display(ban):
    """盤面を表示する"""
    print('*****************')
    blk_num, whi_num = koma_status()
    print('BLACK={0} WHITE={1}'.format(blk_num, whi_num))

    if(now_koma == BLACK):
        print('[BLACK(O)]')
    else:
        print('[WHITE(+)]')

    print(' 12345678')
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
    print('   1  2  3  4  5  6  7  8')
    for y in range(8):
        print(f"{y+1}", end='-')
        for x in range(8):
            #print(ban[y][x].format(), end=',')
            print('{:>2d}'.format(ban[y][x]), end=',') 
        print("")


def othello_loop():
    global f_pass
    global now_koma
    global pass_status
    game_fin = False

    #オセロ盤表示
    display(ban)

    while True:
        #駒が置けるかすべてのマスを判定する
        f_pass = True
        for y in range(8):
            for x in range(8):
                chk_ban[y][x] = checkBan(x, y, now_koma)

                #ひっくり返せるマスがあるならパスは無し
                if chk_ban[y][x] != 0:
                    f_pass = False
        
        disp_ban(chk_ban)

        #置ける場所があるなら入力を促す
        if f_pass != True:
            #置ける
            pass_status = NONE

            while True:
                # 駒を置く位置を入力する
                ix, iy = map(int, input("駒を置いてください.(x y):").split())  #mapで数字に変換
                print(f"{ix} {iy}")

                # 駒が置けるか判定
                if chk_ban[iy-1][ix-1] > 0:
                    #print('駒が置ける')

                    # 駒をひっくり返す
                    checkBan(ix-1, iy-1, now_koma, True)
                    ban[iy-1][ix-1] = now_koma
                    break
                else :
                    #置けなければやり直し
                    print('置けません')
                    continue

        else:
            #ゲーム終了判定
            game_fin = False    #終了判定用フラグ
            empty = False       #空き判定用フラグ
            #終了条件
            # 1 盤に全て駒が置かれた
            # 2 両者共にパス（置けない）
            for y in range(8):
                for x in range(8):
                    if(ban[y][x] == NONE):
                        empty = True     #空きあり

            if(empty != True) or (pass_status != NONE):
                #空きがない又は両者パスの場合
                game_fin = True     #ゲーム終了
            else:
                pass_status = now_koma  #パスしたことを保存

        if(game_fin == True):
            #ゲーム終了ならループを抜ける
            break

        #終了でなければ次プレーヤに移行
        if now_koma == BLACK:
            now_koma = WHITE
        else:
            now_koma = BLACK

        #盤面表示更新
        display(ban)

    #結果発表
    blk_rst, whi_rst = koma_status()
    if( blk_rst > whi_rst):
        print('BLACKの勝ち')
    elif (whi_rst > blk_rst):
        print('WHITEの勝ち')
    else:
        print('引き分け')       



#
#メイン
#
if __name__ == "__main__":
    #ゲーム開始
    othello_loop()






