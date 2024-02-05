# import csv
# import os
# class DBHandler:
    
#     @classmethod
#     def update_student(cls, student,data):
        
#             selected_student, index =cls.get_student(student)
#             if selected_student:
#                     selected_student = {
#                         "id": selected_student["id"],
#                         "first_name": data.get("first_name",selected_student["first_name"]),
#                         "last_name": data.get("last_name",selected_student["last_name"]),
#                         "academy": data.get("academy",selected_student["academy"]),
#                         "fee_paid": data.get("fee_paid", selected_student["fee_paid"]),
#                         "is_dropout":data.get("is_dropout",selected_student["is_dropout"]),
#                         "first_session_clear": data.get("first_session_clear",selected_student["first_session_clear"]),
#                         "second_session_clear": data.get("second_session_clear",selected_student["second_session_clear"])
#                     }

#                     # Update the rows list with the modified data
#                     rows=[]
#                     with open("student.csv", 'r') as file:
#                         reader = csv.DictReader(file)
#                         rows = list(reader)
#                     rows[index] = selected_student

#             if selected_student is not None:
#                 # Write the updated data back to the file
#                 with open("student.csv", "w", newline='') as file:
#                     fieldnames = ["id", "first_name", "last_name", "academy", "fee_paid", "is_dropout",
#                                 "first_session_clear", "second_session_clear"]
#                     writer = csv.DictWriter(file, fieldnames=fieldnames)
#                     writer.writeheader()
#                     writer.writerows(rows)
#                     return True
            
#             return False

#     def check_enrollment_status(self,firstname,lastname,academy):
#         with open('student.csv', 'r') as file:
#             reader = csv.DictReader(file)
#             for student in reader:
#                 if (
#                     firstname == student["first_name"]
#                     and lastname == student["last_name"]
#                     and academy.id ==  student["academy"]
#                 ):
                  
#                     return True
#             return False

    
#     def get_student(self, student):
#         with open("student.csv", 'r') as file:
#             reader = csv.DictReader(file)
#             rows = list(reader)

#             for index, row in enumerate(rows):
               
#                 if student.id==int(row['id']):
#                     return row, index
#             print("could not get student from database ")


#     def add_student_to_file(self,student,data):
        
#         is_file_empty = os.stat("student.csv").st_size == 0
#         has_header = not is_file_empty and  self.has_csv_header()

#         with open("student.csv", 'a' if not (is_file_empty or has_header) else 'a', newline='') as file:
#             writer = csv.writer(file)

#             if not has_header:
#                 writer.writerow(data.keys())

#             writer.writerow(data.values())

#     # @staticmethod
#     def has_csv_header(self):
#         with open("student.csv", 'r') as file:
#             first_line = file.readline().strip()
#             return first_line == "id,first_name,last_name,academy,fee_paid,is_dropout,first_session_clear,second_session_clear"


#     @staticmethod
#     def get_fee_paid(student):
#         feepaid = 0
#         with open('student.csv', 'r', newline="") as file:
#             reader = csv.DictReader(file)
#             for row in reader:
                
#                 if int(row['id'])==student.id:   
#                     feepaid = int(row["fee_paid"])
#         return feepaid

#     @staticmethod
#     def read_academy_data():
#         academies = []
#         with open("academy.csv", 'r') as file:
#             reader = csv.reader(file)
#             next(reader)
#             for row in reader:
#                 academies.append(row)
#         return academies

#     @staticmethod
#     def get_last_id():
#         with open('student.csv','r') as file:
#             reader= list(csv.reader(file))
#             last_row=reader[-1]
#             return int(last_row[0])
    
  