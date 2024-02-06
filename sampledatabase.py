
from postgres_handler import postgres_connect
class DBHandler:
    
    
    @staticmethod
    def update_student(student, data):
        command = '''
            UPDATE student SET
                first_name = %s,
                last_name = %s,
                academy = %s,
                fee_paid = %s,
                is_dropout = %s,
                first_session_clear = %s,
                second_session_clear = %s
            WHERE id = %s;
        '''
        corr, conn = postgres_connect()
        tuple1 = (
            data['first_name'],
            data['last_name'],
            data['academy'],
            data['fee_paid'],
            data['is_dropout'],
            data['first_session_clear'],
            data['second_session_clear'],
            student.id
        )
        corr.execute(command, tuple1)
        conn.commit()
        corr.close()
        conn.close()

        return corr.rowcount > 0

    @staticmethod
    def check_enrollment_status(first_name, last_name, academy):
        command ='''SELECT * FROM student WHERE first_name = %s AND last_name = %s AND academy = %s'''
        tuple1 = (first_name, last_name, str(academy))
        
        corr, conn = postgres_connect()
        corr.execute(command, tuple1)
        result = corr.fetchone()
        corr.close()
        conn.close()
        return result is not None


    @staticmethod
    def get_student(id):
        command='''
        select * from student where id=%s
        
        '''
        tuple1=(id,)
        corr,con=postgres_connect()
        corr.execute(command,tuple1)
        student=corr.fetchone() 
        corr.close()
        con.close()
        student_dict = dict(zip(["id", "first_name", "last_name", "academy","fee_paid","is_dropout","first_session_clear","second_session_clear"], student))
        return student_dict  



    @staticmethod
    def add_student(data):
        command = '''
            INSERT INTO student (first_name, last_name, academy, fee_paid, is_dropout, first_session_clear, second_session_clear)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id;
        '''

        corr, conn = postgres_connect()

        tuple1 = (
            data['first_name'],
            data['last_name'],
            data['academy'],
            data['fee_paid'],
            data['is_dropout'],
            data['first_session_clear'],
            data['second_session_clear']
        )

        corr.execute(command, tuple1)
        new_id = corr.fetchone()[0]
        conn.commit()
        corr.close()
        conn.close()

        return new_id


    @staticmethod
    def get_fee_paid(student):
        feepaid = 0
        command = '''
            SELECT fee_paid FROM student
            WHERE id = %s
        '''
        tuple1 =(student["id"],) if type(student) is dict else (student.id,) 
        
        corr, conn = postgres_connect()
        corr.execute(command, tuple1)
        result = corr.fetchone()
        corr.close()
        conn.close()
        if result:
            feepaid = int(result[0])  # Convert to integer
        return feepaid


    @staticmethod
    def update_fee_paid(student, additional_fee):
        total_payed_fee = DBHandler.get_fee_paid(student) + additional_fee

        command = '''
            UPDATE student
            SET fee_paid = %s,
                first_session_clear = %s,
                second_session_clear = %s
            WHERE id = %s
        '''
        tuple1 = (total_payed_fee,
                  True if student["first_session_clear"] == "False" else student["first_session_clear"],
                  True if student["second_session_clear"] == "False" and student["first_session_clear"] == 'True' else False,
                  student["id"])

        corr, conn = postgres_connect()
        corr.execute(command, tuple1)
        conn.commit()
        corr.close()
        conn.close()
        
        remaining_fee = max(0, int(student["fee_paid"]) - total_payed_fee)
        return remaining_fee
    
 
    @staticmethod
    def read_academy_data():
        academies = []
        command = '''
            SELECT * FROM academy
        '''

        corr, conn = postgres_connect()
        corr.execute(command)
        academies = corr.fetchall()
        corr.close()
        conn.close()

        academies_list = []
        for academy_tuple in academies:
            academy_dict = dict(zip(["id", "name", "fee", "course"], academy_tuple))
            academies_list.append(academy_dict)

        return academies_list
    
    
    
    
    @staticmethod
    def get_last_id():
        command = '''
            SELECT id FROM student
            ORDER BY id DESC
            LIMIT 1
        '''

        corr, conn = postgres_connect()
        corr.execute(command)
        result = corr.fetchone()
        corr.close()
        conn.close()

        if result:
            return result[0]
        else:
            return 0