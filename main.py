import json
import os

FILE_NAME = "students.json"


# Load students from JSON file
def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Student file contains invalid data.")
            return []

    return []


# Save students to JSON file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Add a new student
def add_student(students):
    student_id = input("Enter Student ID: ").strip()

    # Check whether ID already exists
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Student Name: ").strip()
    age = input("Enter Student Age: ").strip()
    course = input("Enter Course: ").strip()
    email = input("Enter Email: ").strip()

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "email": email
    }

    students.append(student)
    save_students(students)

    print("Student added successfully.")


# Display all students
def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for student in students:
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
        print(f"Email  : {student['email']}")
        print("-------------------------------------")


# Search student
def search_student(students):
    student_id = input("Enter Student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found")
            print("---------------------")
            print(f"ID     : {student['id']}")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")
            print(f"Email  : {student['email']}")
            return

    print("Student not found.")


# Update student
def update_student(students):
    student_id = input("Enter Student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:

            print("\nLeave a field blank to keep the old value.")

            name = input(f"Name ({student['name']}): ").strip()
            age = input(f"Age ({student['age']}): ").strip()
            course = input(f"Course ({student['course']}): ").strip()
            email = input(f"Email ({student['email']}): ").strip()

            if name:
                student["name"] = name

            if age:
                student["age"] = age

            if course:
                student["course"] = course

            if email:
                student["email"] = email

            save_students(students)

            print("Student updated successfully.")
            return

    print("Student not found.")


# Delete student
def delete_student(students):
    student_id = input("Enter Student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:

            students.remove(student)
            save_students(students)

            print("Student deleted successfully.")
            return

    print("Student not found.")


# Main program
def main():

    students = load_students()

    while True:

        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()