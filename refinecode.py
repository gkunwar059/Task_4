import csv

class TextColors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

class Student:
    def __init__(self, first_name, last_name, academy):
        self.id = 1
        self.firstname = first_name
        self.lastname = last_name
        self.academy = academy
        self.already_enrolled = self.check_enrollment_status()

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

        # initialized student_data write into a csv file
        self.write_student_data([student_data])

    @classmethod
    def update_student_data(cls, student_data):
        existing_students = cls.load_existing_students()

        student_found = False
        for existing_student in existing_students:
            if cls.student_match(existing_student, student_data):
                existing_student.update({
                    'fee_paid': student_data['fee_paid'],
                    'is_dropout': student_data['is_dropout'],
                    'first_session_clear': student_data['first_session_clear'],
                    'second_session_clear': student_data['second_session_clear']
                })
                student_found = True

        if not student_found:
            existing_students.append(student_data)

        cls.write_student_data(existing_students)

        if student_found:
            print(TextColors.GREEN + "\nStudent data updated successfully!" + TextColors.RESET)
        else:
            print(TextColors.GREEN + "\nNew student enrolled successfully!" + TextColors.RESET)

    @staticmethod
    def student_match(existing_student, student_data):
        return (
            'first_name' in existing_student and existing_student['first_name'] == student_data['first_name']
            and 'last_name' in existing_student and existing_student['last_name'] == student_data['last_name']
            and 'academy' in existing_student and existing_student['academy'] == student_data['academy']
        )

    @classmethod
    def load_existing_students(cls):
        with open('student.csv', 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)

    @classmethod
    def write_student_data(cls, data):
        with open('student.csv', 'w', newline='') as csvfile:
            fieldnames = ["id", "first_name", "last_name", "academy", "fee_paid", "is_dropout",
                          "first_session_clear", "second_session_clear"]

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    @classmethod
    def find_student(cls, first_name, last_name, academy):
        existing_students = cls.load_existing_students()
        for student in existing_students:
            if cls.student_match(student, {'first_name': first_name, 'last_name': last_name, 'academy': academy}):
                return student

    def opt_out(self):
        selected_student = self.find_student(self.firstname, self.lastname, self.academy.id)

        if selected_student is not None:
            selected_student.update({
                "is_dropout": True,
                "first_session_clear": False,
                "second_session_clear": False
            })
            self.write_student_data([selected_student])
            print(TextColors.RED + "\n You are opted out!" + TextColors.RESET)

    def check_enrollment_status(self):
        existing_students = self.load_existing_students()

        for student in existing_students:
            if self.student_match(student, {'first_name': self.firstname, 'last_name': self.lastname, 'academy': self.academy.id}):
                if int(student["fee_paid"]) == int(self.academy.fee):
                    print(TextColors.RED + "\n Student has already fully paid and cannot enroll again." + TextColors.RESET)
            # elif
                    # return True
                    break

                print(TextColors.RED + "\n Student already enrolled! " + TextColors.RESET)

                print(f"\n Previous Fee Information:")
                print(f" - Fee Paid: {student['fee_paid']}")
                remaining_fee = max(0, int(self.academy.fee) - int(student["fee_paid"]))
                over_payment = max(0, int(student["fee_paid"]) - int(self.academy.fee))

                if remaining_fee > 0:
                    print(f" - Remaining Fee for the next session: {remaining_fee}")
                elif over_payment > 0:
                    print(f" - Overpayment from previous sessions: {over_payment}")
                    print("   Please contact the office for a refund or carry forward for the next session.")
                else:
                    print(" - Your fees are up to date. No remaining fee or overpayment.")

                return True

        print(TextColors.GREEN + "\n New student enrolled! " + TextColors.RESET)
        return False

    def pay_fee(self, fee):
        selected_student = self.find_student(self.firstname, self.lastname, self.academy.id)

        if selected_student is not None:
            updated_row = {
                "id": selected_student["id"],
                "first_name": selected_student["first_name"],
                "last_name": selected_student["last_name"],
                "academy": selected_student["academy"],
                "fee_paid": fee + int(selected_student["fee_paid"]),
                "is_dropout": selected_student["is_dropout"],
                "first_session_clear": not selected_student["first_session_clear"],
                "second_session_clear": not selected_student["second_session_clear"]
            }

            self.write_student_data([updated_row])

            if fee < int(self.academy.fee):
                remaining_fee = int(self.academy.fee) - fee
                print(f"\n You need to pay the remaining installment of {remaining_fee}")
            elif fee == int(self.academy.fee):
                print("\n Total Fee Paid ")
            else:
                over_payment = fee - int(self.academy.fee)
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

        if is_next:
            feepaid = 0
            with open('student.csv', 'r', newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[1] == student.firstname and row[2] == student.lastname and row[3] == self.id:
                        feepaid = row[4]

if __name__ == "__main__":
    name = input(TextColors.GREEN + " \n  Enter your Name: " + TextColors.RESET)
    print(TextColors.BLUE + "\n  Please select the academy you want to join !" + TextColors.RESET)

    with open("academy.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row[0], row[1], row[2], row[3])

        choice = int(input(TextColors.YELLOW + "\n  Enter the number to join the academy  :" + TextColors.RESET))
        academy = None

        with open("academy.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if int(row[0]) == choice:
                    academy = Academy(row[0], row[1], row[2], row[3])

        first_name, last_name = name.split(' ')
        student = Student(first_name, last_name, academy)

        print(f"\n Total enrollment Fee: {academy.fee}")
        print("\n How much do you want to pay now?")
        fee = int(input(TextColors.YELLOW + "\n Enter the amount:" + TextColors.RESET))

        student.pay_fee(fee)
        choice = int(input(TextColors.BLUE + "\n  Do you want to start the next session(1) or opt out(2)?"
                           + TextColors.RESET))

        if choice == 2:
            student.opt_out()
        elif choice == 1:
            academy.start_session(student, is_next=True)
