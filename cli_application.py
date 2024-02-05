import csv
import os
import sys
from postgres_database import DBHandler
class TextColors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'


class Student:

    def __init__(self, first_name, last_name, academy):
        try:
            id=DBHandler.get_last_id()
        except ValueError :
            id=0
        self.id =id +1
        self.firstname = first_name
        self.lastname = last_name
        self.academy = academy
        already_enrolled = self.check_enrollment_status()
        print(already_enrolled)
    
        if already_enrolled:
            choice=int(input("Student already enrolled.Do you want to join again? [1]Yes [2]No"))
            if choice==1:
                pass
            elif choice==2:
                sys.exit()
            else:
                print("Invalid Choice ")

        student_data = {
            "id": self.id,
            "first_name": self.firstname,
            "last_name": self.lastname,
            "academy": self.academy.id,
            "fee_paid": 0,
            "is_dropout": False,
            "first_session_clear": False,
            "second_session_clear": False
        }
        DBHandler.add_student_to_file(student_data)



    def opt_out(self):
        if DBHandler.update_student(self,{"is_dropout":True,"first_session_clear": False, "second_session_clear": False}):
            print(TextColors.RED + "\n You are opted out!" + TextColors.RESET)

        else:
            print(TextColors.RED + "\n Student not found for opt-out." + TextColors.RESET)


    def check_enrollment_status(self):
        return DBHandler.check_enrollment_status(self.firstname, self.lastname, self.academy)



    def pay_fee(self, fee):
                   
            student, _=DBHandler.get_student()
            total_payed_fee = fee + int(student["fee_paid"])
            if not (DBHandler.update_student(self,{"fee_paid": total_payed_fee,"first_session_clear":True if student["first_session_clear"] == "False" else student["first_session_clear"],"second_session_clear":True if student["second_session_clear"] == "False" and student["first_session_clear"]=='True' else False})):
                print("Couldnot pay your fee ,,")
            

            if total_payed_fee < int(self.academy.fee):
                remaining_fee = int(self.academy.fee) - fee
                print(f"\n You need to pay the remaining installment of {remaining_fee}")
            elif total_payed_fee == int(self.academy.fee):
                print("\n Total Fee Paid ")
            else:
                over_payment = total_payed_fee - int(self.academy.fee)
                print(f"You sent more money {over_payment}, Please contact the office!")
                
                
class Academy:
    def __init__(self, id, name, academy_fee, course):
        self.id = id
        self.name = name
        self.fee = academy_fee
        self.course = course
        
        
    def start_session(self, student, is_next=False):
        print("\n Starting new session ")
        print(TextColors.YELLOW + f" \n Academy Name: {self.name}" + TextColors.RESET)
        print(TextColors.YELLOW + f"\n Course Name: {self.course}" + TextColors.RESET)
        additional_fee = 0
        if is_next:
            remaining_fee = max(0, int(self.fee) - DBHandler.get_fee_paid(student))

            while remaining_fee > 0:
                print(TextColors.YELLOW + f"\n Remaining Fee for the next session: {remaining_fee}" + TextColors.RESET)

                additional_fee = int(input(TextColors.BLUE + "\n Enter the amount to pay the remaining fee: " + TextColors.RESET))

                if additional_fee > remaining_fee:
                    print(TextColors.RED + "You entered more than the remaining fee. Please try again." + TextColors.RESET)
                elif additional_fee < remaining_fee:
                    print(TextColors.RED + "You entered less than the remaining fee. Please try again." + TextColors.RESET)
                else:
                    student.pay_fee(additional_fee)
                    print(TextColors.GREEN + "\n Remaining fee paid. You can now start the next session." + TextColors.RESET)

            else:
                print(TextColors.GREEN + "\n No remaining fee. Your fees are up to date." + TextColors.RESET)

            overpayment = max(0, DBHandler.get_fee_paid(student) - additional_fee - int(self.fee))
            if overpayment > 0:
                print(TextColors.YELLOW + f"\n You have overpaid by {overpayment}. Please collect your overpaid amount." + TextColors.RESET)

  

if __name__ == "__main__":
    name = input(TextColors.GREEN + "\t \t \n Enter your Name: " + TextColors.RESET)
    print(TextColors.BLUE + "\n Please select the academy you want to join!" + TextColors.RESET)

    academies = DBHandler.read_academy_data()

    for idx, row in enumerate(academies, start=1):
        print(f" {row[0]} {row[1]} {row[2]} {row[3]}")

    while True:
        try:
            choice = int(input(TextColors.YELLOW + "\n Enter the number to join the academy: " + TextColors.RESET))
            academy = next((Academy(row[0], row[1], row[2], row[3]) for row in academies if int(row[0]) == choice), None)
            if academy:
                
                break
            print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number to join!")

    first_name, last_name = name.split(' ')
    student = Student(first_name, last_name, academy)

    print(f"\n Total enrollment Fee: {academy.fee}")
    print("\n How much do you want to pay now?")

    while True:
        try:
            fee = int(input(TextColors.YELLOW + "\n Enter the amount: " + TextColors.RESET))
            break
        except ValueError:
            print("Please enter a valid amount!")

    student.pay_fee(fee)

    while True:
        try:
            choice = int(input(TextColors.BLUE + "\n Do you want to start the next session(1) or opt out(2)?"
                               + TextColors.RESET))
            break
        except ValueError:
            print("Please choose 1 or 2!")

    if choice == 2:
        student.opt_out()
    elif choice == 1:
        academy.start_session(student, is_next=True)
        
        
        
        
        
        
        
        
        