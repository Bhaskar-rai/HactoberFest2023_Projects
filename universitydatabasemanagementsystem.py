class UniversityDatabase:
    def __init__(self):
        self.teachers = {}
        self.students = {}
        self.professors = {}

    def add_teacher(self, teacher_id, name, department):
        self.teachers[teacher_id] = {'name': name, 'department': department}

    def add_student(self, student_id, name, major):
        self.students[student_id] = {'name': name, 'major': major}

    def add_professor(self, professor_id, name, department):
        self.professors[professor_id] = {'name': name, 'department': department}

    def display_teachers(self):
        for teacher_id, teacher_info in self.teachers.items():
            print(f"Teacher ID: {teacher_id}, Name: {teacher_info['name']}, Department: {teacher_info['department']}")

    def display_students(self):
        for student_id, student_info in self.students.items():
            print(f"Student ID: {student_id}, Name: {student_info['name']}, Major: {student_info['major']}")

    def display_professors(self):
        for professor_id, professor_info in self.professors.items():
            print(f"Professor ID: {professor_id}, Name: {professor_info['name']}, Department: {professor_info['department']}")


def main():
    university_db = UniversityDatabase()

    while True:
        print("\nUniversity Database Management System")
        print("1. Add Teacher")
        print("2. Add Student")
        print("3. Add Professor")
        print("4. Display Teachers")
        print("5. Display Students")
        print("6. Display Professors")
        print("7. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            teacher_id = input("Enter Teacher ID: ")
            name = input("Enter Teacher Name: ")
            department = input("Enter Teacher Department: ")
            university_db.add_teacher(teacher_id, name, department)

        elif choice == '2':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            major = input("Enter Student Major: ")
            university_db.add_student(student_id, name, major)

        elif choice == '3':
            professor_id = input("Enter Professor ID: ")
            name = input("Enter Professor Name: ")
            department = input("Enter Professor Department: ")
            university_db.add_professor(professor_id, name, department)

        elif choice == '4':
            print("\nTeachers:")
            university_db.display_teachers()

        elif choice == '5':
            print("\nStudents:")
            university_db.display_students()

        elif choice == '6':
            print("\nProfessors:")
            university_db.display_professors()

        elif choice == '7':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
