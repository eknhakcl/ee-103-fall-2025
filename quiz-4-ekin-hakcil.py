def create_student(name,age):
    student_tuple = (name,age)
    return student_tuple

def describe_student(student_tuple):
    name = student_tuple[0]
    age = student_tuple[1]
    description = f"Student {name} is {age} years old."
    return description

name = input("Enter the student's name: ")
age = int(input("Enter the student's age: "))

student = create_student(name, age)
description = describe_student(student)
print(description)