class TeacherAcademy:
    student_name = ""
    def display_teacher_report(self):
        print("Student under Teacher's notice")

class Student(TeacherAcademy):
    def display_student_report(self):
        print("and name is ", self.student_name)

student = Student()
student.student_name = "Shreesha Voniyadka"
student.display_teacher_report()
student.display_student_report()
