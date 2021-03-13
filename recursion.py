def addup(num):
  if num == 1:
    return 1
  else:
    return num + addup(num - 1)

print(addup(100))

def factorial(num):
  if num == 1:
    return 1
  else:
    return num * factorial(num - 1)
  
print(factorial(5))