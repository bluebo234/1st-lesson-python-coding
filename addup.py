def addup(num):
  if num == 2:
    return 2
  else:
    return num + addup(num - 2)

print(addup(10))


def factorial(number, times):
  if number == 1:
    return 1
  else:
    return number * factorial(number - 1, times - 1)

print(factorial(4, 4))
