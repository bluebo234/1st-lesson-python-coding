import random
rn = random.randint(1, 100)
guess = input("I have chosen a number between 1 and 100. You have to type and guess the number. I will tell you if the number is higher or lower than the random number.")
while guess != rn:
  if guess > rn:
    print()