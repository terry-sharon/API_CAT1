class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {self.name}.")

    def display_grades(self):
        if self.assignments:
            print(f"Grades for {self.name}:")
            for assignment, grade in self.assignments.items():
                print(f" - {assignment}: {grade}")
        else:
            print(f"No grades recorded for {self.name}.")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to the course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"Student with ID {student_id} not found.")

    def display_all_students_grades(self):
        if self.students:
            print(f"All students' grades for the course '{self.course_name}':")
            for student in self.students:
                student.display_grades()
        else:
            print("No students in the course.")

# Interactive code for adding students and assigning grades
if __name__ == "__main__":
    # Initialize instructor and course
    instructor = Instructor("Samuel", "BBIT")

    while True:
        print("\nCourse Management System")
        print("1. Add a student")
        print("2. Assign a grade to a student")
        print("3. Display all students' grades")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            # Add a student
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            new_student = Student(name, student_id)
            instructor.add_student(new_student)

        elif choice == '2':
            # Assign a grade
            student_id = input("Enter student ID: ")
            assignment_name = input("Enter assignment name: ")
            try:
                grade = float(input("Enter grade: "))
                instructor.assign_grade(student_id, assignment_name, grade)
            except ValueError:
                print("Invalid grade. Please enter a number.")

        elif choice == '3':
            # Display all students' grades
            instructor.display_all_students_grades()

        elif choice == '4':
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.") 

 