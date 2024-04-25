# 問 1. 素数判定 <関数>
# エクストラ問題

list = [61, 10, 3.14, -1, 1]
def prime_number(n):
    if n < 0:
      return("error")
    elif n <= 1:
      return False
    elif isinstance(n, float):
      return("error")

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in list:
  print(prime_number(i))