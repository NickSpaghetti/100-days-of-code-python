usn = input("UserName> ")
pwd = input("Password> ")

if(usn == "Ziggy"):
  if(pwd == "Cat"):
    print("Welcome Ziggy!")
  else:
    print("Wrong password")
elif(usn == "Will"):
  if(pwd == "Rudy"):
    print("Hello Mr Marriot")
  else:
    print("Wrong Password")
elif(usn == "Ridge"):
  if(pwd == "GURL"):
    print("Hello Micheal")
  else:
    print("invalid password")
else:
  print("None of these usn are in our system")