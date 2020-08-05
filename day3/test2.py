'''
자료형 :
'''
s = 'sequence' #이런 문자열이 있어요 
print(s,len(s),s.count('e'),s.find('e')) #몇자인지 알고 있어요 , 그 뒤 count e가 몇 개 있어 숫자 세줌. 그 뒤 e 찾아줘 
print(s.find('e',3),s.rfind('e')) # 세번째부터 e를 찾고 싶어요.그래서 4 그 뒤 아래 
#오른쪽에서부터 찾고 싶어요 .


ss = 'mbc'

print('mbc', type(ss), id(ss))  # 어디에 있는지 주소추적,ss가 어디있는지 반환해주는 것 id 
#id(): 객체의 고유값(레퍼런스)을 반환하는 함수

print("문자열 자르기")
print(s, s[2:4], s[3:], s[3::2]) # ... 3부터 끝까지 ,3부터 건너서 끝까지 2개 건너서 (step)--배열형태로 가져온다고 보면 됨. 한글자씩 끊어서 


msg = " Hello Python " # 앞에 공백 한 칸 중간 한 칸 마지막 한칸 있음 
#공백제거하는 함수 strip 
print(msg, msg.strip()) 
#나란히 
print(msg)
print(msg.strip()+"^^") #제거되는 효과 넣기 위해 "^^"
print(msg.rstrip(), msg.lstrip) #왼쪽만 지워요 rstrip  #오른쪽 공백만 지워요. lstrip
#사용자 입력받는 값 이렇게 조작 많이 해야함.    


msg = "구정,신정,성탄절,초파일,추석"    #msg라는 문자열을 만든다
m = msg.split(",")                      #msg문자열을 ","(쉼표)단위로 나누어서 m에 저장한다. split을 쓰면 반환 타입은 list이다
for i in m:                             # 반환된 리스트m에 값들을
    print(i)                            #출력한다.

msg3 = list('hello')
print(msg3)

str_time = ['10', '44', '30']

print(";".join(str_time)) #,붙여 문자열로 만들고 싶음, split의 반대 
#문자열을, 단위로 짤라서 리스트 ==> split(",")
#리스트에, 문자를 붙여서 문자열로 -->",".join(리스트)

msg3 = list('hello')
print(msg3)

print(msg3[3])


print(msg3[4])
msg3[0] = 'm'
print(msg3)



