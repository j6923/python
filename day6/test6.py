#세계 최초의 암호화 : setEncryption(문자열)
#1. 사용자로부터 단어를 입력받는다. ex) HELLO
#  
#2. 3번째 뒤에 글자를 출력한다. ex_) ~~~
#문자열의 아스키코드값 얻고 3을 구해요, 문자에서 한 글자씩 잘라옴
#그것을 아스키 코드값으로 구해요. 그 값을 다시 문자열로 옴 
#문자 세 자가 A: 65~90 90은 +3은 이상한 문자됨. 끝의 3자 abc

#예) A ---> D   #줄리어스 시저가 옆으로 민 글자로 암호와 3칸 밀어. 
#    C ----> E 
#    B ------> E
# 
# #암호화 #복구화함수 구하고 싶어요.  

#getdecode 암호화 된 값 집어넣으면 HELLO와 값은 값 나오게 출력 
# def setEncryption()

s = input("문자를 입력하세요.: ")
print(s)
print(s[0]) #s의 첫번째 문자 구하세요. 
for i in s:
    print(ord(i)+3) #한글자 한글자 출력 
m = ord(i)-3
print(chr(m))   #아스키코드값을 문자로 바꿔줌  
#여러 글자 뽑을 거여서 , 3글자, 4글자일수도 있어서 
#문자를 아스키코드로 바꾸고 

