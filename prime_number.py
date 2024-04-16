# 問1.　素数判定

# 素数判定訂正

a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

def prime_number(n):
    if n <= 1:
        return "素数ではない"
    for i in range(2, n):
        if n % i == 0:
          return "素数ではない"
    return "素数である"


print(prime_number(a))
print(prime_number(b))