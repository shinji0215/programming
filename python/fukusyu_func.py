
g_num = 100             #グローバル変数(モジュール変数)
    #モジュール全ての箇所で参照可能

def f_func():
    print("f_func")
    #基本関数

def func1(arg1, arg2):
    print("func1-----") 
    #ローカル変数
    #arg1,arg2,retは関数内のみが有効範囲
    ret = arg1 + arg2 + g_num   #g_numは参照可能
    #g_num = 200        #グローバル変数は変更不可

    print(dir())             #func2関数内ローカルスコープ表示['arg1', 'arg2', 'ret']
    print("func1 end-----")
    return ret      #関数戻り値

def func2(arg1, arg2):
    print("func2-----")
    global g_num        #グローバル宣言
    g_num = 200         #グローバル変数を変更可能

    ret = arg1 + arg2 + g_num   #g_numは参照可能

    print(locals())             #func2関数内ローカルスコープ表示{'arg1': 1, 'arg2': 2, 'ret': 203}
    print("func2 end-----")
    return ret      #関数戻り値

def sub1():
    print('sub1')
    a = 'c++'
    #関数内に関数定義可能
    def sub1_1():
        print('sub1_1')
        a = 'java'
        print(a)        #java

    sub1_1()
    print(a)            #c++

def sub2():
    a = 'python'
    print('sub2')
    sub1()
    print(a)        #python

def main():
    print("main-----")
    ret = 1
    result = func1(1, 2)
    print(result)           #103=1+2+100
    print(ret)              #1 main関数スコープのret
    print(g_num)            #100 グローバル変数g_num

    print(func2(1,2))
    print(g_num)            #200 グローバル変数g_num func2で変更    
    print("main end-----")

    #sub1()
    #sub1_1()                 #関数内関数は関数外から実行できない
    sub2()

#def sub1()
#    return 10
# 関数は呼び出す前に宣言しなければいけない


if __name__ == "__main__":
    print("***fukusyu.py***")
    f_func()
    main()
    print(locals())             #グローバルスコープ表示
    print(locals()==globals())  #True トップレベルのローカルスコープとグローバルスコープは同じ



