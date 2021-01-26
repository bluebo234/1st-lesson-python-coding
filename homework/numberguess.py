import random
rn = random.randint(1, 100)
guess = int(input("I have chosen a number between 1 and 100. You have to type and guess the number. I will tell you if the number is higher or lower than the random number. "))
while guess != rn:
  if guess > rn:
    print("The number I am thinking of is lower than", guess,)
  elif guess < rn:
    print("the number I am thinking of is higher than", guess,)
  else:
    print("Congratulations! The number was", rn,)
  guess = int(input("Guess another number. "))
print("Congratulations! The number was", rn,"!")