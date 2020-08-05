import cx_Oracle
connection = cx_Oracle.connect("scott","tigertiger", "orcl.cyb0gs2amyei.ap-northeast-2.rds.amazonaws.com:1521/orcl")
print(connection)

cur = connection.cursor()


sql = """
select empno, job, deptno, ename
from emp 
where deptno = :deptno 
"""


cur.execute(sql,deptno = 10)  #변수명 
print(cur)

for empno,job, deptno, ename in cur:
    print("{}\t{}\t{}\t{}".format(empno,job, deptno, ename))


connection.close()




