print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as you can!")
print()

counter = 1
while True:
  lyrics = input("""Never _____ give you up
                    Never _____ let you down
                    Never _____ run around and desert you
                    Never _____ make you cry
                    Never _____ say goodbye
                    Never _____ tell a lie and hurt you""").lower()
  if lyrics == "gonna":
    print("You got it!")
    break
  else:
    print("Nope! Try again!")
    counter +=1
    
print("Thanks for playing!")

print("You got the correct lyrics in", counter, "attempt(s).")