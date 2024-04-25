# 問 2. 台形積分 <関数>

import math
# from math import sin, pi
# # --example--
# # print(sin(0))
# # >>> 0
# -----------

def f1(x):
  return math.sin(x)

def f2(x):
  return 4 / (1 + (x ** 2))

def f3(x):
  return math.pi ** (0.5) *math.exp(-x ** 2)

def trapezoidal_integral(f, a=0, b=1, n=100):
  h = (b - a) / n
  S = 0
  for i in range(1, n + 1):
    S += (h / 2) * (f(a + ((i -1))*h) +f(a + (i * h)))

  return S

#(1)～(3)の解答

result_1 = trapezoidal_integral(f1, 0, math.pi/2, 50)
result_2 = trapezoidal_integral(f2, 0, 1, 100)
result_3 = trapezoidal_integral(f3, -100, 100, 1000)

print(result_1)
print(result_2)
print(result_3)