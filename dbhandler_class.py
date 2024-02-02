# import csv
# import os

# class Student:
#     def __init__(self,id,first_name,last_name,academy,fee_paid,is_dropout,first_session_clear,second_session_clear):
#         self.id=id
#         self.first_name=first_name
#         self.last_name=last_name
#         self.academy=academy
#         self.fee_paid=fee_paid
#         self.is_dropout=is_dropout
#         self.first_session_clear=first_session_clear
#         self.second_session_clear=second_session_clear
        
        
# class Academy:
#     def __init__(self,id,fee):
#         self.id=id
#         self.fee=fee
        
# class CsvDatabase:
#     FILENAME="student.csv"
# # we dont ned to instance to perform the task right

#     @staticmethod
#     def read_csv(filename):
#         students=[]
#         with open(filename,'r') as file:
#             reader=csv.DictReader(file)
#             for row in reader:
#                 students.append(Student(**row))
#             return students
        
        
#     @staticmethod   
#     def write_csv(students,filename=FILENAME):
#         with open(filename,'w',newline='')as file:
#             fieldnames=["id", "first_name", "last_name", "academy", "fee_paid", "is_dropout",
#                             "first_session_clear", "second_session_clear"]
#             writer=csv.DictWriter(file,fieldnames=fieldnames)
#             writer.writeheader()
#             for student in students:
#                 writer.writerow(vars(student)) 
                
#     @staticmethod
#     def update_student(students,student,data):
#         selected_student,index= CsvDatabase.get_student(students,student)
#         if selected_student:
#             selected_student.__dict__.update({k: v for k, v in data.items() if v})
#             students[index] = selected_student
#             return True
#         return False      
    
#     @staticmethod
#     def get_student(students, student):
#         for index, s in enumerate(students):
#             if s.first_name == student.first_name and s.last_name == student.last_name and s.academy == student.academy.id:
#                 return s, index
#         return None, None
          
#     @staticmethod
#     def check_enrollment_status(students, firstname, lastname, academy):
#         for student in students:
#             if (
#                 firstname == student.first_name
#                 and lastname == student.last_name
#                 and academy.id == student.academy
#             ):
#                 if int(student.fee_paid) == int(academy.fee):
#                     print("\n Student has already fully paid and cannot enroll again.")
#                     return True

#                 print("\n Student already enrolled! \n Please Join the Academy Again ......   ")
#                 return False

#     @staticmethod
#     def add_student(students, student):
#         students.append(student)

#     @staticmethod
#     def get_fee_paid(students, student):
#         for s in students:
#             if s.first_name == student.first_name and s.last_name == student.last_name and s.academy == str(student.academy.id):
#                 return int(s.fee_paid)
#         return 0

#     @staticmethod
#     def update_fee_paid(students, student, additional_fee):
#         fee_paid = CsvDatabase.get_fee_paid(students, student)
#         remaining_fee = max(0, int(student.academy.fee) - (fee_paid + additional_fee))
#         return remaining_fee


                
                
                
    
        