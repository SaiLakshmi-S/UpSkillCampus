import os

class Student:
    def __init__(self, name, roll, dept):
        self.name = name
        self.roll = roll
        self.dept = dept

    def __str__(self):
        return f"{self.name}, {self.roll}, {self.dept}"

class StudentManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    name, roll, dept = line.strip().split(", ")
                    self.students.append(Student(name, roll, dept))

    def save_students(self):
        with open(self.filename, 'w') as file:
            for student in self.students:
                file.write(str(student) + "\n")

    def add_student(self):
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        dept = input("Enter department: ")
        self.students.append(Student(name, roll, dept))
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        print("\nAll Students:")
        for student in self.students:
            print(student)

    def search_student(self):
        roll = input("Enter roll number to search: ")
        found = False
        for student in self.students:
            if student.roll == roll:
                print(f"Student Found: {student}")
                found = True
                break
        if not found:
            print("Student not found.")

    def delete_student(self):
        roll = input("Enter roll number to delete: ")
        for i, student in enumerate(self.students):
            if student.roll == roll:
                del self.students[i]
                print("Student deleted successfully.")
                return
        print("Student not found.")

    def menu(self):
        while True:
            print("\n--- Student Record System ---")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Save and Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                self.save_students()
                print("Records saved. Exiting...")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    manager = StudentManager()
    manager.menu()
