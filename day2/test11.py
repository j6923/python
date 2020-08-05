print(1+1)
a = 10
print(a)
#실수로 바꾸고 싶어요 
a = float(a)
print(a)
print(complex(1.3, 1.4j)) #복소수 
#정수부랑 실수부랑


print("----------------------------------")


#input()은 입력하세요/ 안 쓰면 기다림
#변수에 얘를 담아서 밑에 
#x = input("아무 값이나 하나 입력하세요")
#print(x)
#x만 하면x지 뭔지 모르니까
#변수에 할당이 되고 결과 출력됨
# print("xdml rkqtdms :") 
#동시에 여러개 가능, 그리고 ','로 구분 
#print("aaa", "bbb", "cccc")
#print("aaa", "bbb", "cccc")
#print("x의 값은 :", x)
print(3>5) #3이 5보다 커, 참과 거짓으로 표시  #첫글자 대문자 나머지 소문자, 파이썬의 특성 
a = 100
b = 200
c = None 
#아무것도 안 쓰려면 None #앞에는 대문자로 쓰기 
print(a<b) #b가 더 큰카요? 

print(100>2 and 300>100)
print(100>2 and 300>100 or 100>200) 

x = True
y = False

print(x and y)
print("------------------------------------")
print(True and True)
print(False or True)


print(not True)

a = 300
b = 200
print(a == b)
print(a != b)


#국어, 영어, 수학 점수를 입력받기 
# 60점 이하가 있다면 False(실패), True(합격)
#kor = input("국어 점수를 입력하세요") #이렇게 해도됨 
kor, eng, mat = input("점수를 입력하세요").split()
#eng = input("영어 점수를 입력하세요") 
#mat = input("수학 점수를 입력하세요")
kor = int(kor) #int는 하나씩 
eng = int(eng)
mat = int(mat)
#print(kor>90) #이렇게도 할 수 있음 
#print(eng>60)
#print(mat>60) 
print("kor:", kor>90, "eng :", eng>60, "mat :", mat>60)


#print(kor>90)


#if(input("국어,영어, 수학").split()
#else false 

#수업 
kor, eng, mat = input("국어 영어 수학 점수를 입력하세요").split()
kor =int(kor)
eng = int(eng)
mat = int(mat)
#print("kor", kor, "eng:", eng, "mat", mat)
#변수 할당 출력됨 위
print("kor", kor >= 40, "eng:", eng >= 40, "mat", mat >= 40)
print("Total : ", kor >= 40 and eng>= 40 and mat>=40)
#이 조건 다 만족하면 합격  

print("평균 : " , kor + eng + mat/3 >=60)
#/3까지 하면 평균 나옴 





#잘못 씀 
m = [] #공백 m은 비어있는 리스트예요, 비워두었다가 값을 하나씩 추가해서 씀 
#range()연속된 값 얻을 수 있음 
print(range(10))
#print(range(0,10)) 0부터 10 미만 값 가짐 
# a = list(range(0,10)) 0부터 9까지 같고 리스트 되어서 가짐 리스트 형변환 
# 되서 나옴  
#0-3000넣으려면 어려움 그래서 사이값 지정하는 함수 지정 range 
# print(m) 
print(range(0,10))
#range(0, 10) 하면 range(10, 20) 
##10부터 19까지 10개의 연속된 숫자로 된 k list를 만들고 화면에 출력 

m=list(range(10,20))  
print(m) 

#print(range(10, 20, 2)) 시작값 끝값 증가폭을 줄 수 있음 
# 음수도 가능 
print(list(range(100,0,-1))) #줄어들 수도 있음 
#1부터 1000사이의 3의 배수를 목록으로 출력
# rang(시작값, 종료값, 증가폭) 
#print(2,100,2)
#print(3,1000,3) -- > 3부터 하면 3의 배수로 됨. 
# print(list(range(1,1001,3*))) 왜 에러? 

#달의 표면 온도는 밤 : -170 낮 120도, 초당 3도씩 상승 한다고 가정했을 때 온도의
# 변화를 리스트로 만들어 출력  
print(list(range(-170,120,3)))

