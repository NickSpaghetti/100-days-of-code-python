print("Welcome to the Generation Caluclator.")
birth_year = int(input("What year were you born?> "))
if(birth_year >= 1925 and birth_year <= 1946):
  print("You are a Traditionalist!")
elif(birth_year >= 1947 and birth_year <= 1964):
  print("You are a Baby Boomer")
elif(birth_year >= 1965 and birth_year <= 1981):
  print("You are a Generation X")
elif(birth_year >= 1965 and birth_year <= 1981):
  print("You are a Baby Boomer")
elif(birth_year >= 1982 and birth_year <= 1995):
  print("You are a Millenial")
elif(birth_year >= 1996 and birth_year <= 2015):
  print("You are a Generation Z")
else:
  print("looks like we dont have a generation for the year {0}".format(birth_year))
  