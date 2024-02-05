
import csv
import os
from postgres_handler import postgres_connect
class DBHandler:
    # from  import TextColors
    @classmethod
    def update_student(cls, student,data):
        
        command=''' 
         update student set first_name=(%s),last_name=(%s),academy=(%s),fee_paid=(%s),is_dropout=(%s),first_session_clear=(%s),second_session_clear=(%s)
         where id=(%s);
         
         
        '''
        corr,conn=postgres_connect()
        tuple1=(data['first_name'],data['last_name'],data['academy'],data['fee_paid'],data['is_dropout'],
                
                data['first_session_clear'],data['second_session_clear'],data['id']
                )
        
        corr.execute(command,tuple1)
        conn.commit()
        corr.close()
        conn.close()
        
        # # Read existing data from the file
        #     selected_student, index =cls.get_student(student)
        #     if selected_student:
        #             # Create the updated student data
        #             selected_student = {
        #                 "id": selected_student["id"],
        #                 "first_name": data.get("first_name",selected_student["first_name"]),
        #                 "last_name": data.get("last_name",selected_student["last_name"]),
        #                 "academy": data.get("academy",selected_student["academy"]),
        #                 "fee_paid": data.get("fee_paid", selected_student["fee_paid"]),
        #                 "is_dropout":data.get("is_dropout",selected_student["is_dropout"]),
        #                 "first_session_clear": data.get("first_session_clear",selected_student["first_session_clear"]),
        #                 "second_session_clear": data.get("second_session_clear",selected_student["second_session_clear"])
        #             }

        #             # Update the rows list with the modified data
        #             rows=[]
        #             with open("student.csv", 'r') as file:
        #                 reader = csv.DictReader(file)
        #                 rows = list(reader)
        #             rows[index] = selected_student

        #     if selected_student is not None:
        #         # Write the updated data back to the file
        #         with open("student.csv", "w", newline='') as file:
        #             fieldnames = ["id", "first_name", "last_name", "academy", "fee_paid", "is_dropout",
        #                         "first_session_clear", "second_session_clear"]
        #             writer = csv.DictWriter(file, fieldnames=fieldnames)
        #             writer.writeheader()
        #             writer.writerows(rows)
        #             return True
            
        #     return False

    @classmethod
    def check_enrollment_status(cls, firstname, lastname, academy):
        command=''''''
        # with open('student.csv', 'r') as file:
        #     reader = csv.DictReader(file)
        #     for student in reader:
        #         if (
        #             firstname == student["first_name"]
        #             and lastname == student["last_name"]
        #             and academy.id ==  student["academy"]
        #         ):
        #             # if int(student["fee_paid"]) == int(academy.fee):
        #             #     print(  "\n Student has already fully paid and cannot enroll again." )
        #             #     return True

        #             # print( "\n Student already enrolled! \n Please Join the Academy Again ......   " )
        #             # return False
        #             return True
        #     return False

    @staticmethod
    def get_student():
        
        command= '''
        select * from student
        '''
        corr,conn=postgres_connect()
        corr.execute(command)
        student=corr.fetchall()
        student_dict=()
        corr.close()
        conn.close()
        return student
        
        # with open("student.csv", 'r') as file:
        #     reader = csv.DictReader(file)
        #     rows = list(reader)

        #     for index, row in enumerate(rows):
        #         # if( student.firstname == row["first_name"]
        #         # and student.lastname == row["last_name"]
        #         # and student.academy.id == row["academy"]):
        #         if student.id==int(row['id']):
        #             return row, index
        #     print("could not get student from database ")


    @staticmethod
    def add_student_to_file(data):
        tuple1=(data['first_name'],data['last_name'],data['academy'],data['fee_paid'],data['is_dropout'],
                
                data['first_session_clear'],data['second_session_clear']
                )
        command='''
        INSERT into student (first_name,last_name,academy,fee_paid,is_dropout,first_session_clear,second_session_clear) values(%s,%s,%s,%s,%s,%s,%s);
        
        
        
        '''

        corr,conn=postgres_connect()
        corr.execute(command,tuple1)
        conn.commit()
        corr.close()
        conn.close()

        # is_file_empty = os.stat("student.csv").st_size == 0
        # has_header = not is_file_empty and  cls.has_csv_header()

        # with open("student.csv", 'a' if not (is_file_empty or has_header) else 'a', newline='') as file:
        #     writer = csv.writer(file)

        #     if not has_header:
        #         writer.writerow(data.keys())

        #     writer.writerow(data.values())

    @classmethod
    def has_csv_header(cls):
        with open("student.csv", 'r') as file:
            first_line = file.readline().strip()
            return first_line == "id,first_name,last_name,academy,fee_paid,is_dropout,first_session_clear,second_session_clear"


    @classmethod
    def get_fee_paid(cls, student):
        feepaid = 0
        with open('student.csv', 'r', newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                
                if int(row['id'])==student.id:   
                    feepaid = int(row["fee_paid"])
        return feepaid

    # def update_fee_paid(student, additional_fee):
    #     # Update the student's fee paid
    #     student.pay_fee(additional_fee)
    #     print(" Remaining fee paid. You can now start the next session.")

    #     # Recalculate remaining fee after user's input
    #     remaining_fee = max(0, int(student.academy.fee) - (get_fee_paid(student) + additional_fee))
    #     return remaining_fee


    # read academy data
    @classmethod
    def read_academy_data(cls):
        academies = []
        with open("academy.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                academies.append(row)
        return academies

    @classmethod
    def get_last_id(cls):
        with open('student.csv','r') as file:
            reader= list(csv.reader(file))
            last_row=reader[-1]
            return int(last_row[0])