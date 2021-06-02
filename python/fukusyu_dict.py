#辞書型(dict)
#dict()
#get()

sk = {
    'first_name':'shinji',
    'family_name':'kawasaki',
    'weight':80
    }
print(sk)

#空の辞書
emptydict = {}
print(emptydict)

#dict関数による辞書の作成


#辞書から要素を取り出す
print(sk['first_name'])
#print(sk['age'])        #存在しないキーはエラーになるKeyError: 'age'

#get()関数
print(sk.get('first_name'))             #shinji
print(sk.get('age'))                    #None
print(sk.get('age', 'not found'))       #not found

#変更
sk['family_name'] = 'okazaki'
print(sk)       #{'first_name': 'shinji', 'family_name': 'okazaki', 'weight': 80}

#追加
sk['age'] = 150
print(sk)       #{'first_name': 'shinji', 'family_name': 'okazaki', 'weight': 80, 'age': 150}

#update()関数
mydict = {'foo':'FOO', 'bar':'BAR', 'baz':'BAZ'}
print(mydict)   #{'foo': 'FOO', 'bar': 'BAR', 'baz': 'BAZ'}
mydict.update(foo='fooo', somekey='somevalue')  #キーワード引数による更新
print(mydict)   #{'foo': 'fooo', 'bar': 'BAR', 'baz': 'BAZ', 'somekey': 'somevalue'}
mydict.update({'bar':'new BAR'})    #辞書による辞書の更新
print(mydict)   #{'foo': 'fooo', 'bar': 'new BAR', 'baz': 'BAZ', 'somekey': 'somevalue'}

#pop()関数　値の取得と削除
result = mydict.pop('bar')  #'bar'を削除
print(result)   #new BAR
print(mydict)   #{'foo': 'fooo', 'baz': 'BAZ', 'somekey': 'somevalue'}
result = mydict.pop('bar', 'no found')  #barは無いので'no found'
print(result)   #no found
#result = mydict.pop('bar')  #barは無いのでエラーKeyError: 'bar'

#setdefault()関数　指定KEYが存在すれば値を返す
print(mydict.setdefault('foo'))     #fooo

#反復処理
sk = {
    'first_name':'shinji',
    'family_name':'kawasaki',
    'weight':80
    }
for item in sk:     #KEYがループitemに渡される
    print(item, sk[item])

#keys()     KEYの一覧を返す、
#values()   値の一覧を返す
#items()    KEYと値の組の一覧を返す
for key, value in sk.items():   #KEYと値を渡す
    print(key, value)

print('kawasaki' in sk)         #False
print('kawasaki' in sk.values())    #True


unit_1 = {'type':'MS', 'name':'GM'}
unit_2 = {'type':'MA', 'name':'RD'}
unit_list = [
    unit_1, unit_2
]

print(unit_list)
print((unit_list[1])['name'])   #RD




