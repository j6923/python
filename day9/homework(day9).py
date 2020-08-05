# 1. 두 개의 정수 값을 받아 두 값의 평균을 구하는 함수를 작성하고 임의의 값으로 실행 하세요 

def avg(a,b):
    return (a+b)/2
a, b = input("두 개의 정수값을 입력하세요:").split()
a= int(a)
b= int(b)
print(avg(a,b))

# 2. sList 는 학생들의 영어 점수로 만든 리스트 이다.  최댓값과 최솟값을 반환하는 함수를 작성하세요.

# sList = [ 90, 80, 23, 55, 32, 50, 95, 90, 85, 60, 75, 35, 88, 92]

# def max_min(listData):

sList = [ 90, 80, 23, 55, 32, 50, 95, 90, 85, 60, 75, 35, 88, 92]

def max_min(sList):
    return max(sList), min(sList)
print(max_min(sList))
    

# 3. e:/dev/python_workspace/  경로에 있는 *.txt 파일의 목록을 파이썬 리스트로 반환하는 함수를 작성하세요.

for file in os.listdir("e:/"):
    if file.find("*.txt")>0: 
        print(file)
# def get_list(path):
#     pass
print(os.listdir("e:\dev\python_workspace")) 

# 4. 오늘의 월 일을 출력하는 함수를 작성하세요 

def get_todate():
    import time 
    return time.gmtime().tm_mon,time.gmtime().tm_mday    
print(get_todate()) 
    



# 5.  다음 함수를 작성하세요 


def get_triangle_area(width, height):
    return width, height #삼각형 너비 구하는 것 : 밑변 height 높이 
print(get_triangle_area)


add(100, 200) #함수사용하려고요 매게변수 전달할 거예요. 
#print(add(100,200))


# print(get_triangle_area(100,200))  # 10000

# 6. 
원주율 파이 원 너비 

# def get_circle_area(radius):
#     pass


# print(get_circle_area(10))  # 314.1592653589793



# 7. nList 에 랜덤하게 1부터 100사이 의 정수 20개 를 넣는다. 

nList = []
nList.append(int(range[1,21]))

# 8. nList에 홀수 가 몇개가 있는지 를 리턴하는 함수를 구하세요 

# print(get_odd(nList))  # n


# 9.  5자로 구성된 랜덤문자를 만들어 20개를 넣는다. 

# wordList = []   # wordList = ['abcde', 'xwdsd, ....]

from random import randint
for i in range():
    print(wordList)


# 10. wordList 요소에서 뒤에 3글자만 자른 문자를 갖는 리스트를 출력하는 함수를 작성하세요

# print(get_last_word(wordList))  #  [ cde ,  dsd  , .... ]
def get_last_word():
    return wordList 

# 11. 지금까지 만들어진 함수를 test 라는 모듈로 작성하세요


# 12. 현재 파일에서 실행할때만 테스트 결과가 출력되게 작성하세요 
# if __name__=="__main__":  #math.파이
print(__name__) 
print("잘 나오나?")
if __name__=="__main__":
# 13. ex1.py 파일을 작성하고  test. get_circle_area(300)을 실행시켜보세요


# 14. 다른 모듈의 함수를 불러 사용하는 방법 3가지를 정리하세요 
#임포트 하는 방법 3가지 
#1) import 모듈명 
#2) from 모듈명 import 함수명 
#3) from 모듈명 import *
lines = ['안녕하세요\n',"오늘은 금요일\n", "이면 좋겠네요\n"]

# 15. 비의 깡 가사를 rain.txt 파일에 저장하세요 
lines = ["Yeah 다시 돌아왔지\n","내 이름 레인(RAIN)\n","스웩을 뽐내 WHOO!\n","They call it! 왕의 귀환\n","후배들 바빠지는 중!\n",
"신발끈 꽉 매고/n","스케줄 All Day\n","내 매니저 전화기는\n","조용할 일이 없네 WHOO!\n\n","15년을 뛰어\n","모두가 인정해 내 몸의 가치\n",
"허나, 자만하지 않지\n","매 순간 열심히 첫 무대와 같이\n", "타고난 이 멋이 어디가\n","30 sexy 오빠\n","또 한번 무대를 적셔\n","레인이펙트\n",
"나 비 효과\n\n","화려한 조명이 나를 감싸네\n","시간이 멈추길 기도해\n","but, I’m not gonna cry yeah\n","불 꺼진 무대 위 홀로 남아서\n",
"떠나간 그대의 목소릴 떠올리네/n"
"나 쓰러질 때까지 널 위해 춤을 줘\n"
"허세와는 거리가 멀어\n"
"난 꽤 많은 걸 가졌지\n"
"수많은 영화제 관계자\n"
"날 못 잡아 안달이 나셨지\n"
"귀찮아 죽겠네 알다시피\n"
"이 몸이 꽤 많이 바빠\n"
"섭외 받아 전세계 왔다 갔다\n"
"팬들이 하늘을 날아 WHOO!\n\n"

"TV 드라마, 영화 yeah!\n"
"I get it all\n"
"이젠 모두를 붙잡을 노래를 불러\n"
"볼륨은 올리고\n"
"재 등장과 동시\n"
"완전 물 만나 call me 나쁜 오빠\n"
"무대를 다시 한번 적시지\n"
"레인이펙트\n"
"나 비 효과\n\n"

"화려한 조명이 나를 감싸네\n"
"시간이 멈추길 기도해\n"
"but, I’m not gonna cry yeah\n"
"불 꺼진 무대 위 홀로 남아서\n
"떠나간 그대의 목소릴 떠올리네\n
"나 쓰러질 때까지 널 위해 춤을 줘\n"]
with open("./day9/rain.txt",'w',encoding = "utf-8") as file:
    file.writelines(lines)  


  





# 16.
# 	rain.txt 에서 4글자 단어는 모두 몇개인가? 

# 17.
	
# 	사용자가 입력한 디렉토리의 파일과 디릭토리 목록을 dir.txt 파일에 저장하세요
	
# 	입력: c:/
	
	

# 18.
# 	로또 번호를 생성해서  lotto.txt 파일에 한줄씩 저장하세요 
# ex)
# 	3
# 	15
# 	29
# 	32
# 	35
# 	41
#lines list 
def lotto:
    import random 
    random.randint()
    
# 19.
# 	랜덤하게 소문자 3자를 생성해서  randomchar.txt 파일에 저장하세요 
import random
random.randint()
# 20.  다음 내용을 stock.csv 로 저장하세요 

# 	종목번호  회사명   현재주가 
# 	035720  카카오   326500
#  	005930  삼성전자  55600
# 	047820  초록뱀     1590 
3333444
6,카카오,122434

