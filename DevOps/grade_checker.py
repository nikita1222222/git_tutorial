#Take a score as input and print the grade based on the following:


score = int(input("Enter your numbers \n"))
print(type(score))

if score >=90 :
    grade = "A"

elif score >=80 and score <=89:
    grade = "B"

elif score >=70 and score <=79:
    grade = "C"

elif score >=60 and score <=69:
    grade = "D"

else :
     grade = "F"


print("Your Grade is " + grade)