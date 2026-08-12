# **Student Management System**

A simple **command-line Student Management System built with Python** that allows users to create, view, search, update, and delete student records. The application uses **JSON file handling** to store student information permanently.

---

## **Project Overview**

The Student Management System is a menu-driven Python application designed to manage student records efficiently.

The system allows the user to perform basic **CRUD operations**:

- **Create** — Add a new student
- **Read** — View and search student records
- **Update** — Modify existing student information
- **Delete** — Remove a student record

Student data is stored in a `students.json` file, so records remain available even after the program is closed.

---

## **Objectives**

- Develop a menu-driven Python application.
- Implement CRUD operations.
- Practice Python functions and data structures.
- Store and retrieve data using JSON.
- Implement file handling.
- Implement basic error handling.
- Develop practical problem-solving and programming skills.

---

## **Features**

### **1. Add Student**
Allows the user to add a new student with:
- Student ID
- Student Name
- Age
- Course
- Email

### **2. View Students**
Displays all stored student records.

### **3. Search Student**
Allows the user to search for a student using their Student ID.

### **4. Update Student**
Allows the user to update:
- Name
- Age
- Course
- Email

The user can leave a field blank to keep its previous value.

### **5. Delete Student**
Allows the user to delete a student record using the Student ID.

### **6. Data Persistence**
Student records are saved in a JSON file and remain available when the program is restarted.

### **7. Error Handling**
The program handles situations such as:
- Duplicate Student ID
- Student not found
- Invalid JSON data
- Empty student records
- Invalid menu choice

---

## **Technologies Used**

- **Python 3**
- **JSON**
- **File Handling**
- **Lists and Dictionaries**
- **Command-Line Interface (CLI)**

---

## **Python Concepts Used**

### **Functions**
Separate functions are created for different operations:

```python
add_student()
view_students()
search_student()
update_student()
delete_student()
```

### **Lists**
A list is used to store multiple student records.

```python
students = []
```

### **Dictionaries**
Each student is represented using a dictionary:

```python
student = {
    "id": student_id,
    "name": name,
    "age": age,
    "course": course,
    "email": email
}
```

### **File Handling**
Python's `open()` function is used to read and write the JSON file.

### **JSON**
The `json` module is used to store structured student information.

```python
json.load()
json.dump()
```

### **Exception Handling**
`try-except` is used to handle invalid JSON data and prevent unexpected program termination.

### **Loops**
A `while` loop keeps the main menu running until the user chooses Exit.

### **Conditional Statements**
`if`, `elif`, and `else` are used to process the user's menu choice.

---

## **CRUD Operations**

| Operation | Project Function | Purpose |
|---|---|---|
| **Create** | `add_student()` | Add a student |
| **Read** | `view_students()` | Display students |
| **Read** | `search_student()` | Search student |
| **Update** | `update_student()` | Modify student |
| **Delete** | `delete_student()` | Remove student |

---

## **Project Structure**

```text
Student-Management-System/
│
├── main.py
├── students.json
├── README.md
├── requirements.txt
└── screenshots/
```

### **`main.py`**
Contains the complete Python program.

### **`students.json`**
Stores student records permanently.

### **`README.md`**
Contains project documentation.

### **`requirements.txt`**
This project uses only Python's built-in modules, so no external packages are required.

### **`screenshots/`**
Can be used to store screenshots of the program output.

---

## **How to Run the Project**

### **Step 1: Install Python**

Make sure Python 3 is installed.

```bash
python --version
```

### **Step 2: Clone the Repository**

```bash
git clone https://github.com/your-username/Student-Management-System.git
```

### **Step 3: Open the Project Folder**

```bash
cd Student-Management-System
```

### **Step 4: Run the Program**

```bash
python main.py
```

---

## **Sample Output**

```text
========== STUDENT MANAGEMENT SYSTEM ==========
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

Enter your choice: 1

Enter Student ID: 101
Enter Student Name: Rahul
Enter Student Age: 20
Enter Course: B.Tech CSE-AI
Enter Email: rahul@gmail.com

Student added successfully.
```

### **View Student**

```text
Enter your choice: 2

========== STUDENT RECORDS ==========

ID     : 101
Name   : Rahul
Age    : 20
Course : B.Tech CSE-AI
Email  : rahul@gmail.com
-------------------------------------
```

### **Search Student**

```text
Enter your choice: 3

Enter Student ID to search: 101

Student Found
---------------------
ID     : 101
Name   : Rahul
Age    : 20
Course : B.Tech CSE-AI
Email  : rahul@gmail.com
```

### **Update Student**

```text
Enter your choice: 4

Enter Student ID to update: 101

Leave a field blank to keep the old value.

Name (Rahul): Rahul Patel
Age (20):
Course (B.Tech CSE-AI):
Email (rahul@gmail.com):

Student updated successfully.
```

### **Delete Student**

```text
Enter your choice: 5

Enter Student ID to delete: 101

Student deleted successfully.
```

---

## **Data Storage**

The project stores student records in `students.json`.

Example:

```json
[
    {
        "id": "101",
        "name": "Rahul",
        "age": "20",
        "course": "B.Tech CSE-AI",
        "email": "rahul@gmail.com"
    }
]
```

Using JSON makes the data:
- Easy to read
- Easy to modify
- Easy to store
- Easy to retrieve using Python

---

## **Error Handling**

The application includes basic error handling.

### **Duplicate Student ID**

```text
Student ID already exists.
```

### **Student Not Found**

```text
Student not found.
```

### **Invalid Menu Choice**

```text
Invalid choice. Please try again.
```

### **Invalid JSON File**

```text
Error: Student file contains invalid data.
```

These checks make the application more reliable and user-friendly.

---

## **Program Flow**

```text
Start
  ↓
Load students.json
  ↓
Display Menu
  ↓
Choose Operation
  ↓
Add / View / Search / Update / Delete
  ↓
Save Changes to JSON
  ↓
Return to Menu
  ↓
Exit
  ↓
End
```

---

## **Learning Outcomes**

By completing this project, I strengthened my understanding of:

- Python programming fundamentals
- Functions
- Lists and dictionaries
- File handling
- JSON data storage
- CRUD operations
- Exception handling
- User input handling
- Menu-driven applications
- Persistent data storage
- Problem-solving and logical thinking

---

## **Future Enhancements**

The project can be further improved by adding:

- Admin login and authentication
- SQLite/MySQL database
- Marks and grade management
- Attendance management
- Advanced student search
- Student report generation
- Tkinter graphical interface
- Flask web interface
- Password-based authentication
- Student performance analytics

---

## **Why I Built This Project**

I developed this project to strengthen my practical Python programming skills and understand how basic data management systems work.

It helped me apply concepts such as **CRUD operations, file handling, JSON, functions, loops, dictionaries, and error handling** in a practical application.

---

## **Project Information**

| Category | Details |
|---|---|
| **Project Level** | Beginner → Intermediate |
| **Project Type** | Command-Line Application |
| **Language** | Python |
| **Data Storage** | JSON |

---

## **Author**

**Kanan**  
B.Tech Computer Science & Engineering – AI Student

Interested in Python Programming, Software Development, Artificial Intelligence, and Problem Solving.

---

## **Acknowledgement**

I would like to express my sincere gratitude to everyone who supported and guided me during the development of this project.

This project provided me with valuable hands-on experience in Python programming and helped me improve my understanding of file handling, CRUD operations, JSON data management, and problem-solving.

I look forward to continuing to learn and develop more practical and innovative software projects.

---

## **Support**

If you find this project useful, consider giving the repository a **star ⭐** on GitHub.

Thank you for visiting this project!
