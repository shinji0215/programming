## data
# int
# str
# float
# fomat()


def p2_1_Data():
    print("**int型**")
 
    ### 整数int型
    d0 = 0b00111101     #2進数
    d1 = 0o7            #8進数
    d2 = 0x1f           #16進数
    d3 = 1234           #10進数
    d4 = 0b1111_0101_0011_0000  #アンダースコアを挿入可能

    print(d0)                   #61 出力は10進数
    print(d1)                   #7
    print(d2)                   #31
    print(d3)                   #1234
    print(d4)                   #62768
    print(type(d4))             #型確認 <class 'int'>

    #計算
    result = 0b10 * 0o10 + 0x10     #合計 2*8 + 16=32
    print(result)

    #整数値<int> -> 文字列<str>変換
    print(str(d0))              #61 10進数の文字列になる

    #bin()/oct()/hex() 2/8/16進数表記の文字列に変換
    print(bin(d0))              #0b111101
    print(oct(d1))              #0o7
    print(hex(d2))              #0x1f
    print(type(bin(d0)))        #型確認 <class 'str'>
  
    #format() b/o/x 書式化指定文字列 2/8/16進数表記
    print(format(d0, 'b'))      #2進数　111101
    print(format(d0, '#b'))     #2進数 プレフィックス0b付き 0b111101
    print(format(d0, '08b'))    #2進数 8桁0埋め 00111101
    print(format(d0, '#010b'))  #2進数 10桁0埋めプレフィックス0b付き 0b00111101

    #文字列<str> -> 整数<int>
    #int(文字列,基数)
    print(int('10'))            #10 10進数
    print(int('10', 2))         #2  2進数
    print(int('10', 8))         #8  8進数
    print(int('10', 16))        #16 16進数

    #文字列型 str型
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


    ###浮動小数点 float型
    f1 = 3.14           #浮動小数点float
    f2 = 1.0e-3         #浮動小数点1.0*10^-3
    f3 = 1.0e-5         #浮動小数点1.0*10^-5
    print(f2)           #0.001
    print(f3)           #1.0e-5 小数点5桁以上は指数表記
    print(type(f1))     #型確認 <class 'float'>

    #浮動小数点<float> -> 文字列<str>
    print(str(f1))          #3.14
    print(str(f2))          #0.001
    print(str(f3))          #1.0e-5

    #文字列<str> -> 浮動小数点<float>
    print(float('3.14'))        #4.32
    print(float('1.0e-3'))      #0.001


if __name__ == "__main__":
    print("***fukusyu.py***")
    p2_1_Data()

