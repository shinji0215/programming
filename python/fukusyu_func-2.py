

def func1():
    #複数の戻り値(タプル)
    return 'abc', 100, [0, 1, 2]

def func2():
    #複数の戻り値(リスト)
    return ['abc', 100, [0, 1, 2]]

def func3():
    #単一の戻り値
    return 50

def arg_test1(a, b, c='デフォルト'):
    #デフォルト引数
    print(a, b, c)

def arg_test2(*args):
    #可変長パラメータ
    #パラメータがタプルとして扱う
    print(args)
    print(type(args))       #<class 'tuple'>
    for s in (args):
        print(s)

def arg_test3(**kwargs):
    #辞書型パラメータ
    print(kwargs)
    print(type(kwargs))


def run_something(func):
    #高階関数（関数を引数にわたす）
    ret = func()
    print(ret)

def run_something2(func, arg1, arg2):
    func(arg1, arg2)

def main():
    print("main")

    # 複数の戻り値(戻り値はタプル)
    result = func1()            #複数の戻り値
    print(result)               #('abc', 100, [0, 1, 2])
    print(type(result))         #<class 'tuple'>
    print(result[0])           #abc
    print(type(result[0]))     #<class 'str'>
    print(result[1])           #100
    print(type(result[1]))     #<class 'int'>
    print(result[2])           #[0, 1, 2]
    print(type(result[2]))     #<class 'list'>
    #result[1] = 200            #タプルのためエラーになる

    # 複数の戻り値（アンパックして各変数へ)
    ret1, ret2, ret3 = func1()
    print(ret1)
    print(ret2)
    print(ret3)
    ret2 = 200          #変更可能

   # 複数の戻り値(戻り値はリスト)
    l_result = func2()
    print(l_result)             #('abc', 100, [0, 1, 2])
    print(type(l_result))       #<class 'list'>
    l_result[1] = 2             #変更可能

    #単一の戻り値
    ret4 = func3()
    print(ret4)             #50
    print(type(ret4))       #<class 'int'>
    ret4 = 30               #変更可能

    #複数引数（c=デフォルト引数)
    arg_test1('aa', 'bb', 'cc')     #aa bb cc
    arg_test1('AA', 'BB')           #AA BB デフォルト

    #可変長パラメータ
    arg_test2(1, 2, 3, 4, 5)        #(1, 2, 3, 4, 5)

    #辞書型
    arg_test3(volley='ボーン', smash='パコーン')    #{'volley': 'ボーン', 'smash': 'パコーン'}

    #高階関数(関数を引数でわたす)
    run_something(func3)        #50
    run_something2(arg_test1, 'xx', 'yy')   #xx yy デフォルト

if __name__ == "__main__":
    print("***fukusyu.py***")
    main()

