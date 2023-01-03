from getpass import getpass as hiddenInput


valid_input = ["rock","paper","scissors"]
player_one=input("What is player one's name? > ")
player_two=input("What is player two's name? > ")

print("Select your move Rock, Paper, or Scissors")

player_one_selection = hiddenInput("What is your selection {0}? > ".format(player_one)).lower()
player_two_selection = hiddenInput("What is your selection {0}? > ".format(player_two)).lower()

if(player_one_selection not in valid_input):
    print("{0} {1} is not a valid input".format(player_one,player_one_selection))
    exit()

if(player_two_selection not in valid_input):
    print("{0} {1} is not a valid input".format(player_two,player_two_selection))
    exit()

if(player_one_selection == player_two_selection):
    print("Looks like you both tied!")
    exit()

if((player_one_selection == "rock" and player_two_selection == "scissors") 
or (player_one_selection == "paper" and player_two_selection == "rock")
or (player_one_selection ==  "scissors" and player_two_selection == "paper")):
    print("{0} beats {1} {2} Wins!".format(player_one_selection,player_two_selection,player_one))

if((player_two_selection == "rock" and player_one_selection == "scissors") 
or (player_two_selection == "paper" and player_one_selection == "rock")
or (player_two_selection ==  "scissors" and player_one_selection == "paper")):
    print("{0} beats {1} {2} Wins!".format(player_two_selection,player_one_selection,player_two))

