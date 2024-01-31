# import csv
# import os

# class TextColors:
#     GREEN = '\033[92m'
#     RED = '\033[91m'
#     BLUE = '\033[94m'
#     YELLOW = '\033[93m'
#     RESET = '\033[0m'

# class Student:
#     def __init__(self, first_name, last_name, academy):
#         self.id = 1
#         self.firstname = first_name
#         self.lastname = last_name
#         self.academy = academy
#         self.already_enrolled = self.check_enrollment_status()

#         student_data = {
#             "id": self.id,
#             "first_name": self.firstname,
#             "last_name": self.lastname,
#             "academy": self.academy.id,
#             "fee_paid": 0,
#             "is_dropout": False,
#             "first_session_clear": False,
#             "second_session_clear": False
#         }

#         # Check if the file is empty or if the header does not exist
#         is_file_empty = os.stat("student.csv").st_size == 0
#         has_header = not is_file_empty and self.has_csv_header()

#         # Initialize the file in write mode if it's empty or if the header does not exist
#         with open("student.csv", 'a' if not (is_file_empty or has_header) else 'a', newline='') as file:
#             writer = csv.writer(file)

#             # Write the header only if the file is empty or if the header does not exist
#             if not has_header:
#                 writer.writerow(student_data.keys())

#             # Write the student data
#             writer.writerow(student_data.values())

#     def has_csv_header(self):
#         with open("student.csv", 'r') as file:
#             first_line = file.readline().strip()
#             return first_line == "id,first_name,last_name,academy,fee_paid,is_dropout,first_session_clear,second_session_clear"

#     def opt_out(self):
                
#                 if self.firstname == row[1] and self.lastname == row[2] and self.academy.id == row[3]:
#                     selected_student = {
#                         "id": row[0],
#                         "first_name": row[1],
#                         "last_name": row[2],
#                         "academy": row[3],
#                         "fee_paid": row[4],
#                         "is_dropout": True,
#                         "first_session_clear": False,
#                         "second_session_clear": False
#                     }

#         # If found, updates the student's status to dropout and writes it back to the file.
#                 with open("student.csv", "a") as file:
#                     fieldnames = ["id", "first_name", "last_name", "academy", "fee_paid", "is_dropout",
#                                 "first_session_clear", "second_session_clear"]
#                     writer = csv.DictWriter(file, fieldnames=fieldnames)

#                     if selected_student is not None:
#                         if file.tell() == 0:
#                             writer.writeheader()
#                         writer.writerow(selected_student)
#                         print(TextColors.RED + "\n You are opted out!" + TextColors.RESET)

#     def check_enrollment_status(self):
#         with open('student.csv', 'r') as file:
#             reader = csv.DictReader(file)
#             for student in reader:
#                 if (
#                     self.firstname == student["first_name"]
#                     and self.lastname == student["last_name"]
#                     and self.academy.id == student["academy"]
#                 ):
#                     if int(student["fee_paid"]) == int(self.academy.fee):
#                         print(TextColors.RED + "\n Student has already fully paid and cannot enroll again." + TextColors.RESET)
#                         return True

#                     print(TextColors.RED + "\n Student already enrolled! \n Please Join the Academy Again ......   " + TextColors.RESET)
#                     return False
                   

#             # If the loop completes without finding the student, it's a new enrollment
#             print(TextColors.GREEN + "\n New student enrolled! " + TextColors.RESET)
#             return True

#     def pay_fee(self, fee):
#         updated_row = None
#         with open("student.csv", 'r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 if self.firstname == row[1] and self.lastname == row[2] and self.academy.id == row[3]:
#                     updated_row = {
#                         "id": row[0],
#                         "first_name": row[1],
#                         "last_name": row[2],
#                         "academy": row[3],
#                         "fee_paid": fee + int(row[4]),
#                         "is_dropout": row[5],
#                         "first_session_clear": True if row[6] == "False" else False,
#                         "second_session_clear": True if row[7] == "False" else False
#                     }

#         with open('student.csv', 'a', newline='') as csvfile:
#             fieldnames = ["id", "first_name", "last_name", "academy", "fee_paid", "is_dropout",
#                         "first_session_clear", "second_session_clear"]
#             # check if the file is empty
#             file_empty=csvfile.tell()==0
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#             # Write the header only if the file is empty


#             if file_empty:
#                 writer.writeheader()

#             if updated_row is not None:
#                 writer.writerow(updated_row)
#                 if fee < int(self.academy.fee):
#                     remaining_fee = int(self.academy.fee) - fee
#                     print(f"\n You need to pay the remaining installment of {remaining_fee}")
#                 elif fee == int(self.academy.fee):
#                     print("\n Total Fee Paid ")
#                 else:
#                     over_payment = fee - int(self.academy.fee)
#                     print(f"You sent more money {over_payment}, Please contact the office!")

# class Academy:
#     def __init__(self, id, name, academy_fee, course):
#         self.id = id
#         self.name = name
#         self.fee = academy_fee
#         self.course = course
#     def start_session(self, student, is_next=False):
#         print("\n Starting new session ")
#         print(TextColors.YELLOW + f" \n Academy Name: {self.name}" + TextColors.RESET)
#         print(TextColors.YELLOW + f"\n Course Name: {self.course}" + TextColors.RESET)
#         additional_fee = 0 # Initialize additional_fee before the loop
#         if is_next:
#             feepaid = 0
#             with open('student.csv', 'r', newline="") as file:
#                 reader = csv.DictReader(file)
#                 for row in reader:
#                     if row["first_name"] == student.firstname and row["last_name"] == student.lastname and row["academy"] == str(self.id):
#                         feepaid = int(row["fee_paid"])

#             remaining_fee = max(0, int(self.fee) - feepaid)

#             while remaining_fee > 0:
#                 print(TextColors.YELLOW + f"\n Remaining Fee for the next session: {remaining_fee}" + TextColors.RESET)

#                 # Ask the user to pay the remaining fee
#                 additional_fee = int(input(TextColors.BLUE + "\n Enter the amount to pay the remaining fee: " + TextColors.RESET))

#                 if additional_fee > remaining_fee:
#                     print(TextColors.RED + "You entered more than the remaining fee. Please try again." + TextColors.RESET)
#                 elif additional_fee < remaining_fee:
#                     print(TextColors.RED + "You entered less than the remaining fee. Please try again." + TextColors.RESET)
#                 else:
#                     # Update the student's fee paid
#                     student.pay_fee(additional_fee)
#                     print(TextColors.GREEN + "\n Remaining fee paid. You can now start the next session." + TextColors.RESET)

#                     # Recalculate remaining fee after user's input
#                     remaining_fee = max(0, int(self.fee) - (feepaid + additional_fee))

#             else:
#                 print(TextColors.GREEN + "\n No remaining fee. Your fees are up to date." + TextColors.RESET)

#             # Check for overpayment
#             overpayment = max(0, feepaid + additional_fee - int(self.fee))
#             if overpayment > 0:
#                 print(TextColors.YELLOW + f"\n You have overpaid by {overpayment}. Please collect your overpaid amount." + TextColors.RESET)




# if __name__ == "__main__":
#     name = input(TextColors.GREEN + " \n  Enter your Name: " + TextColors.RESET)
#     print(TextColors.BLUE + "\n  Please select the academy you want to join !" + TextColors.RESET)

#     with open("academy.csv", 'r') as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             print(row[0], row[1], row[2], row[3])

#         choice = int(input(TextColors.YELLOW + "\n  Enter the number to join the academy  :" + TextColors.RESET))
#         academy = None

#         with open("academy.csv", 'r') as file:
#             reader = csv.reader(file)
#             next(reader)
#             for row in reader:
#                 if int(row[0]) == choice:
#                     academy = Academy(row[0], row[1], row[2], row[3])

#         first_name, last_name = name.split(' ')
#         student = Student(first_name, last_name, academy)

#         print(f"\n Total enrollment Fee: {academy.fee}")
#         print("\n How much do you want to pay now?")
#         fee = int(input(TextColors.YELLOW + "\n Enter the amount:" + TextColors.RESET))

#         student.pay_fee(fee)
#         choice = int(input(TextColors.BLUE + "\n  Do you want to start the next session(1) or opt out(2)?"
#                            + TextColors.RESET))

#         if choice == 2:
#             student.opt_out()
#         elif choice == 1:
#             academy.start_session(student, is_next=True)
