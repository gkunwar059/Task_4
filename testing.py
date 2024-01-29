# Create a cli application where student can enroll in any academy.
# Student can opt out from that academy, student should be able to 
# pay their fee in two installments, once at the start of enrollment,
# second on the next session start. In next session of that particular student,
# show prompt to pay the remaining due, if not paid. Student can enroll in any academy. 
# Show the enrolled academy at the start of every new session. Use OOP approach.
# Use interactive user interface to interact in cli application.

#  Use csv files to read and write student's data.
# ANSI escape codes for text colors
import os

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class TextColors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'  # Reset to default color

# ASCII art for your CLI application
ascii_art = """
                                                !!!  WELCOME TO CLI APPLICATION  !!!
"""

# Print ASCII art in a specific color
clear_screen()
# print(TextColors.BLUE + ascii_art + TextColors.RESET)

print(TextColors.BLUE + ascii_art + TextColors.RESET)

# Rest of your CLI application code
# ...

import csv


class Student:  
    # pass
    def __init__(self,first_name,last_name,academy):
        self.id=1
        self.firstname=first_name
        self.lastname=last_name

        self.academy=academy

        student_data={
        "id":self.id,
        "first_name": self.firstname,
        "last_name":self.lastname,
        "academy":self.academy.id,
        "fee_paid":0,
        "is_dropout":False
        }

# initialized student_data write into a csv file 
# student.csv: Used to store data related to students. The columns include id, student_name, academy, fee_paid, and is_dropout.
        with open ("student.csv",'w',newline="") as file:
            writer=csv.writer(file)
            writer.writerow(student_data.keys())
            writer.writerow(student_data.values())

    

    # Reads the student.csv file to find the student matching the given name and academy.
    def opt_out(self):

        selected_student=None
        with open("student.csv",'r') as file:
            reader=csv.reader(file)
            for row in reader:
                if self.firstname==row[1] and self.lastname==row[2] and self.academy.id==row[3]:
                    selected_student={
                        "id":row[0],
                        "first_name":row[1],
                        "last_name":row[2],
                        "academy":row[3],
                        "fee_paid":row[4],
                        "is_dropout":True
                    }


# If found, updates the student's status to dropout and writes it back to the file.
        with open("student.csv","a") as file:
            fieldnames=["id","first_name","last_name","academy","fee_paid","is_dropout"]
            writer=csv.DictWriter(file,fieldnames=fieldnames)

            if selected_student is not None:
                if file.tell()==0:
                    writer.writeheader()
                writer.writerow(selected_student)
                print(TextColors.RED +"\n You are opt out ! "+TextColors.RESET )
            


# 

    def pay_fee(self,fee):
        student_data=None
# read the student.csv file to find student matching to the academy 
        
        updated_row= None
        with open("student.csv",'r') as file:
            reader=csv.reader(file)
            for row in reader:
                if self.firstname == row[1] and self.lastname==row[2] and self.academy.id == row[3]:
                    updated_row = {
                        "id": row[0],
                        "first_name": row[1],
                        "last_name":row[2],
                        "academy": row[3],
                        # update the paid_fee with the updated fee
                        "fee_paid": fee,
                        "is_dropout":row[5]
                    }
        with open('student.csv', 'a', newline='') as csvfile:
            fieldnames = ["id", "first_name","last_name", "academy", "fee_paid","is_dropout"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


            if updated_row is not None:
                if csvfile.tell()==0:

                    writer.writeheader()

                writer.writerow(updated_row)
                print(TextColors.GREEN +"\n Fee has been paid"+TextColors.RESET )
                
# check if the fee paid is less then total fee then show the pompt student to pay the remaining installment
                if fee  < int(self.academy.fee):
                    print("\n Pay second remaining due another installment")  
                    
                else:
                    print("\n You send more money ! Inform office to refund")
            # else:
            #     print("YOu God refund money !")
                                        
        
class Academy:
    def __init__(self,id,name,academy_fee,course):
        self.id=id
        self.name=name
        self.fee=academy_fee
        self.course=course


        # method start_session to begain a new session,checking if the student has paid the full fee
    def start_session(self,student,is_next=False):
        print("\n Starting new session ")
# print academic and course information 
        print(TextColors.YELLOW+f" \n Academy Name: {self.name}"+TextColors.RESET )   
        print(TextColors.YELLOW+f"\n Course Name: {self.course}"+TextColors.RESET)

# is_next flag is True if the installement of the fee is done otherwise prompt above remaining file
        if is_next :
            feepaid=0
#             #check if second installement is pending , if pending show the prompt
            with open('student.csv' ,'r',newline="") as file:
                reader=csv.reader(file)
                for row in reader:
                    if row[1]==student.firstname and row[2]==student.lastname and row[3]==self.id:
                        feepaid=row[4]
        
            if feepaid <self.fee:
                print(TextColors.RED +"\n Please pay remaining installment fee"+TextColors.RESET )
  
                



if __name__=="__main__":

    name=input(TextColors.GREEN +" \n  Enter your Name: "+TextColors.RESET )
    print(TextColors.BLUE+"\n  Please select the academy you want to join !"+TextColors.RESET)
    # academy.csv: Used to store data related to academies. The columns include id, name, fee, and course.
    # Accepts the student's name and displays a list of academies to choose from (academy.csv).
    # 
    with open ("academy.csv" , 'r') as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            print(row[0],row[1])

        choice=int(input(TextColors.YELLOW+"\n  Enter the number to join the academy  :"+TextColors.RESET))
        academy=None
        
        with open ("academy.csv" , 'r') as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if int(row[0])==choice:

                    academy=Academy(row[0],row[1],row[2],row[3])
        first_name,last_name=name.split(' ')            
        student=Student(first_name,last_name,academy)

        print(f"\n Total enrollment Fee: {academy.fee}")
        print("\n How much do you want pay now ?")
        fee=int(input(TextColors.YELLOW +'\n Enter the amount:'+TextColors.RESET))
        
        student.pay_fee(fee)
        choice=int(input(TextColors.BLUE+"\n  Do you want to start next session(1) or opt out(2)?" + TextColors.RESET))
        # If opting out, calls the opt_out method.
        if choice ==2:
            student.opt_out()
            # If starting the next session, calls the start_session method.
        elif choice==1:
            academy.start_session(student,is_next=True)
        
        

        






