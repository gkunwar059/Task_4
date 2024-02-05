import psycopg2
def postgres_connect():
    conn= psycopg2.connect(
        host='localhost',
        database="postgres",
        user="postgres",
        password="123456789"
    )
   
   
    corr=conn.cursor()
            
    return corr,conn
        


        
    
    

