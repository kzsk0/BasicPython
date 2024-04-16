# 問1.　素数判定

a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TODO
def prime_number(n):
  if n <= 1:
    return False

  elif n % 2 == 0 or n % 3 == 0:
    return False

  elif n % 5 == 0 or n % 7 == 0:
    return False

  else:
    return True

if prime_number(a):
    print("aは素数")
else:
    print("aは素数ではない")

if prime_number(b):
    print("bは素数")
else:
    print("bは素数ではない")