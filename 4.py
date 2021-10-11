# 4. Trvac e a = 1, b = 1. a-n fibonacci-i hajordakanutyan mej arajin tivn e, isk b-n 2-rd tiv@. j = input() e arvum kamayakan tiv.
# Petq e tpel fibonacci-i hajordakanutyan mej j-rd tiv@.


phi = ((5 ** 0.5) + 1) / 2

def fib(n):
    t = int(((phi ** n) - ((-1 * phi) ** (-1 * n))) / 5 ** 0.5)
    return t


print(fib(50))
