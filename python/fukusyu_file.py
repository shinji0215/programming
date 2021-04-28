#file読み書き
#read()/readline()/readlines()

myfile = open('sample.txt')     #ファイルを開く
lines = myfile.read()           #内容を読み込む　改行含む全ての行が1つの文字列
print(lines)

#文字列を'\n'で分割
#分割してリスト化したものをenumerate関数でindexと要素で反復処理
#0:12345
#1:abcde
#2:AABBCC
#3:
for count, line in enumerate(lines.split('\n')):
    print(f'{count}:{line}')

myfile.close()      #ファイルを閉じる


myfile = open('sample.txt')     #ファイルを開く
line = myfile.readline()        #内容を読み込む　改行含む1行
#print(f'[{line}]')             #[12345\n]  改行含む
while line != '':           #ファイル末尾で空文字''になるまで繰り返す
    print(f'{count}:{line}', end='')
    count += 1
    line = myfile.readline()

myfile.close()


myfile = open('sample.txt')     #ファイルを開く
#lines = myfile.readlines()      #内容を読み込む　改行含む全ての行をリスト化
#print(lines)                    #['12345\n', 'abcde\n', 'AABBCC\n']

for count, line in enumerate(myfile.readlines()):
    print(f'{count}:{line}', end='')

myfile.close()      #ファイルを閉じる


myfile = open('sample.txt')     #ファイルを開く
for count, line in enumerate(myfile):       #ファイルオブジェクトを直接使ってもできる
    print(f'{count}:{line}', end='')
myfile.close()      #ファイルを閉じる


if __name__ == "__main__":
    print("***fukusyu.py***")

