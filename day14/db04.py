import cx_Oracle  #오라클에 연결하게끔 외부에서 가져옴 
#1. connecton 객체 생성
connection = cx_Oracle.connect("scott", "tigertiger","orcl.cyb0gs2amyei.ap-northeast-2.rds.amazonaws.com:1521/orcl")
print(connection)
#2. cursor 객체
cur = connection.cursor()



#.3. 사용할 sql문 객체  #문장 길어지면 """ 
sql = """
    INSERT INTO dept VALUES (:deptno, :dname, :loc)
"""

#4. 실행 
# cur.execute(sql,[1,"SALESMAN", 'SELOUL'])
#이 sql문 쓰되 값 순서대로 씀 
cur.execute(sql,[2,None, "BUSAN"]) # null로 쓰는 데 파이썬 이어서 None
cur.execute(sql,[3,"INCHEON"])

# sql = """
#     INSERT INTO dept (deptno, loc) VALUES (:deptno,:loc) 
# connection.commit()
# """
#값을 넣지 않으면 null로 하는 방법이 있음. 
#5. 로직처리 
connection.commit()

connection.close()
# 6. 자원 반납 
# connection.close()

#update, delete도 같음. 

