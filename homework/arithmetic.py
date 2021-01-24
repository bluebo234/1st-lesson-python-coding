a = 2
b = 0
c = int(input("What number do i add up to? "))
while a < c + 1:
  b = a + b
  a = a + 2
print(b)