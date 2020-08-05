
mydic = dict(k1=1, k2='abc', k3 = 3.4)  #앞 키 뒤 값(value) , =은 '매칭되는 애들의 의미', 숫자는 정수, 실수 상관없이 사용가능 
print(mydic)

dic = {'파이썬' : '뱀', '자바': '커피', '오라클':'예언자'} #신 이름으로 지은것 오라클은,, 쌍 이루는 걸로 이룸 #이렇게 딕션어리 만들 수 있음. 
#탐색하고 찾음
# print(dic, len(dic)) #dic가 있고 길이 구함. 묶어놓은 것이 한 개임. 
# print(dic['자바']) #키로 밸류값 찾을 수 있음 , 키로 벨류값을 꺼내줌. 
# dic['스미스'] = "백그라운드프로세스" #없는 요소에 추가 할당하면 추가 됨 
# print(dic) #새로운 애들도 더 추가가능. 
dic['neo'] = "주인공"
dic['스미스'] = "bg" #같은 이름  t값에 할당값을 하면 써짐, 있는 값 할당 하면 덮어써버림
# #중복된 값 안 됨, 중복된 값 주면 덮어써버림. 
# print(dic)
#print(dic[0]) #인덱싱해서 찾을 수 없음

#안에 하나씩 꺼내고 싶어요. 
for key in dic:
        print(key, dic[key])

    #처음부터 값(value)들만 출력

for val in dic.values():
    print(val)

#키와 value 모두 한꺼번에 가져오고 싶어요. 
for key, val in dic.items():
    # print("key = "+key+", value : " + val) #보기 좋게 하려면 
    print("key : {key}, value : {val}". format(key=key, val=val)) #되어있는 애의 format의 이거에는 이거 val에는 val넣어라. 

# 키가 있는지 여부 판단 : in 

print('neo' in dic)  #True, False 형태로 리턴 

#네오 지워버리고 싶어 neo삭제   
del dic['neo']    #키 값이 neo인 항목 삭제 

print(dic)                    


#다양한 형태의 데이터 들어갈 수 있음  #여러개 쓰고 싶습니다 game은 키 
dic['game'] = ['대항해시대', '바람의 나라', '운명6', '토탈위'] #키로는 못 써도 value값으로 쓸 수 있음. 
print(dic)

dic['broadcasting_co']=['kbs', 'mbc', 'sbs', 'ytn', 'jtbc'] #키가 있다면 밸류 여러개 가능, 그리고 리스트로 들어갈 수 있다. 
print(dic) 


from pprint import pprint as pp  #줄 맞추는 것 좋아해요. 별칭으로 pp할게 as두에 있는 것 

pp(dic) #enter딱딱 들어가요. 

#정리 
#문자형, list 튜플, set, dic , range 실수, 정수 ,복소수 
#순서 없어요, dic set 첫번째, 두번째 꺼내서 쓸 수 없어요.
  
#과일명, 과일생산지를 dictionary 로 작성 
#여러개면 []리스트로 가능 
fruit = {'딸기' : ['논산', '하우스'],'망고': '필리핀', '두리안':'말레이시아', '사과':['봉화', "영주"],'배' : '나주'}
#중괄호 안에 키값 콜론 벨류 값 
print(fruit["딸기"])  
#딸기 생산지를 출력 

#망고 생산지 
print(fruit["망고"])
#과일명: 생산지 형식으로 전체 출력 
for key, val in fruit.items():
    print(key, val)


