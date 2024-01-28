# Create a cli application where student can enroll in any academy.
# Student can opt out from that academy, student should be able to 
# pay their fee in two installments, once at the start of enrollment,
# second on the next session start. In next session of that particular student,
# show prompt to pay the remaining due, if not paid. Student can enroll in any academy. 
# Show the enrolled academy at the start of every new session. Use OOP approach.
# Use interactive user interface to interact in cli application.

#  Use csv files to read and write student's data.

import csv
class Student:
    # pass
    def __init__(self,sName,academy):
        self.id=1,
        self.student_name=sName
        self.academy=academy

        student_data={
        "id":self.id,
        "student_name": self.student_name,
        "academy":self.academy.id,
        "fee_paid":0


        }


        with open ("student.csv",'w',newline="") as file:
            writer=csv.writer(file)
            writer.writerow(student_data.keys())

            writer.writerow(student_data.values())

 
    

    def opt_out():
        print("I am out !! ")
        # add dropout flag on student row

        studentdata=[]
        with open("opt.csv",'w',newline="") as file:
            writer=csv.writer(file)
            writer.writerows(studentdata)


    def get_feepayment(self,fee):
        #save user fee in the database 
        list_of_data=[]
        with open("studentdata.csv",'w') as file:
            writer=csv.writer(file)
            for item in list_of_data:
                writer.writerows([item])

        
        if fee  < self.academy.fee:
            print("Pay second remaining due another installment")


            
         
        

class Academy:
    def __init__(self,name,academy_fee,course):
        self.id=1
        self.name=name
        self.fee=academy_fee
        self.course=course


    # academy file 
        data={
            "id":self.id,
            "name":self.name,
            "fee":self.fee,
            "course":self.course,

        }
        # fieldnames=['Name','fee','course']
        with open ("academy.csv",'w',newline="") as file:
            writer=csv.writer(file)
            writer.writerow(data.keys())

            writer.writerow(data.values())

        
    def start_session(self,student,is_next=False):
        if is_next :
#             # TODO: check if second installement is pending , if pending show the prompt
            with open('student.csv' ,'r',newline="") as file:
                reader=csv.reader(file)
                for row in reader:
                    if row[1]==student.student_name and row[2]==self.id:
                        feepaid=row[3]
        
            if feepaid < self.fee:
                print("You should pay second installment in the next session ")
                


#          with open("studentdata.csv",'r') as sfile:
#              reader=csv.reader(sfile)
#              next(reader)   
#             #  skip the header
#              for row in reader:
#                 academy_name,fee,course_academy=row
#                 fee=int(fee)

    
# class Session:
#     def __init__(self,academy,is_next=False):
#         if is_next :
#             # TODO: check if second installement is pending , if pending show the prompt
#          with open("studentdata.csv",'r') as sfile:
#              reader=csv.reader(sfile)
#              next(reader)   
#             #  skip the header
#              for row in reader:
#                 academy_name,fee,course_academy=row
#                 fee=int(fee)

#         #TODO: show academy information 


        


academy=Academy("Dima Academy",4000,"Officer Cadet")
print(vars(academy))

student=Student("Rmaesh",academy)
print(vars(student))




# obj3=Session("first session")
# print(vars(obj3))

# print(obj.get_enrollement())
# print(obj.get_feepayment())





