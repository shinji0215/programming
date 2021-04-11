

f_pass = False   #パス実行有無

class Ban:
    def __init__(self):
        self.status = 0
        self.friend_ps = [0,0,0,0,0,0,0,0]   #味方の駒。0:なし 1:あり

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



def checkBan(x, y):
    """駒が置けるか？"""



def display():
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



def othello_loop():
    global f_pass
    while True:
        # 駒を置く位置を入力する
        x, y = map(int, input("駒を置いてください.(x y):").split())  #mapで数字に変換
        print(f"{x} {y}")
        ban[y-1][x-1] = BLACK

        # 駒が置けるか判定

        # 駒をひっくり返す

        #盤面表示更新
        display()

        #ゲーム終了判定

        #次プレーヤのパス判定
        
        if f_pass != True:
            print("passしない")
            break
        else:
            print("passする")

    #結果発表

#
#メイン
#
#オセロ盤表示
display()

#ゲーム開始
othello_loop()





