class Academy:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, student_id, name, academy):
        self.student_id = student_id
        self.name = name
        self.enrolled_academies = [academy]
        self.opted_out = False
        self.first_installment_paid = False
        self.second_installment_paid = False

class EnrollmentSystem:
    def __init__(self):
        self.academies = [Academy('Math Academy'), Academy('Science Academy')]
        self.students = []

    def enroll_student(self, student_id, name, academy_name):
        academy = next((a for a in self.academies if a.name == academy_name), None)
        if academy:
            new_student = Student(student_id, name, academy_name)
            self.students.append(new_student)
            print(f"{name} has successfully enrolled in {academy_name}.")
        else:
            print(f"Academy {academy_name} not found.")

    def opt_out_student(self, student_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.opted_out = True
            print(f"{student.name} has opted out.")
        else:
            print("Student not found.")

    def pay_fee(self, student_id, installment_number):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            if not student.opted_out:
                if installment_number == 1:
                    student.first_installment_paid = True
                    print(f"{student.name} has paid the first installment.")
                elif installment_number == 2:
                    student.second_installment_paid = True
                    print(f"{student.name} has paid the second installment.")
                else:
                    print("Invalid installment number.")
            else:
                print("Student has opted out and cannot pay fees.")
        else:
            print("Student not found.")
