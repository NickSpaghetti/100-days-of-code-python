import random
is_correct_number = False
my_number = random.randrange(1, 1_000_000)
attempts = 0
while(not is_correct_number):
  guess = int(input("Guess a number between 0 and 1,000,000?> "))
  if guess < 0:
    print("Guess you don't want to play anymore.")
    exit()
    
  if(guess == my_number):
    print("You got it!")
    is_correct_number = True
  elif(guess < my_number):
    print("My number is higher than {0}".format(guess))
  elif(guess > my_number):
    print("My number is less than {0}".format(guess))

  attempts += 1
  
print("It took you {0} attemps to get guess {1}".format(attempts,my_number))