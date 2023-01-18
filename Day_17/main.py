from getpass import getpass as hiddenInput


valid_input = ["rock","paper","scissors"]
player_one=input("What is player one's name? > ")
player_two=input("What is player two's name? > ")
player_one_score = 0
player_two_score = 0

while True:
  print("Select your move Rock, Paper, or Scissors")
  
  player_one_selection = hiddenInput("What is your selection {0}? > ".format(player_one)).lower()
  player_two_selection = hiddenInput("What is your selection {0}? > ".format(player_two)).lower()
  
  if(player_one_selection not in valid_input):
      print("{0} {1} is not a valid input lets try again".format(player_one,player_one_selection))
      continue
  
  if(player_two_selection not in valid_input):
      print("{0} {1} is not a valid input lets try again".format(player_two,player_two_selection))
      continue
  
  if(player_one_selection == player_two_selection):
      print("Looks like you both tied!")
      exit()
  
  if((player_one_selection == "rock" and player_two_selection == "scissors") 
  or (player_one_selection == "paper" and player_two_selection == "rock")
  or (player_one_selection ==  "scissors" and player_two_selection == "paper")):
      print("{0} beats {1} {2} Wins!".format(player_one_selection,player_two_selection,player_one))
      player_one_score += 1
      print("With a score of {0}".format(player_one_score))
  
  elif((player_two_selection == "rock" and player_one_selection == "scissors") 
  or (player_two_selection == "paper" and player_one_selection == "rock")
  or (player_two_selection ==  "scissors" and player_one_selection == "paper")):
      print("{0} beats {1} {2} Wins!".format(player_two_selection,player_one_selection,player_two))
      player_two_score += 1
      print("With a score of {0}".format(player_two_score))

  if(player_one_score  == 3):
    print("Congrats {0} you are the winner with a score of {1}!".format(player_one,player_one_score))
  elif(player_two_score  == 3):
    print("Congrats {0} you are the winner with a score of {1}!".format(player_two,player_two_score))

  if(player_one_score  == 3 or player_two_score == 3):
    play_again = input("Would you like to play again? Enter yes or no? >")
    if(play_again.lower() == "yes"):
      player_one_score = 0
      player_two_score = 0
    else:
      print("Thanks for playing {0} and {1}!".format(player_one, player_two))

