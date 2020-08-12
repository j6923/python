import pygame #pygame을 불러온다. 
import random #random을 불러온다. 
pygame.init() #int해야 초기화 

screen_width = 1200  #1200을 스크린 너비인 screen_width에 대입해라. 
screen_height = 800  # 800을 스크린 높이인 screen_height에 대입해라. 
#배경 이미지 객체 
bg = pygame.image.load("e:/dev/python_workspace/img/img/bg.jpg") #pygame을 대상으로 이미지를 하는데 "e:/dev/python_workspace/img/img/bg.jpg"
#에서 이미지를 가져와라 (다시보기 )그리고 bg에 대입해라. 
bg = pygame.transform.scale(bg,(1200,600)) # bg를 1200,600의 크기로 옮기되 pygame으로 해라. 그리고 bg에 대입해라.  
ball = pygame.image.load("e:/dev/python_workspace/img/img2/gold.png") #pygame을 대상으로 이미지를 load하는데 "e:/dev/python_workspace/img/img2/gold.png"
#에서 해라.
ball = pygame.transform.scale(ball,(100,100)) 
screen = pygame.display.set_mode((screen_width,screen_height))

isRunning = True #반복함 
bx = 600  #공이 튕기면서 이동해야 해서 
by = 400 #좌표줌. 
inc_x = random.randint(-10,10) #속도줄려면 
inc_y = random.randint(-10,10)
pygame.display.set_caption("핑퐁")

#배경 이미지 객체 





while True: #이거해야 꺼지지 않음 
    # bx -=2 # x좌표반복하면서 2씩 감소하니까 위로 올라감 
    by -= inc_x #increase x x는 
    by -= inc_y #양수냐 음수냐에 따라 방향 결정 
    for event in pygame.event.get(): #이벤트 가져옴 
        if event.type == pygame.QUIT: #이벤트가 종류이벤트이면 빠져나감
            isRunning = False 
    screen.blit(bg,(0,0)) 
    screen.blit(ball,(bx,by))
    pygame.display.update() #화면 잠깐 떳다가 꺼짐 

#램덤하게 사방으로 



pygame.quit()
