def addup(total, index, max):

  total = total + index
  index = index + 1
  if index > max:
    return total
  else:
    return addup(total, index, max)

print (addup(0, 1, 10))

def factorial(total, times, max):

  total = total * (total - 1)
  times = times - 1
  if times < 1:
    return total
  else:
    return factorial(total, times, max)

print(factorial(5, 2, 10))