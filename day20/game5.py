import pygame #pygame을 불러온다. 
import random #random을 불러온다. 
pygame.init() #int해야 초기화  

screen_width = 1200   #1200을 screen_width에 넣는다. 스크린의 너비값(x값)
screen_height = 800   #800을 screen_height에 넣는다. 스크린의 높이값(y값) 
#배경 이미지 객체 
bg = pygame.image.load("e:/dev/python_workspace/img/img/bg.jpg")  #pygame으로 image를 e:/dev/python_workspace/img/img/bg.jpg에서 load하고 bg에 대입  
bg = pygame.transform.scale(bg,(1200,800)) #pygame으로 크기를 옮기는데 bg의 x측을 1200으로 하고 y측을 800으로 한다. 

ball = pygame.image.load("e:/dev/python_workspace/img/img2/gold.png")  #pygame으로 이미지를 업로드하는데 e:/dev/python_workspace/img/img2/gold.png에서 하고 그리고 ball에 대입해라.  
ball = pygame.transform.scale(ball,(100,100)) #pygame을 대상으로 크기를 조정하는데 ball을 x측 100으로 하고 y측 100으로 해라.그리고 ball에 대입  
screen = pygame.display.set_mode((screen_width,screen_height)) #pygame을 대상으로 x측을 screen_width로 y측을 screen_height로 mode를 지정해서 나타내라(display)


bx = 600  #공이 튕기면서 이동해야 해서 #ball의 x좌표를 600으로 함. 600을 bx에 대입 
by = 400 #좌표줌.    #400을 by에 대입   #ball의 y좌표를 400으로 함. 400을 by에 대입 
inc_x = random.randint(-10,10) #속도줄려면         #increase x를 나타내는 inc_x에 -10에서 10사이의 수에서 램덤하게 수를 뽑아냄. 
inc_y = random.randint(-10,10)                    #increase y를 나타내는 inc_y에 -10에서 10사이의 수에서 램덤하게 수를 뽑아냄. 
pygame.display.set_caption("핑퐁")                #pygame으로 창의 틀을 핑퐁으로 나타내라. 
#시계변수
clock = pygame.time.Clock()                       #pygame으로   #얘가 뭐였지? 
isRunning = True #반복함                           #true를 isRunning에 대입. 
def changeDirection(x,y,ix,iy): #ix는 inc_x        #changeDirection이라는 함수를 
    #화면 위쪽 벽에 맞으면 튕겨나가게 설정 
    #y가 0에 닿으면 
    if y <= 3 or y>=780: #0이면 너무 붙어있는 것 같으니까  #한번에 쓸수 있음 
        #벽에 감으면 5씩감소 닿으면 5씩 증가 
        iy = -iy #화면에 y가 거의 3정도까지 닿음. 
    if x <=3 or x >= 1150:
        ix =-ix #ix의 값을 -ix로 바꿈 
    return ix,iy
    # if y >= 780:
    #     iy = -iy 
    # return ix,iy 


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
    
    screen.blit(bg,(0,0)) 
    screen.blit(ball,(bx,by))
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