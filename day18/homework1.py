import pygame   #pygame함수를 외부에서 가져온다. 

pygame.init() #초기화한다. 


screen_width = 1200  #스크린의 너비를 1200으로 한다. 
screen_height = 800  #스크린의 높이를 800으로 한다. 

screen = pygame.display.set_mode((screen_width,screen_height)) #스크린을 띄운다. 

#배경이미지를 나타낸다. 
bg1 = pygame.image.load("e:/dev/python_workspace/img/bac/bg1.jpg")
bg2 = pygame.image.load("e:/dev/python_workspace/img/bac/bg2.jpg")
run1 = pygame.image.load("e:/dev/python_workspace/img/bac/run1.png")
run2 = pygame.image.load("e:/dev/python_workspace/img/bac/run2.png")
run3 = pygame.image.load("e:/dev/python_workspace/img/bac/run3.png")

#배경이미지의 크기를 조절한다. 
bg1 = pygame.transform.scale(bg1,(1200,800))
bg2 = pygame.transform.scale(bg2,(1200,800))

rx = 590
ry = 590
count = 0 
clock = pygame.time.Clock()
pygame.display.set_caption("짝퉁 고군분투")
isRunning = True     
cnt = 0 
px = 500
while isRunning: #화면을 계속해서 보게 해준다. 
    cnt += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False 
    screen.blit(bg1,(0,0)) #배경이 나오게 한다. 
    screen.blit(bg2,(0,0))
    #캐릭터가 나오게 한다. 
    # screen.blit(run1,(590,590))
    # screen.blit(run2,(590,590))
    # screen.blit(run3,(590,590))

    
#3의 배수로 해서 
    if cnt%3 == 0:
        screen.blit(run1,(rx,ry))
    elif cnt%3 == 1:
        screen.blit(run2,(rx,ry))
    else:
        screen.blit(run3,(rx,ry))
    #if keys[]
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] ==1:
        rx  -=5 

    if keys[pygame.K_UP] == 1:
        ry -= 5

    if keys[pygame.K_RIGHT]==1:
        rx += 5 
    
    if keys[pygame.K_DOWN] ==1:
        ry += 5 


    

    pygame.display.update() #들여쓰기 

pygame.quit() #게임을 끝낸다. 
