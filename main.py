def star(n):
  if n == 1:
     print('*', end="")
  print(star(n/3)) * 3
  print(star(n/3), star(n/3))
  print(star(n/3)) * 3

n = int(input())
print(star(n))