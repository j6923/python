#이번에는 종게임 

#게임의 기본 틀 
import pygame
import math 
#적우주선 출현 


#초기화 하기전 초기화 해줘야함. 
pygame.init()
#미사일과 충돌 테스트 
def pythagoras(x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)) #x측y측간의 차이의 제곱 #자꾸 불러쓰면 소스가 엉키게 됨. 



screen_width = 600  #너비 높임 
screen_height = 900

screen = pygame. display.set_mode((screen_width,screen_height)) #기본으로 설정 

isRunning = True   

pygame. display. set_caption("우주 전쟁")
#배경 이미지 객체(1)
bg = pygame.image.load("e:/dev/python_workspace/img/img2/space.jpg")
#캐릭터 우주선 객체     

player1 = pygame.image.load("e:/dev/python_workspace/img/img2/player1.png")
player2 = pygame.image.load("e:/dev/python_workspace/img/img2/player2.png")
player3 = pygame.image.load("e:/dev/python_workspace/img/img2/player3.png")
player4 = pygame.image.load("e:/dev/python_workspace/img/img2/player4.png")
#미사일 객체 
missile = pygame.image.load("e:/dev/python_workspace/img/img2/missile1.png")
#적 비행기 객체 
enemyship0 = pygame.image.load("e:/dev/python_workspace/img/img2/gunship0.png")
enemyship1 = pygame.image.load("e:/dev/python_workspace/img/img2/gunship1.png")
enemyship2 = pygame.image.load("e:/dev/python_workspace/img/img2/gunship2.png")
enemyship3 = pygame.image.load("e:/dev/python_workspace/img/img2/gunship3.png")

#크기 조정 
player1 = pygame.transform.scale(player1,(50,50))
player2 = pygame.transform.scale(player2,(50,50))
player3 = pygame.transform.scale(player3,(50,50))
player4 = pygame.transform.scale(player4,(50,50))



enemyship0 = pygame.transform.scale(enemyship0,(50,50))
enemyship1 = pygame.transform.scale(enemyship1,(50,50))
enemyship2 = pygame.transform.scale(enemyship2,(50,50))
enemyship3 = pygame.transform.scale(enemyship3,(50,50))

#캐릭터 우주선 좌표 변수 (8)
px = 250
py = 800  #그릴 때도 이 좌표 기준으로 그리기 
#이미지 크기를 화면의 크기로 변환(5) 
bg1 = pygame.transform.scale(bg,(600,900)) #이미지 속성 보면 사진크기 알 수있음. 사진 찍으면 장비에서 찍었늦지 gps좌표 찍힘, 해상도 시간 
bg2 = pygame.transform.scale(bg,(600,900)) #이미지 속성 보면 사진크기 알 수있음. 사진 찍으면 장비에서 찍었늦지 gps좌표 찍힘, 해상도 시간 


#시계변수 (6)
clock = pygame.time.Clock()
#미사일 객체 
missile = pygame.image.load("e:/dev/python_workspace/img/img2/missile1.png")

#미사일 좌표 변수 (10)
mx = -250 #원래 시작한발 있었는데 무작정 한발 발사, 우주로 보내버리기 (11)
my = -300
#여기 사이에 코드가 반복 되어야 종료하기전 계속 반복함. 
#카운터 변수 적용 (4)
cnt = 0
#배경 x,y좌표 
bg1Y=0
bg2Y=-900  #연결하게 하려면 -900되어야 함. 

my-=3#(10)

gs = 0
#적 우주선 좌표 변수 
ex =250
ey = 50
#


#미사일 리스트
mList = []

#충돌 체크 함수 
def collision():
    global ey #지역변수라고 생각해서 글로벌 변수로 함. 
    for m in mList:
        dis = pythagoras(ex,ey,m.x,m.y)
        if dis< 30:
            print("아야~~~")
            print(dis)        #미사일 한발 만 쏴서 테스트 
            ey -= 5
            m.x = -100 #미사일이 사라지는 효과가 나타남. 미사일 화면밖으로 가면 제거가 됨. 


class Missle: #객체로 만듦 
    def __init__(self,x,y):
        self.x = x
        self.y = y 

    def __del__(self): #소멸자 
        pass
        # print("소멸자..미사일 제거됨")

while isRunning:
    cnt += 1
    bg1Y+= 2
    bg2Y+= 2
    if bg1Y >=900:
        bg1Y = -900
        bg2Y = 0
    if bg2Y > 900:
        bg2Y = -900
        bg1Y = 0
    #frame 지정 (7)
    fps = clock.tick (30) #화면에 초당 프레임수 30 
    #현재 프레임이 얼마인지 확인 
    #print("fps:", str(clock.get_fps()))
    ey+=3
    for event in pygame.event.get(): #가져와서 한개 꺼내 만약 이벤트 타입이 
        if event.type == pygame.QUIT:  #그 타입이 종류라면 false로 바꾸고 false라면 빠져나옴
            isRunning = False
        if event.type==pygame.MOUSEBUTTONDOWN:
        #print("마우스 클릭됨")           #이벤트 타입이 pygame.MOUSEBUTTONDOWN이면 
            mx, my = pygame.mouse.get_pos() #마우스 클릭한 지점에 
            mList.append(Missle(mx,my)) #클릭하면 #미사일 객체를 만들어서 mx, my함 
    
        screen.blit(enemyship2,(ex,ey))
#배경 그리기 
    screen.blit(bg1,(0,bg1Y)) #0,0자리에 그려    #(3)
    screen.blit(bg2,(0,bg2Y)) #0,0자리에 그려    #(3)
#미사일 그리기 
    

    for m in mList:
        screen.blit(missile,(m.x,m.y)) #원래 좌표였는데 mx,my로 
        # m[1]-= 2
        m.y -= 5 
        if m.y <= -50:
            mList.remove(m) #만약 y값이 -50보다 작아지면 이거 리스트해서 리무브하자 
            del(m) #메모리상에서 없애버림. 메모리상에 남아있는 애들이 없게, 느리지는 현상 없애줌 
    #미사일과 적우주선간 충돌 발생 여부 체크하는 함수를 호출
    #collsion() #내 미사일배열과 적 미사일배열 비교햐서 맞았어, 안 맞았어  
    collision()
    
    if cnt %4 == 0: 
        screen.blit(enemyship0,(ex-25,ey-25))
    elif cnt %4 == 1: 
        screen.blit(enemyship1,(ex-25,ey-25))
    elif cnt %4 == 2:
        screen.blit(enemyship2,(ex-25,ey-25))
    elif cnt %4 == 3:
        screen.blit(enemyship3,(ex-25,ey-25))


#클릭하면 append 
    if cnt %4 == 0: #(4)
        screen.blit(player1,(px-25,py-25)) #(4)
    #(3)
    elif cnt %4 == 1: 
        screen.blit(player2,(px-25,py-25)) #(3)
    elif cnt %4 == 2:
        screen.blit(player3,(px-25,py-25)) #(3)
    elif cnt %4 == 3:
        screen.blit(player4,(px-25,py-25))#(3) (9)-25

    
    
    #마우스 좌표 구하기 (8)
    #print(pygame.mouse.get_pos()) 
    px, py =pygame.mouse.get_pos()  #마우스 따라서 움직임(9) 
    pygame.display.update()  #화면에 다시 그려 #무한 반복  

pygame.quit() #  끝냄 


#밑에 내려오게 
#총으로 쏴서 맞히기 