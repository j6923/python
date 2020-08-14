import pygame #pygame을 불러옴. 

pygame.init() #int해야 초기화 

screen_width = 1200 #스크린의 너비에 1200대입 
screen_height = 800 #스크린의 높이를 800에 대입 

screen = pygame.display.set_mode((screen_width,screen_height)) #playgame함수로 현재 display화면에 지정하는데, 너비, 높이로 display화면에 모드 설정. 
isRunning = True #반복함 
while True: #이거해야 꺼지지 않음 
    for event in pygame.event.get(): #이벤트 가져옴 
        if event.type == pygame.QUIT: #이벤트가 종류이벤트이면 빠져나감
            isRunning = False #isRunning이 False #반복 안함. 
    pygame.display.update() #화면 잠깐 떳다가 꺼짐 





pygame.quit()  #pygame을 끝낸다. 
