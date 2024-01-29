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
        "fee_paid":0,
        "is_dropout":False
        }

        with open ("student.csv",'w',newline="") as file:
            writer=csv.writer(file)
            writer.writerow(student_data.keys())

            writer.writerow(student_data.values())

    
    def opt_out(self):

        # this action required 

        # studentdata=[]
        # with open("opt.csv",'w',newline="") as file:
        #     writer=csv.writer(file)
        #     writer.writerows(studentdata)
        selected_student=None
        with open("student.csv",'r') as file:
            reader=csv.reader(file)
            for row in reader:
                if self.student_name==row[1] and self.academy.id==row[2]:
                    selected_student={
                        "id":row[0],
                        "student_name":row[1],
                        "academy":row[2],
                        "fee_paid":row[3],
                        "is_dropout":True
                    }

        with open("student.csv","a") as file:
            fieldnames=["id","student_name","academy","fee_paid","is_dropout"]
            writer=csv.DictWriter(file,fieldnames=fieldnames)

            if selected_student is not None:
                writer.writeheader
                writer.writerow(selected_student)
                print("You are opt out !")
            




    def pay_fee(self,fee):
        student_data=None
        import csv

        updated_row= None
        with open("student.csv",'r') as file:
            reader=csv.reader(file)
            for row in reader:
                if self.student_name == row[1] and self.academy.id == row[2]:
                    updated_row = {
                        "id": row[0],
                        "student_name": row[1],
                        "academy": row[2],
                        "fee_paid": fee,
                        "is_dropout":row[4]
                    }
        with open('student.csv', 'a', newline='') as csvfile:
            fieldnames = ["id", "student_name", "academy", "fee_paid","is_dropout"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if updated_row is not None:

                writer.writeheader()

                writer.writerow(updated_row)
                print("Fee has been paid")
                

                if fee  < int(self.academy.fee):
                    print("Pay second remaining due another installment")                   
        
class Academy:
    def __init__(self,id,name,academy_fee,course):
        self.id=id
        self.name=name
        self.fee=academy_fee
        self.course=course


    # academy file 
        # data={
        #     "id":self.id,
        #     "name":self.name,
        #     "fee":self.fee,
        #     "course":self.course,

        # }
        # # fieldnames=['Name','fee','course']
        # with open ("academy.csv",'w',newline="") as file:
        #     writer=csv.writer(file)
        #     writer.writerow(data.keys())

        #     writer.writerow(data.values())

        
    def start_session(self,student,is_next=False):
        print("Starting new session ")

        print(f"Academy Name: {self.name}")    
        print(f"Course Name: {self.course}")

        if is_next :
            feepaid=0
#             #check if second installement is pending , if pending show the prompt
            with open('student.csv' ,'r',newline="") as file:
                reader=csv.reader(file)
                for row in reader:
                    if row[1]==student.student_name and row[2]==self.id:
                        feepaid=row[3]
        
            if feepaid < self.fee:
                print("please pay remaining installment fee")
                


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


        


# academy=Academy("Dima Academy",4000,"Officer Cadet")

# student=Student("Rmaesh",academy)

# student.pay_fee(1000)

if __name__=="__main__":

    name=input("Enter your Name: ")
    print("Please select the academy you want to join !")
    
    with open ("academy.csv" , 'r') as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            print(row[0],row[1])

        choice=int(input())
        academy=None
        with open ("academy.csv" , 'r') as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if int(row[0])==choice:

                    academy=Academy(row[0],row[1],row[2],row[3])
        student=Student(name,academy)

        print(f"Total fee is {academy.fee}")
        print("How much do youj want pay now ?")
        fee=int(input())
        
        student.pay_fee(fee)
        choice=int(input("Do you want to start next session(1) or opt out(2)?"))
        if choice ==2:
            student.opt_out()
        elif choice==1:
            academy.start_session(student,is_next=True)
        
        

        






