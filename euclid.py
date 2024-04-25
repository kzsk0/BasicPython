# 問3．ユークリッドの互除法 <関数>

# a = int(input("a の値を入力: "))
# b = int(input("b の値を入力: "))

# TODO

def euclid(a,b):
  r = a % b
  while r != 0:
    a = b
    b = r
    r = a % b

  if r == 0:
    return b

euclid(a,b)

# 問 4. 互いに素　<関数>

import random
counts = 0

def mutually_prime(a, b): 
  if euclid(a,b) == 1: # 互いに素 ⇔ 最大公約数が 1
    return True
  else:
    return False


# エクストラ問題
for i in range(100000): # 10万個
  a = random.randint(1, 10000) # 1万以下の自然数
  b = random.randint(1, 10000)

  if mutually_prime(a, b) == True:
    counts += 1

p = counts / 100000 # 各組が互いに素である確率
print(p)
