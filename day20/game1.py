import pygame  #pygame을 불러온다. 

pygame.init() #int해야 초기화 

screen_width = 1200    #스크린의 너비를 1200으로 한다. 
screen_height = 800    #스크린의 높이를 800으로 한다. 

screen = pygame.display.set_mode((screen_width,screen_height))
#pygame을 display해서 mode를 set하는데 스크린의 너비와 높이로 한다. 
while True: #이거해야 꺼지지 않음 
    pygame.display.update() #화면 잠깐 떳다가 꺼짐 




pygame.quit()   #pygame을 끝낸다. 
