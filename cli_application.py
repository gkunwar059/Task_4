class TextColors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

import sys
from sampledatabase import DBHandler

class Student:
    def __init__(self, first_name, last_name, academy):
        try:
            id = DBHandler.get_last_id()
        except ValueError:
            id = 0
        self.id = id + 1
        self.firstname = first_name
        self.lastname = last_name
        self.academy = academy
        already_enrolled = DBHandler.check_enrollment_status(self.firstname, self.lastname, self.academy.id)
        print(already_enrolled)
        if already_enrolled:
            choice = int(input("Student already enrolled. Do you want to join again? [1] Yes [2] No"))
            if choice == 2:
                sys.exit()
            elif choice != 1:
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
        DBHandler.add_student(student_data)


    def opt_out(self):
        student_dict=DBHandler.get_student(self.id)
        if DBHandler.update_student(self, {"first_name":student_dict['first_name'],"last_name":student_dict['last_name'],"academy":student_dict['academy'],"fee_paid":student_dict['fee_paid'],"is_dropout": True, "first_session_clear": False, "second_session_clear": False}):
            print(TextColors.RED + "\n You are opted out!" + TextColors.RESET)
        else:
            print(TextColors.RED + "\n Student not found for opt-out." + TextColors.RESET)
            
            
    def check_enrollment_status(self):
        return DBHandler.check_enrollment_status(self.firstname, self.lastname, self.academy)
    
    
    def pay_fee(self, fee):
        students = DBHandler.get_students()
        if students:
            student = students[0]
            fee_paid_from_db = DBHandler.get_fee_paid(student)
            fee_paid_from_db = int(fee_paid_from_db)
            total_paid_fee = fee + fee_paid_from_db
            remaining_fee = DBHandler.update_fee_paid(student, fee)
            over_payment = max(0, total_paid_fee - int(self.academy.fee))
            first_session_clear = True if student.get("first_session_clear") == "False" else student.get(
                "first_session_clear")
            second_session_clear = True if student.get(
                "second_session_clear") == "False" and first_session_clear == 'True' else False
            if not DBHandler.update_student(self, {
                "first_name": self.firstname,
                "last_name": self.lastname,
                "academy": self.academy.id,
                "fee_paid": total_paid_fee,
                "is_dropout": student["is_dropout"],
                "first_session_clear": first_session_clear,
                "second_session_clear": second_session_clear
            }):
                print("Could not pay your fee ...")

            if total_paid_fee < int(self.academy.fee):
                print(f"\nYou need to pay the remaining installment of {remaining_fee}")
            elif total_paid_fee == int(self.academy.fee):
                print("\nTotal Fee Paid")
            else:
                over_payment = total_paid_fee - int(self.academy.fee)
                print(f"You sent more money {over_payment}, Please contact the office!")
        else:
            print("No student found.")
            
            
             
    def view_details(self):
            student_data = DBHandler.get_student(self.id)
            if student_data:
                print(TextColors.BLUE + "\n Student Details:" + TextColors.RESET)
                print(f" Student ID: {student_data['id']}")
                print(f" First Name: {student_data['first_name']}")
                print(f" Last Name: {student_data['last_name']}")
                print(f" Academy: {self.academy.name}")
                print(f" Course: {self.academy.course}")
                print(f" Total Enrollment Fee: {self.academy.fee}")
                print(f" Fee Paid: {student_data['fee_paid']}")
                print(f" Enrollment Status: {'Enrolled' if not student_data['is_dropout'] else 'Opted Out'}")
                print(f" First Session Cleared: {student_data['first_session_clear']}")
                print(f" Second Session Cleared: {student_data['second_session_clear']}")
            else:
                print("No student found.")    
  
    def cancel_admission(self):
            student_data = DBHandler.get_student(self.id)
            if student_data:
                total_paid_fee = float( student_data['fee_paid'])
                refund_amount = total_paid_fee * 0.5  # 50% refund
                remaining_fee = int(total_paid_fee - refund_amount)

                if DBHandler.update_student(self, {
                    "first_name": self.firstname,
                    "last_name": self.lastname,
                    "academy": self.academy.id,
                    "fee_paid": remaining_fee,
                    "is_dropout": True,
                    "first_session_clear": False,
                    "second_session_clear": False
                }):
                    print(TextColors.RED + "\n Admission canceled. 50% refund processed." + TextColors.RESET)
                else:
                    print(TextColors.RED + "\n Failed to cancel admission." + TextColors.RESET)
            else:
                print("No student found.")                                   

class Academy:
    def __init__(self, id, name, academy_fee, course):
        self.id = id
        self.name = name
        self.fee = academy_fee
        self.course = course


    def start_session(self, student:Student, is_next=False):
        print("\n Starting new session ")
        print(TextColors.YELLOW + f" \n Academy Name: {self.name}" + TextColors.RESET)
        print(TextColors.YELLOW + f"\n Course Name: {self.course}" + TextColors.RESET)
        additional_fee = 0
        if is_next:
            remaining_fee = max(0, int(self.fee) - DBHandler.get_fee_paid(student))
            while remaining_fee > 0:
                print(TextColors.YELLOW + f"\n Remaining Fee for the next session: {remaining_fee}" + TextColors.RESET)
                additional_fee = int(
                    input(TextColors.BLUE + "\n Enter the amount to pay the remaining fee: " + TextColors.RESET))
                if additional_fee > remaining_fee:
                    print(TextColors.RED + "You entered more than the remaining fee. Please try again." + TextColors.RESET)
                elif additional_fee < remaining_fee:
                    print(
                        TextColors.RED + "You entered less than the remaining fee. Please try again." + TextColors.RESET)
                else:
                    student.pay_fee(additional_fee)
                    print(
                        TextColors.GREEN + "\n Remaining fee paid. You can now start the next session." + TextColors.RESET)
            else:
                print(TextColors.GREEN + "\n No remaining fee. Your fees are up to date." + TextColors.RESET)

            overpayment = max(0, DBHandler.get_fee_paid(student) - additional_fee - int(self.fee))
            if overpayment > 0:
                print(
                    TextColors.YELLOW + f"\n You have overpaid by {overpayment}. Please collect your overpaid amount." + TextColors.RESET)



if __name__ == "__main__":
    name = input(TextColors.GREEN + "\t \t \n Enter your Name: " + TextColors.RESET)
    print(TextColors.BLUE + "\n Please select the academy you want to join!" + TextColors.RESET)

    academies = DBHandler.read_academy_data()
    for idx, row in enumerate(academies, start=1):
        print(f" {row['id']} {row['name']} {row['fee']} {row['course']}")
    while True:
        try:
            choice = int(input(TextColors.YELLOW + "\n Enter the number to join the academy: " + TextColors.RESET))
            academy = next(
                (Academy(row['id'], row['name'], row['fee'], row['course']) for row in academies if int(row['id']) == choice),
                None)
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
            choice = int(
                input(TextColors.BLUE + "\n Do you want to start the next session(1) , opt out(2) ,Student view detail (3) and Admission Cancel (4) ? and " + TextColors.RESET))
            break
        except ValueError:
            print("Please choose 1 ,2,3,4")
    
    
    if choice == 3:
        student.view_details()

    if choice == 2:
        student.opt_out()
        
    elif choice == 1:
        academy.start_session(student, is_next=True)
        
    elif choice == 4:
        student.cancel_admission()

