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
#미사일 객체 
missile = pygame.image.load("e:/dev/python_workspace/img/img2/missile1.png")


#크기 조정 
player1 = pygame.transform.scale(player1,(50,50))
player2 = pygame.transform.scale(player2,(50,50))
player3 = pygame.transform.scale(player3,(50,50))
player4 = pygame.transform.scale(player4,(50,50))

#캐릭터 우주선 좌표 변수 (8)
px = 250
py = 800  #그릴 때도 이 좌표 기준으로 그리기 
#이미지 크기를 화면의 크기로 변환(5) 
bg1 = pygame.transform.scale(bg,(600,900)) #이미지 속성 보면 사진크기 알 수있음. 사진 찍으면 장비에서 찍었늦지 gps좌표 찍힘, 해상도 시간 
bg2 = pygame.transform.scale(bg,(600,900)) #이미지 속성 보면 사진크기 알 수있음. 사진 찍으면 장비에서 찍었늦지 gps좌표 찍힘, 해상도 시간 


#시계변수 (6)
clock = pygame.time.Clock()
#미사일 객체 
missile = pygame.image.load("e:/dev/python_workspace/img/img2/missile1.png")

#미사일 좌표 변수 (10)
mx = 250
my = 300
#여기 사이에 코드가 반복 되어야 종료하기전 계속 반복함. 
#카운터 변수 적용 (4)
cnt = 0
#배경 x,y좌표 
bg1Y=0
bg2Y=-900

my-=3#(10)

while isRunning:
    cnt += 1
    bg1Y+= 2
    bg2Y+= 2
    if bg1Y >=900:
        bg1Y = -900
        bg2Y = 0
    if bg2Y > 900:
        bg2Y = -900
        bg1Y = 0
    #frame 지정 (7)
    fps = clock.tick (30) #화면에 초당 프레임수 30 
    #현재 프레임이 얼마인지 확인 
    #print("fps:", str(clock.get_fps()))
    for event in pygame.event.get(): #가져와서 한개 꺼내 만약 이벤트 타입이 
        if event.type == pygame.QUIT:  #그 타입이 종류라면 false로 바꾸고 false라면 빠져나옴
            isRunning = False
    if event.type==pygame.MOUSEBUTTONDOWN:
        #print("마우스 클릭됨")           #이벤트 타입이 pygame.MOUSEBUTTONDOWN이면 
        mx, my = pygame.mouse.get_pos() #마우스 클릭한 지점에 
#배경 그리기 
    screen.blit(bg1,(0,bg1Y)) #0,0자리에 그려    #(3)
    screen.blit(bg2,(0,bg2Y)) #0,0자리에 그려    #(3)
#미사일 그리기 
    screen.blit(missile,(mx,my)) #원래 좌표였는데 mx,my로 

    if cnt %4 == 0: #(4)
        screen.blit(player1,(px-25,py-25)) #(4)
    #(3)
    elif cnt %4 == 1: 
        screen.blit(player2,(px-25,py-25)) #(3)
    elif cnt %4 == 2:
        screen.blit(player3,(px-25,py-25)) #(3)
    elif cnt %4 == 3:
        screen.blit(player4,(px-25,py-25))#(3) (9)-25
    #마우스 좌표 구하기 (8)
    #print(pygame.mouse.get_pos()) 
    px, py =pygame.mouse.get_pos()  #마우스 따라서 움직임(9) 
    pygame.display.update()  #화면에 다시 그려 #무한 반복  

pygame.quit() #  끝냄 
