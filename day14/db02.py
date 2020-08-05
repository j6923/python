import cx_Oracle
#1. connecton 객체 생성
connection = cx_Oracle.connect("scott", "tigertiger","orcl.cyb0gs2amyei.ap-northeast-2.rds.amazonaws.com:1521/orcl")
print(connection)


#2. cursor 객체

cur = connection.cursor()

#.3. 사용할 sql문 객체  #문장 길어지면 """ 
sql ="""
select empno, ename, sal
FROM emp 
Where ename = :txt 
"""
#SCOTT부분만 바뀜, 변수인지 값인지 :로 앎, 바이드 변수 


#4. 실행 

cur.execute(sql,txt="SCOTT") #두번쨰 매게변수가 :txt에 전달 ... txt란 변수에 scott넣어서 써 
print(cur)

#5. 로직처리 
# for x in cur:
#     print(x)    

for empno,ename, sal  in cur: #튜플형태 하나씩 꺼내서 볼 수 있었음 
    print("{}\t{}\t{}".format(empno,ename,sal))


# 6. 자원 반납 
connection.close()




    