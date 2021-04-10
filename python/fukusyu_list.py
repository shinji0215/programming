
#リスト・・一度セットした値を変更可能 []
#タプル・・一度セットした値は変更不可 ()
#range・・連続した数値
#これら３つはイテレート可能なオブジェクト

#リスト
l_data1 = ['aa', 'bb', 'cc', 'dd', 'ee']
print(l_data1[0])       #aa
print(l_data1[-1])      #ee 最後の要素
print(l_data1[0:3])     #['aa', 'bb', 'cc'] スライス index=0~2
print(l_data1[-3:-1])   #['cc', 'dd']
print(l_data1[::2])     #['aa', 'cc', 'ee'] 2つおきにスライス
print(l_data1[::-1])    #['ee', 'dd', 'cc', 'bb', 'aa'] -1だと逆順でスライス

#リストの更新
l_data1[0] = '11'
print(l_data1)          #['11', 'bb', 'cc', 'dd', 'ee']
l_data1.append('ff')    #最後に追加
print(l_data1)          #['11', 'bb', 'cc', 'dd', 'ee', 'ff']
l_data1.pop()           #最後のデータを取り出す
print(l_data1)          #['11', 'bb', 'cc', 'dd', 'ee']
ret = l_data1.pop(0)    #最初のデータを取り出す
print(l_data1)          #['bb', 'cc', 'dd', 'ee']
print(ret)              #11

#list関数　リストを作成
print(list(range(10)))      #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 11)))   #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list('book'))         #['b', 'o', 'o', 'k']

#len関数 長さを返す
print(len(l_data1))         #4

#リストのリスト(多重リスト)
l_x = [1, 2, 3, 4, 5, 6]
l_y = [10, 20, 30, 40, 50]
l_area = [l_x, l_y]
print(l_area)           #[[1, 2, 3, 4, 5, 6], [10, 20, 30, 40, 50]]
print(l_area[0])        #[1, 2, 3, 4, 5, 6]
print(l_area[1][3])     #40

#2次元配列
l_ban = []
for i in range(3):
    l_ban.append(list(range(3)))

print(l_ban)        #3x3 [[0, 1, 2], [0, 1, 2], [0, 1, 2]]


##リストの操作
l_data2 = list('abc')
l_data3 = list('def')
l_data2.extend(l_data3)     #別のリスト要素を追加
#l_data2 += l_data3          # +=でも同じ
print(l_data2)              #['a', 'b', 'c', 'd', 'e', 'f']

l_data3.insert(1, 'Z')      #指定indexに要素を追加
print(l_data3)              #['d', 'Z', 'e', 'f']

del l_data3[1]              #指定indexの要素を削除
print(l_data3)              #['d', 'e', 'f']

l_data2.remove('d')         #値を指定して削除　indexがわからない時に使用
print(l_data2)              #['a', 'b', 'c', 'e', 'f']

index = l_data2.index('b')  #指定した値のindexを調べる
print(index)                #1

print('a' in l_data2)       #True 値'a'が存在するか調べる

l_data4 = list('a1b1c1')
print(l_data4.count('1'))   #指定した値がいくつ存在するか調べる

n = [5, 3, 0, 4, 1]
n.sort()                    #昇順で並べ替え
print(n)                    #[0, 1, 3, 4, 5]
n.sort(reverse=True)        #降順で並べ替え
print(n)                    #[0, 1, 3, 4, 5]

#リストのコピー
l_data5 = [1, 2, 3]
l_data6 = l_data5           #参照の代入
print(l_data6)
l_data5[0] = 99             #l_data5を変更
print(l_data6)              #l_data6にも反映（l_data6はl_data5を参照）

l_data5 = [1, 2, 3]
l_data7 = l_data5.copy()    #l_data5のコピー
l_data8 = list(l_data5)     #l_data5の全ての要素をコピー
l_data9 = l_data5[:]        #l_data5の全ての要素をスライスして作成
l_data5[1] = -99
print(l_data5)              #[1, -99, 3]
print(l_data7)              #[1, 2, 3] 変化なし
print(l_data7)              #[1, 2, 3] 変化なし
print(l_data7)              #[1, 2, 3] 変化なし

#リスト内表記
comp1 = [num for num in range(1, 6)]
print(comp1)                #[1, 2, 3, 4, 5]
comp2 = [num for num in range(1, 6) if num % 2 == 1]
print(comp2)                #[1, 3, 5]

#
#タプル(書き換え不可)
#
t_1 = ('a', 'b', 'c', 'd')      
print(t_1)                      #('a', 'b', 'c', 'd')
t_2 = 'A', 'B', 'C'             #()は無くても良い。','がタプル
print(t_2)                      #('A', 'B', 'C')
a1, b1, c1, = t_2               #タプルは一度に変数に代入可能
print(a1, b1, c1, sep=':')      #A:B:C


def f_list():
    print("p_list")


if __name__ == "__main__":
    print("***fukusyu.py***")
    f_list()

