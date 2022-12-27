print("Inidal D Fan Question quiz!")
question = input("Do you like Inital D> ")
if question.lower() == "yes":
  make = input("Do you know what make of an AE86? ")
  if make.lower() == "toyota":
    print("You got it.")
    rx7 = input("What is the chassie code of the Rx7 FD> ")
    if(rx7.lower() == "fd3s"):
      print("YOU GOT IT!")
    elif rx7.lower() == "fc3s":
      print("So close thats the FC")
    else:
      print("Guess you are not a super fan")
  else: 
    print("No it is not a {0}".format(make))
else:
  print("Guess you don't.")