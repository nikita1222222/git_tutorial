#Create a dictionary where the keys are student names and the values are their grades.
#Add a new student and grade.
#Update an existing student's grade.
#Print all student grades.

students = {
    "Savi" : 89,
    "Prasad" : 67,
    "Indra" : 78,
    "Rani" : 43,
    "Satya" : 59
}

print(students)

#Add a new student and grade

new_student = {input("Enter new student name ") : int(input("Enter grade " ))}  #enter manually name and grade
students.update(new_student)

print(students)

#Update an existing student's grade.
students["Rani"]= 76

#Print all student grades.
print(students)
