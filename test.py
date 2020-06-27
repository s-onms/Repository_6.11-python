# -*- coding: utf-8 -*
# ↑これで日本語コメントアウトのエラー解決出来る

print("test")

total = 100
total /= 2
print(total)

s = 'string'[-3:-1]
print(s)

# ５文字毎に飛ばし読みする場合
tobashiyomi = 'hiraganagayomenai'[::5]
print(tobashiyomi)

# 郵便番号を作る場合(5行目で表示可)
post_number1 ='5530001'[:3] + '-'
post_number2 ='5530001'[:4:] 

print(post_number1) 
print(post_number2) 
print(post_number1 + post_number2) 

# モジュールを使う
# 1・・まずモジュールを「インポート」
# 2・・あとは殆どいつも通り変数（あだ名付けれる空箱）にはめる
import  random
num = random.random()
print(num)

# サイコロを作る
# まず、整数の範囲を指定する
# これで、1から6をランダムの生成出来る
dais = random.randint(1,6)
print(dais)

# モジュール名を変更
import ramdom as r
num2 = r.randint(10,15)
print(num2)


