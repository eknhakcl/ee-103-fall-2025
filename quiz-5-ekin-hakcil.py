std_name = input("Enter student name: ")
std_dept = input("Enter department: ")
std_gpa = float(input("Enter GPA: "))
std_id = int(input("Enter student ID: "))

student_info = {
    "name": std_name,
    "department": std_dept,
    "GPA": std_gpa, 
    "ID": std_id
}
def describe_student(info_dict) :
    return f"Student {info_dict['name']} from {info_dict['department']} has a GPA of {info_dict['GPA']:.2f} and ID: {info_dict['ID']}."

print(describe_student(student_info))
