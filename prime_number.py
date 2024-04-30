# 問 1. 素数判定 <関数>
# エクストラ問題

list = [61, 10, 1, 3.14, -1]
def prime_number(n):
    if not isinstance(n, int):
      raise TypeError("int 型でないのでエラー")
    if n < 0:
      raise ValueError("自然数でないのでエラー")
    elif n <= 1:
      return False
    

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in list:
  print(prime_number(i))