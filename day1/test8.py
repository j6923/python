#a, b, c 변수에 100, 200, 300 값을 대입 
# : 100, b : 200, c : 300 <---- 출력 
#값 교환 
# a : 300 b:100, c= 200 <----출력 
#각 변수에 값에서 10씩 증가 
#a : 310 b : 100, c: 210 <----- 출력 




a, b, c = 100, 200, 300 #값 안 맞으면 에러남. 

print("a :", a, ",b: ", b,", c: , c") #출력 
a, b, c = c, a, b 
print("a: ", a, ", b :", b, "c :, c")


a = a+10
b += 10
c += 10 
print("a : , a, b :", b, ", c :", c) 

a = 10; b= 20
#사칙연산 
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #int/int --> int 지 생각하는 사람있어 예전방법 구현 
print(a%b) #나머지 구하는 연산자 

#int 연산 int --> int 


print("----------------------------------------")
a = -a 
print(a)
print("---------------------------------------")

msg = input(" 출력할 메세지를 입력하세요") #사용자에게 보여주면서 입력받을 수 있음 
print(msg)  #입력받아 변수에 대입 그리고 출력 -- 메아리 
# 사용자로부터  두 수를 입력받아 화면에 출력
 

print("-----------------------------------------")
x = input("첫번째 숫자를 입력하세요")
y = input("두번째 숫자를 입력하세요")

print("x", x,", y:", y)
#사용자가 수를 입력하게끔 기다림
#여러 라인 동시 주석 : trl + /
#shift + alt + 화살표 아래방향키 


x = int(x)
y = int(y)

print(x+y)