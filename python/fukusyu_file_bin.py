#バイナリファイル
#bytes()    bytes型オブジェクト生成
#encode()   文字列をエンコードしてbytes型を返す
#decode()   bytes型を文字列に変換
#from_bytes()   bytes型を指定エンコードで変換

#bytes型
b1 = b'a'
b2 = b'abc'
b3 = b'\x61'
print(b1, b2, b3)   #b'a' b'abc' b'a'
print(type(b1))     #<class 'bytes'>

b4 = bytes(5)                   #5byteのbytesオブジェクト作成(全要素0)
b5 = bytes([0x61, 0x62, 0x63])
b6 = bytes('abc', 'utf-8')       #文字列abcをUTF-8でエンコード
print(b4, b5, b6)                #b'\x00\x00\x00\x00\x00' b'abc' b'abc'

encode_value = 'あ'.encode()    #UTF-8でエンコードしてbytes型へ
print(encode_value)             #b'\xe3\x81\x82'    UTF-8の'あ'は3byteのbytes型
print(type(encode_value))       #<class 'bytes'>

decode_value = encode_value.decode()    #3byteのbytes型を文字列に変換
print(decode_value)                     #あ
print(type(decode_value))               #<class 'str'>

#バイナリファイル読み書き
binfile = open('testtest.txt','rb')     #バイナリモードで読み込み
content = binfile.read()
print(content)
binfile.close()

def get_dimension(filename):
    f = open(filename, 'rb')
    spec = f.read(6).decode()       #先頭6byte読み込み
    width = int.from_bytes(f.read(2), 'little')     #リトルエンディアンで変換
    height = int.from_bytes(f.read(2), 'little')
    f.close()
    print(f'this file is {spec}, size: {width} x {height}') #this file is GIF89a, size: 660 x 380

get_dimension('img_yokohama_02.gif')



