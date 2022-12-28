myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip_percent = int(input("What is the % do you want to give as a tip"))
tip_percent *= 0.01
answer = round(((myBill * tip_percent) + myBill) / numberOfPeople,2)
print("You all owe",answer)