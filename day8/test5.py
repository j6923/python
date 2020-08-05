import re 
re.compile('패턴')  #정규표현식에 맞는지 확인해줌,  패턴을 만들어줌. 

p = re.compile('[0-9]+') #0-9까지 패턴을 만들어줌,, 형식이다. 
print(p, type(p))
#패턴 : 정규식을 컴파일한 결과       #기계가 이해할 수있는 바꿔주는 것.  

#문자열 검색 
#match() : 문자열의 처음부터 정규식과 매치되는지 조사 
#search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사 
#앞에서 매치, search는 전체에서 하는 것 --- 차이점
#findall(): 정규식과 매치되는 모든 문자열을 리스트로 돌려줘라. #찾은 글자를 가지고싶다면 그 글자만 가지고 올 수 있음. 
#finditer():글자가 아닌 다른 걸로 가지고 오고 싶어요--- 정규식과 매치되는 모든 문자열을 반복가능한 매체로 돌려준다. 
m = p.match("regular expression")
print(m)

if m: 
    print(m.group) #m이라는 애가 있어? 그럼 꺼내와. 
else: 
    print("no match") #그렇지 않으면 print "no match" #math는 앞에서부터 ㅊ팢는것 
    #regular expression 의 결과의 group을 가져옴 

print("--------------------------------------------------------------------")
result = p.search("99999999  aaaaaabbbbbb")
print(result)


#긴 문자열에서 찾고 싶어요
result2 = p.findall("hello python world today is monday")
print(result2)#매칭되는 애들 다가져와 리스트로 뽑음 ,,, 이메일만 가져와 이것 많이 씀,

#for 문으로 1개씩 출력 
for i in result2:
    print(i)
print("-------------------------------------------------------")

result3 = p.finditer("today is monday")
print(result3)

#구축가능한 객체입니다. callable iterator object at 

for data in result3:  #match object 
    print(data)
    print(data.group())  #group이 데이터 글자 값을 보게 됨 
    print(data.start(),":", data.end()) #가져옥되 반복가느한 걸로 가져옴, 반복 ,값을 뽑을려면 데이터 가져올 수  있어, start and 0부터 
    # 5번까지 가져올 수 있습니다. 

    #시작위치와 끝 위치 돌려주는 함수 start

msg = "999,999  smartphone bbb@naver.com aaa@gmal.com"

#이메일만 선택해서 출력하고 싶습니다. 
print(re.match('a-zA-Z@a-zA-Z0-9.a-zA-Z0-9',"999,999  smartphone bbb@naver.com aaa@gmal.com"))

p2 = re.compile("[a-zA-Z0-9.]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+")
print(p2)

result4 = p2.findall(msg)
print(result4)
for email in result4:
    print(email)


#match는 한번 나오면 끝, search는 전체


