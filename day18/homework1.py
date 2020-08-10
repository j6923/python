import pygame   #pygame함수를 외부에서 가져온다. 
import random
pygame.init() #초기화한다. 


screen_width = 1200  #스크린의 너비를 1200으로 한다. 
screen_height = 800  #스크린의 높이를 800으로 한다. 
screen = pygame.display.set_mode((screen_width,screen_height)) #스크린을 띄운다. 
pygame.display.set_caption("짝퉁 고군분투")

#배경이미지를 나타낸다. 
bg1 = pygame.image.load("e:/dev/python_workspace/img/bac/bg1.jpg")
bg2 = pygame.image.load("e:/dev/python_workspace/img/bac/bg2.jpg")
#배경이미지의 크기를 조절한다. 
bg1 = pygame.transform.scale(bg1,(1200,800))
bg2 = pygame.transform.scale(bg2,(1200,800))
bg1x = 0 
bg2x = 1200 #

run1 = pygame.image.load("e:/dev/python_workspace/img/bac/run1.png")
run2 = pygame.image.load("e:/dev/python_workspace/img/bac/run2.png")
run3 = pygame.image.load("e:/dev/python_workspace/img/bac/run3.png")
rx = 100
ry = 500

coin1 = pygame.image.load("e:/dev/python_workspace/img/img2/gold.png")
coin2 = pygame.image.load("e:/dev/python_workspace/img/img2/silver.png")
CoinList = []


count = 0 
clock = pygame.time.Clock() #왜 있었지? 
isRunning = True     
cnt = 0 
px = 500
while isRunning: #화면을 계속해서 보게 해준다. 
    cnt += 1
    bg1x-=2   #왜 -2? 그리고 왜 - 
    bg2x-=2    #while문에 넣어야 반복되면서 바뀜 
    if bg1x <= -1200:   #만약 bg1x가 -1200보다 작거나 같으면 
        bg1x = 1200     #bg1x는 1200에 놓는다. 
        bg2x = 0        #bg2x는 0에 놓는다. 
    if bg2x <= -1200:     #만약 bg2x가 -1200보다 작거나 같으면 
        bg2x =1200      #bg1x는 1200에 놓는다.
        bg1x = 0 
    fps = clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False 
    if cnt %50==0:
        CoinList.append([1200,random.randint(300,500)]) #coin만들어지는 것 
    print(CoinList)
    screen.blit(bg1,(bg1x,0)) #배경이 나오게 한다. 
    screen.blit(bg2,(bg2x,0))  #여기를 바꿔야 화면이 바뀜 
    for coin in CoinList:
        screen.blit(coin1,(coin[0],coin[1]))
        coin[0]-=2
    
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
    # keys = pygame.key.get_pressed()
    
    # if keys[pygame.K_LEFT] ==1:
    #     rx  -=5 

    # if keys[pygame.K_UP] == 1:
    #     ry -= 5

    # if keys[pygame.K_RIGHT]==1:
    #     rx += 5 
    
    # if keys[pygame.K_DOWN] ==1:
    #     ry += 5 


    

    pygame.display.update() #들여쓰기 

pygame.quit() #게임을 끝낸다. 


#스페이스 누르면 점프하게 한다. 
#코인을 램덤하게 넣는다. 



#고칠 것 
#마우스 누르면 점프 