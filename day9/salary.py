#연관되 함수들의 모음: 모듈 --- math, random, re,정규식 (모듈의 이름은 파일이름과 연관)
author = "홍길동"  #변수 쓸 수 있다. 
print(__name__) #__m^.^m__(underbar2)  #underbar2개 특별한 기능 있음 
def raise_sal(sal): #사원의 급여를 인상시켜주고 싶어요. 
    return int(sal*1.1) 
        #급여를 전달하면 10%인상된 급여를 리턴
    
def reduce_sal(sal):
    return int(sal*0.8)

    
#Test code   #모듈의 이름가지고 있어서 
if __name__=="__main__": #이 파일에서 실행할 때만 작동하게 함. \
#__name__ == --> 모듈의 이름을 가진 변수 (동작) #잘 동작되는 지 main 동작할 대는 잘 된다, 테스트하고 
    print(raise_sal(3000))       
#3000을 전달 sal에 return해서 sal*1.1     #연산하다보면 몇 자리까지 포기할 것이냐 약간의 오류가 있음, 오류라기 보다 오차정도  
#일상생활정도 
    print(reduce_sal(1000)) 

#급여를 줄이고 싶어요 
#reduce_sal(1000) --> 20%감소  800



#f2이름바꾸기 

    print("잘 나오나? :", author)

#이 파일에서 실행할 때만 테스트 코드가 보이게끔 하는게 좋을 것 같아요. 
#print(__name__) #__m^.^m__(underbar2)  #underbar2개 특별한 기능 있음 

