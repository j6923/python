#이번에는 종게임 

#게임의 기본 틀 
import pygame


#초기화 하기전 초기화 해줘야함. 
pygame.init()

screen_width = 600  #너비 높임 
screen_height = 900

screen = pygame. display.set_mode((screen_width,screen_height)) #기본으로 설정 

isRunning = True   

pygame. display. set_caption("우주 전쟁")
#배경 이미지 객체(1)
bg = pygame.image.load("e:/dev/python_workspace/img/img2/space.jpg")
#캐릭터 우주선 객체     

player1 = pygame.image.load("e:/dev/python_workspace/img/img2/player1.png")
player2 = pygame.image.load("e:/dev/python_workspace/img/img2/player2.png")
player3 = pygame.image.load("e:/dev/python_workspace/img/img2/player3.png")
player4 = pygame.image.load("e:/dev/python_workspace/img/img2/player4.png")

#이미지 크기를 화면의 크기로 변환 
bg = pygame.transform.scale(bg,(600,900)) #이미지 속성 보면 사진크기 알 수있음. 사진 찍으면 장비에서 찍었늦지 gps좌표 찍힘, 해상도 시간 
#여기 사이에 코드가 반복 되어야 종료하기전 계속 반복함. 
#카운터 변수 적용 (4)
cnt = 0
while isRunning:
    cnt += 1
    for event in pygame.event.get(): #가져와서 한개 꺼내 만약 이벤트 타입이 
        if event.type == pygame.QUIT:  #그 타입이 종류라면 false로 바꾸고 false라면 빠져나옴
            isRunning = False
#배경 그리기 
    screen.blit(bg,(0,0)) #0,0자리에 그려    #(3)
    if cnt %4 == 0: #(4)
        screen.blit(player1,(250,000)) #(4)
    #(3)
    elif cnt %4 == 1: 
        screen.blit(player2,(250,000)) #(3)
    elif cnt %4 == 2:
        screen.blit(player3,(250,000)) #(3)
    elif cnt %4 == 3:
        screen.blit(player4,(250,000))#(3)
    


    pygame.display.update()  #화면에 다시 그려 #무한 반복  

pygame.quit() #  끝냄 