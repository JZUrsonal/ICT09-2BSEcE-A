class GradeManagementSystem():
    def __init__(self,student_id,name,course,grade1,grade2,grade3,grade4):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
        self.grade4 = grade4

students = []

def add_student():
    print("Student's Registration: \n")
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    course = input("Enter Student's Course: ")
    grade1 = float(input("Enter 1st Grade: "))
    grade2 = float(input("Enter 2nd Grade: "))
    grade3 = float(input("Enter 3rd Grade: "))
    grade4 = float(input("Enter 4th Grade: "))

    students.append(GradeManagementSystem(student_id,name,course,grade1,grade2,grade3,grade4))
    print("Student's Record Successfully Registered. \n")

def update_grade():
    print("Update Students' Grades\n")
    student_id = input("Enter Student ID to update: ")
    student = next((student for student in students if student.student_id == student_id), None)
    
    if student:
        print(f"Updating grades for {student.name} ({student.student_id})")
        student.grade1 = float(input("Enter new 1st Grade: "))
        student.grade2 = float(input("Enter new 2nd Grade: "))
        student.grade3 = float(input("Enter new 3rd Grade: "))
        student.grade4 = float(input("Enter new 4th Grade: "))
        print("Grades updated successfully!\n")
    else:
        print("Student ID not found!\n")


def display_records():
    if not students:
        print("No Student Record Found!")
        return
    for student in students:
        print(f'Name: {student.name}, Student ID: {student.student_id}, Course: {student.course}, 1st Grade: {student.grade1}, 2nd Grade: {student.grade2}, 3rd Grade: {student.grade3} , 4th Grade: {student.grade4}')
    print()


def calculate_grade():
    for student in students:
        average_grade = (student.grade1 + student.grade2 + student.grade3 + student.grade4) / 4
        print(f'Name: {student.name}, Student ID: {student.student_id}, Course: {student.course}, 1st Grade: {student.grade1}, 2nd Grade: {student.grade2}, 3rd Grade: {student.grade3} , 4th Grade: {student.grade4}, Average Grade: {average_grade}')
    print()



while True:
        print("Student Grade Management System\n")
        print("1. Add Student")
        print("2. Update Student's Grades")
        print("3. Display All Students' Records ")
        print("4. Calculate Grades for All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_grade()
        elif choice == "3":
            display_records()
        elif choice == "4":
            calculate_grade()
        elif choice == "5":
            print("Program has been shut down! Thank you!")
            break
        else:
            print("Invalid Choice. Please Try Again!\n")


