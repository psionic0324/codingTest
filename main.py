def func(n, i, j):
  if i // n % 3 == 1 and j // n % 3 == 1:
    print(" ", end="")
  elif n // 3 == 0:
    print("*", end="")
  else:
    func(n//3, i, j)

n = int(input())
for i in range(n):
  for j in range(n):
    func(n, i, j)
  print()
"""
함수의 정의
  func(n, i, j)
base condition
  n = 0 return 0
재귀 식
  return func(n-1)
"""