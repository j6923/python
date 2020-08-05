# msg ="aaa bbb 필라테스 힘들어 육체노동 eee smith@naver.com 010-1234-5678 aaa@gmail.com"
# #split해서 끊어온다옴에 @해서 함 
# # 특정 이메일, 김씨만 문자열해서 찾아와야할 될 일이 있음 
# #정규 표현식 --- 길이가 몇 자인 글자만, 이메일만, 이메일이 맞는지 
# #@이메일인지 아닌지 문자내 특정패턴 찾고  싶을 때
# # 특정 크룰링  선정해서 갖고 오는 것 좀더 쉽게 하기 위해 정규 표현식 지원 
# # 왠만한 언어 다 지원 
# # 특정한 규칙이 있는 문자열의 집합의 표현언어  ==== 정규 표현식
# # 
# # 
# # 
# # var pattern =/rules/ 0------java  
# #
# #java에서는 웹브라우저에서 

# print(msg)


'''
 정규표현식(regula expression) : 일정한 규칙(패턴)을 가진 무자열을 표현하는 방법 
 '''

import re #정규표현식 위한 함수 

 #re.match('패턴', '문자열') #라고 하는 애 있어서 앞에 패턴 뒤에 문자열
print(re.match('Hello','Hello python world'))  

 #find로 할 수 있음 여기에 이런 것 있어 
 #문자열 : .find() 

print('Hello','Hello python world'.find('Hello')) #없으면 -1 

 #첫글자가 H로 시작? 

 #데이터 많거나 데이터베이스에서 가져오거나 문서내에서 가져온다거나 하면 얘가 더 편함. 
 #^H
 #hat 첫글자가 이거인 것 
 #끝 문자는 d$

print(re.match('^H','Hello python world'))
print(re.match('world$','Hello Python world'))    

#이렇게 되어 있는 애 찾아 
#print(re.match('Hello','Hello python world'))  
print(re.search('^H','Hello python world'))
print(re.search('world$','Hello Python world'))
print("----------------------------------------------------")
#010-1234-5678
print(re.match('[0-9]+', '1234')) # + : 1개 이상 
print(re.match('[0-9]*', '1234')) #* 0개 이상 , 있을 수도 있고 없을 수도 있다. 


#
#aaabbb --->  a가 1개 이상 있나? 

print(re.match('a{1}','aaabbb')) #{1}개 'a+' 1개 이상 a가 여러개 있어. 정확하면 그냥 써도 됨.
print(re.match('a+b','aaabbb')) #a글자가 있고 여러개 있고 b가 있어 

#한글인지 찾아보고 싶어요
print(re.match('[가-힣]+', "불금달료보자.")) #한글인지 아닌지 알고싶어요 . '가-힣'가 한글의 범주. 낱글자로 잡는게 더 이상해 
#우리가 그렇게 안 쓰니까 #통문자--- 음가가 있는게 많아 가로 쓰는 게 맞아. 
# + : 1개 이상, * : 0 개 이상, ? : 0 or 1(0또는 1개 있음)
# ab9cd, ab9999cd
# print(re.match('ab[0-9]?cd','ab9cd','ab9999cd')) #1일 때는 생략가능  print와 re.match 
# a{1}b{1}    and    a{1}b{1}
print(re.match('a{1}b{1}c{1}d{1}','ab9cd')) and ('a{1}b{1}9{4}c{1}d{1}','ab9999cd')
#넘겨받는 객체 패턴 #사이트 패턴과 같음 #결과 똑같으면 됨. 전산에서는 여러가지 방법이 있음 
#많은 방법 중 쓸 수 있는 걱과 성능 어떤게 괜찮은지 모르지만 
#하지만 밑의 것이 더 짧음 #같은지 분리 연산 같은지 -- and는 
#여러개 하면 멈추는 지점 


print(re.match('a{1}b{1}c{1}d{1}','ab9cd'))

print('a{1}b{1}9{4}c{1}d{1}','ab9999cd')  #두개문자열을 찍어라 
print(None and "Hello") #과 같음. 마땅치 않으니까 none이 나옴. 

print("-----------------------------------------")
print(re.match('ab[0-9]?cd','ab9cd'))
print(re.match('ab[0-9]?cd','ab9999cd'))

