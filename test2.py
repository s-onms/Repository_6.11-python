# map(関数、イテレーター)

def triple(n):
  return n * 3

# 「lambda 引数: 処理」
print(list(map(triple,[1,2,3])))