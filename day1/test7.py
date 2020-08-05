#숫자형 변수 
#정수형(integer) --> int 
#실수형 (float)3.14 --> 314*
#복소수(complex 1.3+1.9i)--- i는 변수와 헷갈려 j로 씀 
#동적타이핑 언어 - 나중에 자료형 할당, 할당하는 순간, 없는게 아니라 안 쓰는 것 
a = 10

#type(a)- type안에 함수 명 어떤 형태인지 암 
# 어떤 타입알고 결과 알기 
print(type(a))

b = 30

#어떤 타입인지 출력 

print(type(b))

#b의 타입과 값 출력 
print(type(b))

print(b, type(b))

print("a : " ,a)
print("b : ", b)

c = "10"

print("a : " , a )
print("b : " , b)
print("c : " + c)
#형변환도 가능 int(), float(), complex(), 문자 str()
# 오라클에서는 to_number date 
print(" a : " + str (a))
print(" b  :", str  (b))
print(" c : " +str (c))


print("before : a: ", a, "b : " ,b)
#a --> 10, b= 20
#임시변수를 만든다 : temp 
temp = 0
#첫번째 변수의 값을 임시변수에 담는다 
temp =a  
#두번째 변수의 값을 첫번째 변수에 담는다.
a= b
#임시변수의 값을 두번째 변수에 담는다. 
b=temp 
#끝
print("after : a :", a , "b :", b) 
#print("before : a: ", a, "b : " b)
  

a, b = b, a 
print("=====> : a :" , a , "b : ", a)

x = 10
y = 10
z = 10 
print("x", x , "y:" , y, "z: ",z)

x = y = z = 10


i, j = 100, 200

print("i", i, "j : " , j)

#아무것도 없는 값 
x = None #다른 언어들은 null, 파이썬은 None,  첫자 대문자여야 함.

print(x)

#a = 100  #a 변수에 100값을 대입해  
#20을 증가 시킨후 출력
# 할당연산자와 계산 연산자 +먼저  
#a = a +20 +는 연산자  #a변수의 값에 20을 더한 후에 a변수에 그 값을 대입 
a = 100    
#a = temp
#a = a +20
a += 20 
#a += 20 