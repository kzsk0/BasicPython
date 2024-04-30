# 問3．ユークリッドの互除法 <関数>


# TODO

def euclid(a,b):
  while a % b != 0:
    a, b = b, a % b
  return b
    

# 問 4. 互いに素 <関数>

import random
counts = 0

def mutually_prime(a, b):
  return euclid(a, b) == 1


# エクストラ問題
for i in range(100000): # 10万個
  a = random.randint(1, 10000) # 1万以下の自然数
  b = random.randint(1, 10000)

  if mutually_prime(a, b) == True:
    counts += 1

p = counts / 100000 # 各組が互いに素である確率
print(p)
