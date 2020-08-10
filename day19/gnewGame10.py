#이번에는 종게임 

#게임의 기본 틀 
import pygame


#초기화 하기전 초기화 해줘야함. 
pygame.init()

screen_width = 600  #너비 높임 
screen_height = 900

screen = pygame.display.set_mode((screen_width,screen_height)) #기본으로 설정 

isRunning = True   

pygame. display.set_caption("우주 전쟁")
#여기 사이으 ㅣ코드가 반복 되어야 종료하기전 계속 반복함. 
while isRunning:
    for event in pygame.event.get(): #가져와서 한개 꺼내 만약 이벤트 타입이 
        if event.type == pygame.QUIT:  #그 타입이 종류라면 false로 바꾸고 false라면 빠져나옴
            isRunning = False

    pygame.display.update()  #화면에 다시 그려 #무한 반복  

pygame.quit() #  끝냄 