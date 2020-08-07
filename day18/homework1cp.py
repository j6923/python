import pygame   #pygame함수를 외부에서 가져온다. 

pygame.init() #초기화한다. 


screen_width = 1200  #스크린의 너비를 1200으로 한다. 
screen_height = 800  #스크린의 높이를 800으로 한다. 

screen = pygame.display.set_mode((screen_width,screen_height))
#스크린을 표시 
bg1 = pygame.image.load("e:/dev/python_workspace/img/bac/bg1.jpg")
screen.blit(bg1,(0,0))
isRunning = True
cnt = 0 
px = 500
while isRunning:
    cnt += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False 


#배경화면을 삽입한다. 

pygame.display.update()

pygame.quit() #게임을 끝낸다. 
