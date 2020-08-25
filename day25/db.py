
import cx_Oracle
def create():
        #객체생성하기 
    connection = cx_Oracle.connect("scott", "tiger","192.168.0.32:1521/orcl")
    print(connection)
        #cur 생성
    cur = connection.cursor()

        #사용할 sql문
    sql = """ 
    CREATE TABLE FOODSS
        (NAME VARCHAR2(50),
        FOOD_CATEGORY VARCHAR2(50),
        ADDRESS VARCHAR2(50),
        REVIEW VARCHAR2(50))
    """
    cur.execute(sql)
    connection.commit()

    connection.close()

create()