# 問3．ユークリッドの互除法

a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
r = a % b

while r != 0:

  a = b
  b = r
  r = a % b

if r == 0:
  print(b)
