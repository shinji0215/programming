#include <stdio.h>
#include <string.h>


struct ban
{
    int status; //0:なし　1: 黒 2:白.
    int friend_ps[8];   // 味方の位置. 0:なし 1:あり.
};

#define TRUE        1
#define FALSE       0

#define NONE        0
#define BLACK       1
#define WHITE       2

struct ban sBan[8][8];      //盤状態.
int active;                 //順番.
int pass;

struct check
{
    int y;
    int x;
};
struct check chk[] = 
{
    {-1, 0},    // 上(y:-1, x:0).
    {-1, +1},   // 右上(y:-1, x:+1).
    {0, +1},    // 右(y:0, x:+1).
    {+1, +1},   // 右下(y:+1, x:+1).
    {+1, 0},    // 下(y:+1, x:0).
    {+1, -1},   // 左下(y:+1, x:-1).
    {+0, -1},   // 左(y:0, x:-1).
    {-1, -1},   // 左上(y:-1, x:-1).
};

void display(void);
void init(void);
int checkBan(int x, int y);
int checkGame(void);
void judgeGame(void);
int checkPass(void);
int checkValid(int x, int y);
void updateBan(int x, int y);

// メイン.
int main(void)
{
    int x, y;
    char input_disp[256];

    printf("start\n");
    init();

    // オセロ盤表示.
    display();

    for(;;)
    {
        if(TRUE != pass)
        {
            // 駒を置く位置を入力する.
            if(BLACK == active)
            {
                strcpy(input_disp, "BLACK ");
            }
            else
            {
                strcpy(input_disp, "WHITE ");
            }
            strcat(input_disp, "駒を置いてください.(x y)");
            printf("%s\n",input_disp);
            scanf("%d %d",&x ,&y);

            printf("x=%d y=%d\n",x ,y);

            // 駒が置けるか?.
            if(TRUE != checkBan(x, y))
            {
                printf("置けません x=%d y=%d\n",x ,y);
                display();
                continue;
            }

            // 駒を置く.

            // ひっくり返す.
            updateBan(x, y);

        }
        else
        {
            printf("PASS!!!.\n");
        }

        // オセロ盤再表示.
        display();

        // ゲーム終了か？.
        if(TRUE == checkGame())
        {
            printf("ゲーム終了.\n");
            break; // ゲーム終了.
        }

        // 順番交代.
        if( BLACK == active )
        {
            active = WHITE; // 次は白.
        }
        else
        {
            active = BLACK; // 次は黒.
        }
        // 次は駒が置くことができるか？パスするか？
        if(TRUE == checkPass())
        {
            pass = TRUE;
        }
        else
        {
            pass = FALSE;
        }
        
        
    }

    // 勝者判定.
    judgeGame();

    // 終了.
    return 0;
}
// 初期化.
void init(void)
{
    active = BLACK;     // 黒先行.
    pass = FALSE;

    sBan[3][3].status = BLACK;
    sBan[4][4].status = BLACK;
    sBan[4][3].status = WHITE;
    sBan[3][4].status = WHITE;

}

//　コマが置けるか？
int checkBan(int x, int y)
{
    int ret = TRUE;

    // 範囲チェック
    if(  (( x > 8) || (x < 1))
       ||(( y > 8) || (y < 1)))
    {
        return FALSE;
    }

    // すでに置いてあるか？
    if( sBan[y-1][x-1].status != NONE )
    {
        return FALSE;
    }

    // 相手コマを返せるか？
    ret = checkValid(x, y);

    return ret;
}

// 駒を置く.
void updateBan(int x, int y)
{
    //printf("------updateBan call\n");
    int next_x;
    int next_y;

    // 駒を置く.
    sBan[y-1][x-1].status = active;

    // ひっくり返す.
    for(int loop=0; loop < 8; loop++)
    {
        if(TRUE != sBan[y-1][x-1].friend_ps[loop])
        {
            //printf("この筋には無い.loop=%d\n", loop);
            continue;
        }

        next_x = x;
        next_y = y;
        for(;;)
        {
            next_x += chk[loop].x;
            next_y += chk[loop].y;

            // 範囲外.
            if(  (( next_x > 8) || (next_x < 1))
               ||(( next_y > 8) || (next_y < 1)))
            {
                printf("範囲外。無いはず.loop=%d\n", loop);
                break;  // 無いはず.
            }
            // 駒が置いていない.
            if(NONE == sBan[next_y-1][next_x-1].status)
            {
                printf("駒がない。無いはず.loop=%d\n", loop);
                break;  // 無いはず.
            }
            // 自分の駒.
            if(active == sBan[next_y-1][next_x-1].status)
            {
                //printf("自分の駒まで到達.loop=%d (x=%d,y=%d)\n", loop, next_x, next_y);
                break;
            }
            // 相手の駒なので返す.
            if(active != sBan[next_y-1][next_x-1].status)
            {
                sBan[next_y-1][next_x-1].status = active;
                //printf("返す(x=%d,y=%d)\n", next_x, next_y);
            }
        }
    }
}

// ゲーム終了判定
int checkGame(void)
{
    int gameend = TRUE;

    // 全ての盤に駒を置いたか？
    for(int i=0; (i<8 && gameend==TRUE); i++)
    {
        for(int j=0; (j<8 && gameend==TRUE); j++)
        {
            if( NONE == sBan[i][j].status)
            {
                gameend = FALSE;    // ゲームはつづく.
                //printf("checkGame: x=%d y=%d\n",j+1, i+1);
            }
        }
    }

    return gameend;
}

// 勝者判定.
void judgeGame(void)
{
    int blackValue = 0;
    int whiteValue = 0;

    // 全ての盤に駒を置いたか？
    for(int i=0; i<8; i++)
    {
        for(int j=0; j<8; j++)
        {
            switch(sBan[i][j].status)
            {
                case BLACK:
                    blackValue++;
                    break;
                case WHITE:
                    whiteValue++;
                    break;
                case NONE:
                default:
                    break;
            }

        }
    }
    printf("black=%d white=%d\n",blackValue, whiteValue);

    if( blackValue > whiteValue)
    {
        printf("black victory!\n");
    }
    else if( whiteValue > blackValue)
    {
        printf("white victory!\n");
    }
    else
    {
        printf("draw.\n");
    }
}

//　パス判定.
int checkPass(void)
{
    int ret = FALSE;

    // 全ての盤に駒を置いたか？
    for(int i=0; i<8; i++)
    {
        for(int j=0; j<8; j++)
        {
            if( NONE == sBan[i][j].status)
            {
                ret = checkValid(j+1, i+1); //有効判定.
            }
        }
    }
    return ret; 
}

// 置き場所は有効か？相手を返せるか？.
int checkValid(int x, int y)
{
    //printf("-----checkValid call\n");

    int ret = FALSE;
    int next_x;
    int next_y;
    int enemy;  // 相手の駒.

    for(int loop=0; loop < 8; loop++)
    {
        next_x = x;
        next_y = y;
        enemy = FALSE;

        for(;;)
        {
            sBan[y-1][x-1].friend_ps[loop] = FALSE;

            next_x += chk[loop].x;
            next_y += chk[loop].y;
            //printf("check loop=%d (x=%d,y=%d)\n", loop, next_x, next_y);

            // 範囲外.
            if(  (( next_x > 8) || (next_x < 1))
               ||(( next_y > 8) || (next_y < 1)))
            {
                //printf("範囲外. loop=%d (x=%d,y=%d)\n", loop, next_x, next_y);
                break;
            }
            // 駒が置いていない.
            if(NONE == sBan[next_y-1][next_x-1].status)
            {
                //printf("駒がない. loop=%d (x=%d,y=%d)\n", loop, next_x, next_y);
                break;
            }
            // 自分の駒.
            if(active == sBan[next_y-1][next_x-1].status)
            {
                // 相手の駒を見つけていれば、有効.
                if(TRUE == enemy)
                {
                    //printf("自分の駒で挟める. loop=%d (x=%d,y=%d)\n", loop, next_x, next_y);
                    sBan[y-1][x-1].friend_ps[loop] = TRUE;
                    ret = TRUE;     // 自分の駒で挟めている.
                }
                break;
            }
            enemy = TRUE;   //　相手の駒あり.
        }
    }

    return ret;
}

// 画面表示.
void display(void)
{
    printf(" １２３４５６７８\n");

    for(int y=0; y<8; y++)
    {
        printf("%d",y+1);
        for(int x=0; x<8; x++)
        {
            switch(sBan[y][x].status)
            {
                case 1:
                    printf("黒");
                    break;
                case 2:
                    printf("白");
                    break;
                case 0:
                default:
                    printf("・");
                    break;
            }
        }
        printf("\n");
    }
    printf("\n");
/*    
    printf("1________\n");
    printf("2________\n");
    printf("3________\n");
    printf("4___O+___\n");
    printf("5___+O___\n");
    printf("6________\n");
    printf("7________\n");
    printf("8________\n");
*/
}
