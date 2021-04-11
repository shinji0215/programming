# str型
#len() 長さ
#[::] 指定切り出し
#split() セパレータ毎に切り出し
#join()　連結
#replace() 置換
#format() 文字列生成
#書式指定子

def f_str():
    print("f_str")

    str1 = 'abcde'          #abcde
    str2 = "fghij"          #fghij  どちらも同じ
    str3 = '''klmn
opqr
stu'''      #'''は改行含めることが可能
    str4 = 'vwx\nz'         #\nは改行

    print(str1)             #abcde
    print(str2)             #fghij
    print(str3)             #klmn\nopqr\nstu
    print(str4)             #vwx\nz
    print(type(str4))       #型確認 <class 'str'>

    #連結
    result1 = str1 + str2   #abcdefghij
    print(result1)

    #繰り返し
    result2 = str2*3        #fghijfghijfghij
    print(result2)

    #文字の抽出[] 文字列[インデックス]
    print(str1[0])          #a
    print(str1[1])          #b
    print(str2[-1])         #j -1:右端

    #文字切り出し 
    #指定インデックスから末尾まで　文字列[インデックス:]
    print(str1[2:])         #cde
    print(str2[-3:])        #hij

    #先頭からインデックス-1まで　文字列[:インデックス]
    print(str1[:3])         #abc
    print(str2[:-3])        #fg

    #指定した範囲切り出し　文字列[インデックス:インデックス]
    print(str1[1:3])        #bc

    #指定文字数ごとに切り出し
    #先頭インデックスからステップ数ごとに末尾インデックス―1までを1文字づつスライス
    # 文字列[インデックス:インデックス:ステップ]
    str5 = '1234567890'
    print(str5[::2])            #13579
    print(str5[::3])            #1470
    print(str5[2:-2:2])         #357

    #文字の長さ
    str6 = '1234567890'
    print(len(str6))            #10文字

    #指定文字をセパレータとして切り分けsplit()
    str7 = '1,2,3,4,5,6,7,8,9,0'
    print(str7.split(','))      #[1 2 3 4 5 6 7 8 9 0]

    #連結2
    #連結に使用する文字.join(文字列リスト)
    str_list1 = str7.split(',')
    print('='.join(str_list1))      #1=2=3=4=5=6=7=8=9=0
    print(''.join(str_list1))       #1234567890
    print(','.join(str_list1))      #1,2,3,4,5,6,7,8,9,0
    print('\n'.join(str_list1))     #1\n2\n3\n4\n5\n6\n7\n8\n9\n0

    #置換
    #文字列.replace(置換前文字列,置換後文字列,置換回数)
    str8 = 'a*b*c*d*e*f*g*h*i*j*k'
    print(str8.replace('*','X',1))    #aXb*c*d*e*f*g*h*i*j*k
    print(str8.replace('*','X',10))   #aXbXcXdXeXfXgXhXiXjXk
    print(str8.replace('*','X',100))  #aXbXcXdXeXfXgXhXiXjXk 回数は多くても良い

    #文字列の自動生成format()
    print('こん{}は'.format(('にち')))              #こんにちは
    print('{}は{}です'.format('今日','雨'))         #今日は雨です
    print('{1}は{0}です'.format('4日','本日'))      #本日は4日です

    #書式指定子
    #type(値の表現型) b c d o x X n s e f % など..
    print('数値1={:d}, 数値2={:x}'.format(20, 31))  #数値1=20, 数値2=1f
    print('指数表記={:e}'.format(0.0001))           #指数表記=1.000000e-04
    print('パーセンテージ={:%}'.format(0.345))      #パーセンテージ=34.500000%

    #width(最小フィールド幅)
    print('[{:10s}]'.format('Lemon'))       #[Lemon     ] 文字列はデフォルト左詰め
    print('[{:5d}]'.format(123))            #[  123] 整数はデフォルト右詰め

    #fill(埋める),align(配置)
    print('[{:<7d}]'.format(-123))      #< 左詰め  [-123   ]
    print('[{:^7d}]'.format(-123))      #^ 中央    [ -123  ]
    print('[{:>7d}]'.format(-123))      #> 右詰    [   -123]
    print('[{:=7d}]'.format(-123))      #= 符号と値の間を埋める [-   123]
    print('[{:*<7d}]'.format(-123))     #指定文字で埋める  [-123***] 

    #signe(符号)
    print('[{:+d}],[{:+d}]'.format(72, -72))      #[+72],[-72]
    print('[{:-d}],[{:-d}]'.format(72, -72))      #[72],[-72]
    print('[{: d}],[{: d}]'.format(72, -72))      #[ 72],[-72]    

    #grouping_option(数値の区切り文字)
    print('[{:,d}]'.format(1234567))        #[1,234,567]
    print('[{:,f}]'.format(12345.678))      #[12,345.678000]
    print('[{:_d}]'.format(12345678))       #[12_345_678]

    #precision(小数部分の制度)
    print('{:f}'.format(1/3))               # 0.333333 デフォルト6桁
    print('{:.3f}'.format(1/3))             # 0.333 3桁
    print('{:.3f}'.format(0.55555))         # 0.556 小数点第4位を四捨五入

    #別形式 2,8,16進数の先頭に0b 0o 0xを付ける
    print("{:b},{:#b}".format(10, 10))      #1010,0b1010
    print("{:o},{:#o}".format(10, 10))      #12,0o12
    print("{:x},{:#x}".format(10, 10))      #a,0xa
    


if __name__ == "__main__":
    print("***fukusyu.py***")
    f_str()

