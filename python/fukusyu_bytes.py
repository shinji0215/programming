#structモジュール
#pack()
#unpack()
#calcsize()

from struct import pack, unpack, calcsize

#書式指定文字	説明	サイズ（バイト数）
#c	文字	1
#b	符号付き整数	1
#B	符号なし整数	1
#h	符号付き整数	2
#H	符号なし整数	2
#i	符号付き整数	4
#I	符号なし整数	4
#l	符号付き整数	4
#L	符号なし整数	4
#f	浮動小数点数	4
#d	浮動小数点数	8
#s	文字列	-
#<	リトルエンディアンの指定	-
#>	ビッグエンディアンの指定	-


#ID:4byteの整数
#名前:3byteの文字列
#データ:4バイトの整数
#書式指定文字 'l3sl'
mydata = [
    (1, 'FOO', 1023), 
    (2, 'BAR', 80), 
    (3, 'BAZ', 4000)
    ]

result = pack('l3sl', mydata[0][0], mydata[0][1].encode(), mydata[0][2])    #bytes型に変換
print(result)       #b'\x01\x00\x00\x00FOO\x00\xff\x03\x00\x00'

myfile = open('mydata.bin', 'wb')
for item in mydata:
    result = pack('l3sl', item[0], item[1].encode(), item[2])
    myfile.write(result)
myfile.close()

size = calcsize('l3sl')
myfile = open('mydata.bin', 'rb')

content = myfile.read(size)
while content:
    restored_data = unpack('l3sl', content)
    print(restored_data)
    content = myfile.read(size)
myfile.close()


