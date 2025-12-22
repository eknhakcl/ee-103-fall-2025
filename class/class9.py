course1 = input("Enter course 1: ")
course2 = input("Enter course 2: ")
course3 = input("Enter course 3: ")
grade1 = int(input(f"Enter grade for {course1}: "))
grade2 = int(input(f"Enter grade for {course2}: "))
grade3 = int(input(f"Enter grade for {course3}: "))
grades = {course1: grade1, course2: grade2, course3: grade3}
grades
print(f"Number of courses: {len(grades)}")
print(f"Average grade: {sum(grades.values()) / len(grades):.2f}")
print(f"Highest grade: {max(grades.values())} Course: {max(grades, key=grades.get)}")