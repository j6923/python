import pygame   #pygame을 불러라. 
import random #random을 불러라. 
pygame.init() #int해야 초기화  #pygame을 초기화해라, 함수여서 #__안 들어감. 

screen_width = 1200  #1200을 screen_width라는 변수에 대입해라. 
screen_height = 800   #800을 screen_height라는 변수에 대입해라. 
#배경 이미지 객체 
bg = pygame.image.load("e:/dev/python_workspace/img/img/bg.jpg")  #pygame의 이미지를 로드한다, "e:/dev/python_workspace/img/img/bg.jpg"에서 그리고 bg에 대입한다.  
bg = pygame.transform.scale(bg,(1200,600))  #bg를 x좌표 1200, y좌표 600으로 pygame의 크기를 옮겨라. 

ball = pygame.image.load("e:/dev/python_workspace/img/img2/gold.png")   #---의 이미지를 로드해서 ball에 넣는다.  #중복함수가 아니면 괜찮음 앞에서부터 해석 
ball = pygame.transform.scale(ball,(100,100)) #ball을 x좌표 100, y좌표 100으로 크기를 옮겨서 pygame으로 ball에 넣는다. (다시보기)
screen = pygame.display.set_mode((screen_width,screen_height)) #x좌표를 screen_width로 하고 y좌표를 screen_height로 해서 mode를 지정한다 그리고 나타낸다. (다시보기)


bx = 600  #공이 튕기면서 이동해야 해서 
by = 400 #좌표줌. 
inc_x = random.randint(-10,10) #속도줄려면 함수 random.randint를 사용해서 -10과 10사이의 정수값으로 램덤하게 해서 inc_x에 넣는다. 
inc_y = random.randint(-10,10)  #random.randint를 사용해서 -10과 10사이의 정수값으로 램덤하게 해서 inc_y에 넣는다. 
pygame.display.set_caption("핑퐁") #문자열 핑퐁으로 창틀의 제목을 지정하되 나타내라 pygame으로 (다시보기)
#시계변수
clock = pygame.time.Clock()   #Clock으로 time을 (다시보기)
isRunning = True #반복함 
def changeDirection(x,y,ix,iy): #ix는 inc_x     #changeDirection이라는 함수를 만들어서 x,y,ix,iy를 매게변수로 한다. #뭐하는 애였지(다시보기) 
    #화면 위쪽 벽에 맞으면 튕겨나가게 설정 
    #y가 0에 닿으면 
    if y <= 3: #0이면 너무 붙어있는 것 같으니까     만약 y가 3보다 작거나 같으면 
        #벽에 감으면 5씩감소 닿으면 5씩 증가 
        iy = -iy #화면에 y가 거의 3정도까지 닿음.   -iy을 iy에 대입한다. 
    return ix,iy    #ix와 iy의 값을 리턴한다.(다시보기) 
while True: #이거해야 꺼지지 않음 
    # bx -=2 # x좌표반복하면서 2씩 감소하니까 위로 올라감 
    bx -= inc_x #increase x x는 
    by -= inc_y #양수냐 음수냐에 따라 방향 결정 

    fps = clock.tick(30)#화면의 초당 프레임수 

    inc_x,inc_y = changeDirection(bx,by,inc_x,inc_y) #changeDirection의 이게 뭐지? 
  #inc_x, inc_y 로 해서 닿으면
    for event in pygame.event.get(): #이벤트 가져옴 
        if event.type == pygame.QUIT: #이벤트가 종류이벤트이면 빠져나감
            isRunning = False #isRunning이 False가 되면서 빠져나감. 
    
    screen.blit(bg,(0,0))   #bg를 x축을 0으로 y축을 0으로 해서 나타낸다 스크린에. 
    screen.blit(ball,(bx,by)) #ball를 x축을 bx로 하고 y축을 by로 해서 나타낸다 스크린에. 
    pygame.display.update() #화면 잠깐 떳다가 꺼짐 

#램덤하게 사방으로 



pygame.quit() #pygame을 끝낸다. 
