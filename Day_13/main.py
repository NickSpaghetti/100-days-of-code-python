test_name = input("What is the name of this test?> ")
total_questions = int(input("How many questions were on this test?> "))
correct_questions = int(input("How many questions out of {0} did you get correct?>".format(total_questions)))
grade = (correct_questions/total_questions) * 100
letter_grade = ""
if(grade >= 90):
  letter_grade = "A+"
elif(grade >= 80 and grade <= 89):
    letter_grade = "A"
elif(grade >= 70 and grade <= 79):
    letter_grade = "B"
elif(grade >= 60 and grade <= 69):
    letter_grade = "C"
elif(grade >= 50 and grade <= 59):
    letter_grade = "D"
else:
    letter_grade = "U"

print("You scored a {0} which is a {1} on {2}".format(grade,letter_grade,test_name))

