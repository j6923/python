import pygame #pygame을 불러온다. 
import random #random을 불러온다. 
pygame.init() #int해야 초기화 

screen_width = 1200  #1200을 스크린 너비인 screen_width에 대입해라. 
screen_height = 800  # 800을 스크린 높이인 screen_height에 대입해라. 
#배경 이미지 객체 
bg = pygame.image.load("e:/dev/python_workspace/img/img/bg.jpg") #pygame을 대상으로 이미지를 하는데 "e:/dev/python_workspace/img/img/bg.jpg"
#에서 이미지를 가져와라 (다시보기 )그리고 bg에 대입해라. 
bg = pygame.transform.scale(bg,(1200,600)) # bg(배경)를 1200,600의 크기로 옮기되 pygame으로 해라. 그리고 bg에 대입해라.  
ball = pygame.image.load("e:/dev/python_workspace/img/img2/gold.png") #pygame을 대상으로 이미지를 load하는데 "e:/dev/python_workspace/img/img2/gold.png"
#에서 해라.
ball = pygame.transform.scale(ball,(100,100)) #pygame을 대상으로 transform(이동)을 하는데 크기를 하는데 공을 x좌표 100,y좌표 100으로 옮겨라, 그리고 그 값을 ball에 대입해라(다시 보기) 
screen = pygame.display.set_mode((screen_width,screen_height)) #pygame을 나타내되 mode를 설정해라 너비(x축)를 변수인 screen_width으로 하고 높이(y축)을 변수인 screen_height로 해라. (다시보기)

isRunning = True #반복함 
bx = 600  #공이 튕기면서 이동해야 해서 
by = 400 #좌표줌. 
inc_x = random.randint(-10,10) #속도줄려면 #inc_x에 random.randint함수를 사용하여 -10에서 10사이의 값으로 램덤하게 부여한다.  
inc_y = random.randint(-10,10) #inc-y(increase y)에 random.randint함수를 사용하여 -10에서 10사이의 값으로 램덤하게 부여한다. 
pygame.display.set_caption("핑퐁") #pygame에 display해서 창틀의 머릿말을 문자열 핑퐁으로 변경한다. 

#배경 이미지 객체 





while True: #이거해야 꺼지지 않음 
    # bx -=2 # x좌표반복하면서 2씩 감소하니까 위로 올라감 
    by -= inc_x #increase x x는 
    by -= inc_y #양수냐 음수냐에 따라 방향 결정 
    for event in pygame.event.get(): #이벤트 가져옴 
        if event.type == pygame.QUIT: #이벤트가 종류이벤트이면 빠져나가면 
            isRunning = False #isRunning이 거짓이됨. 그래서 isRunning이 멈춤 
    screen.blit(bg,(0,0))  #스크린이 나타나는 것을 그림 bg가 x값 0, y값 0에 나타내라. 
    screen.blit(ball,(bx,by)) #공 그림인 ball을 x좌표를 bx의 변수값으로 y축의 값을 by의 값으로 스크린에 나타내라. #위의 변수가 screen이어서 screen으로 썼나? (다시보기 )
    pygame.display.update() #화면 잠깐 떳다가 꺼짐  #화면을 갱신한다. 

#램덤하게 사방으로 



pygame.quit() #pygame을 끝낸다. 
