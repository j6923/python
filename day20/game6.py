import pygame
import random
pygame.init() #int해야 초기화 

screen_width = 1200
screen_height = 800
#배경 이미지 객체 
bg = pygame.image.load("e:/dev/python_workspace/img/img/bg.jpg")
bg = pygame.transform.scale(bg,(1200,800))

wall = pygame.image.load("e:/dev/python_workspace/img/wall.png") 
wall = pygame.transform.scale(wall,(800,400))
ball = pygame.image.load("e:/dev/python_workspace/img/img2/gold.png")
ball = pygame.transform.scale(ball,(100,100))
net1 = pygame.image.load("e:/dev/python_workspace/img/net1.png")
net = pygame.transform.scale(net1,(300,600))
screen = pygame.display.set_mode((screen_width,screen_height))

#공과의 충돌테스트 
def pythagoras(x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)) #아래 피타고라스 쓰기 위해 만듦

dis = pythagoras(sx,sy,m.x,m.y)
if dis<30:
    print(dis)


bx = 600  #공이 튕기면서 이동해야 해서 
by = 600 #좌표줌. 
inc_x = random.randint(-10,10) #속도줄려면 
inc_y = random.randint(-10,10)
pygame.display.set_caption("가짜 벽돌깨기")
#시계변수
clock = pygame.time.Clock()

isRunning = True #반복함 
def changeDirection(x,y,ix,iy): #ix는 inc_x
    #화면 위쪽 벽에 맞으면 튕겨나가게 설정 
    #y가 0에 닿으면 
    if y <= 8 or y>=700: #0이면 너무 붙어있는 것 같으니까  #한번에 쓸수 있음 
        #벽에 감으면 5씩감소 닿으면 5씩 증가 
        iy = -iy #화면에 y가 거의 3정도까지 닿음. 
    if x <=3 or x >= 1150:
        ix =-ix #ix의 값을 -ix로 바꿈 
    return ix,iy #ix, iy의 값을 반환해라 
    # if y >= 780:
    #     iy = -iy 
    # return ix,iy 
#바 좌표 변수  #왜 먼저 좌표넣어줘야 움직임? 
sx = 300
sy = 600 
#왜 어떤 것은 함수로 어떤 것은 class? 차이가 뭐임? 
class wall:
    def __init__(self,sx,sy)
    


    
    
while True: #이거해야 꺼지지 않음 
    # bx -=2 # x좌표반복하면서 2씩 감소하니까 위로 올라감 
    bx -= inc_x #increase x x는 
    by -= inc_y #양수냐 음수냐에 따라 방향 결정 

    fps = clock.tick(30)#화면의 초당 프레임수 

    inc_x,inc_y = changeDirection(bx,by,inc_x,inc_y)
  #inc_x, inc_y 로 해서 닿으면
  #아랫쪽 바닥 부딪치면 튕겨나가게 y값 

    for event in pygame.event.get(): #이벤트 가져옴 
        if event.type == pygame.QUIT: #이벤트가 종류이벤트이면 빠져나감
            isRunning = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            sx, sy = pygame.mouse.get_pos()
                

    sx, sy = pygame.mouse.get_pos()#얘가 있어야 실행됨. 


    #리스트에 담아서 피타고라스 정의해서 하나씩 비교해서 없어지는 것 






    screen.blit(bg,(0,0)) 
    
    screen.blit(ball,(bx,by))
    screen.blit(wall,(200,-10))
    screen.blit(net1,(sx,sy))
    pygame.display.update() #화면 잠깐 떳다가 꺼짐 

#램덤하게 사방으로 



pygame.quit()



#벽돌깨기 
#--아래만 풀어줘서 들어가게 
#하면 됨 
#아래 튕기게 

#내바 컴퓨터 바 컴퓨터 자동으로 왔다갔다 
#나만 왔다갔다 상대방쪽으로 

#이 바가 여기까지 오면 반대로 가게 부호 반대로 
#피타고라스 정의해서 맞으면 어떻게 되는지 처리 




# pyinstaller--hidden-import-pkg_resources.py2_warn-w-F newGame10.py

# apk ---- 안드로이드 패키지 

# 개발자모듈 


# 자바 --- 디컴파일 시킬 수있음 디비 어디쓰고 있는지 apk 하면 게임 

# *소스 분석 ----- 해킹 리버신데어링 공부하는 거는 불법아니지만 상업화는 안됨.
