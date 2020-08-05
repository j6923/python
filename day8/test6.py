



def make2(fn):
    return lambda : "곤니찌와"+fn()    #실행해서 붙이는 것 
    #람다대신 test2 함수변경
    # def make2(): #함수이름
    #     return "곤니찌와"+fn()>>> 이것이 test2니까 이렇게  ..... 위의 것을 이렇게 바꿀 수 있습니다.  리턴 뒤에 오는 게 그거니까 
# make 1 함수를fn에 넣을 수 있음   

# def make1(fn):
#     return lambda : "니하오" + fn()  #처음 


def make1(fn):
    def test():
        return "니하오"+fn() #길어요 람다식으로 간결하게 하는 게 좋잖아? 
    return test     #매게변수 없어서 안써요. 함수명 안 쓰니까 lambda쓰고 
    return lambda : "니하오"+fn()  #익명함수 린턴 그것을 매게변수받는 fn있을 수있데요. 
#def 이름없음():
    #return "니하오"+fn()
#
def hello():
    return "한라봉" #누르면 "안녕"define함   #결과는 함수를 만들어라 print(hello())에 return"한라봉"을 가져다 써라.
print(hello())#결과하려고  
hi = make2(make1(hello)) #함수를 변수에 담을 수 있고 매게 변수에 담을 수 있고 함수#hello를 매게변수로 






#함수 10을 가지고 전달할거예요. 
#hi = 람다식(익명함수)여서 위의 형식으로 묶을 수 있음 
#익명함수 리턴 아무것도 없어요, 매게 변수 없어요. 뒤는 출력값, 리턴값 
#def 이름없음(): 매게변수 없음
#    return "니하오" + fn() #fn 함수를  

#익명함수인데 매게변수 안주고 "니하오"와 함수를 실행한 결과를 붙여 

print(hi()) #함수는 괄호안에서 부터 계산 

#hello() 찾아가서 실행,리턴 -- 부른 애한테 덮어씌워 

# make1()
#  100줌 fn

#fn()마지막 함수 실행해 뜻 #fn --- g

print(make1(hello)) #문자를 리턴했을 때 

#함수식으로 리턴하고 싶어요. 함수는 또다른 함수 리턴가능 
# def make1(fn):
#     def test():
#         return "니하오"+fn()  #람다식으로 써놓은 겁니다. 
#     return test 
#     return lambda : "니하오" + fn()
#print(make1(hello)) #hello 함수를 실행할 때 매게 변수로 전달해.



# hello() 실행해라  실행해서 부른 그 자리에 갖다넣어라. 
# 
# hello 그냥 이름임. 
# make1('하하하')실행할 때 이거 가지고 가서 실행해
# #make 문자열을 fn에 대입 함수 시작 test return 니하오에 fn에 실행해, 함수 아닌데 무슨 소리야 하고 에러남. 
# make1(ello)  #괄호 실헹 안의 함수 실행하고 그 결과  

print(make1(hello))  

t = make1(hello) #함수 실행하려면 괄호있어야 
print(t()) #방금전 이 함수 실행해 
#테스트 함수 

t2= make2(t) #make2(make1(hello))와 같은 것 
print(t2()) #make2(make1(hello))()붙인 것이랑 같음...실행한 것 괄호 열고 닫고  

print(make2(make1(hello))) #함수를 리턴하니까 실행할 거예요. 
# 데코레이터(decorator) ; 장식하다, 꾸미다 라는 의미  >>>>>>원래 기능에 꾸며서 꾸며서 넣어주어 만들면 더 좋게 나옴. 
#내부적으로 짜여있는 것있고 갖다,,, 바로 이걸로 하려면 수식잘 써야함.  
@make2 
@make1  #이게 적용된 헬로우 이거 집어넣어 처리해서 리턴 위의 것이랑 같음 
def hello2():
    return "소망이"

#hello() 실행   #make1(hello)

hi = hello2
print(hi())  #make함수에 넣어서 결과 얻고 싶어요. 