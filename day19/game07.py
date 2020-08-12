import pygame                       #pygame 모듈을 가져온다. 
import math

pygame.init()  #pygame을 초기화한다.  #함수로 만들어 놓고 self init 

# 토끼의 중심좌표와 마우스 클릭 위치의 거리를 구하기 

def pythagoras (x1,y1, x2, y2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))




# 배경음악 

pygame.mixer.music.load("e:/dev/python_workspace/sounds/backsound.wav")
pygame.mixer.music.set_volume(0.5) # 1~0.1

pygame.mixer.music.play(1)

# 화면크기 
screen_width = 1200
screen_height= 800

screen = pygame.display.set_mode((screen_width, screen_height))

# 총 소리 객체 
fSound = pygame.mixer.Sound("e:/dev/python_workspace/sounds/fire.wav")
fSound.set_volume(0.2)

# 비명 사운드 객체 
screamSound = pygame.mixer.Sound("e:/dev/python_workspace/sounds/scream.wav")
screamSound.set_volume(0.2)


# 배경 이미지 객체 
bg1 = pygame.image.load("e:/dev/python_workspace/img/bg.jpg") 
bg2 = pygame.image.load("e:/dev/python_workspace/img/bg.jpg") 
bg1 = pygame.transform.scale(bg1,(1200,800))
bg2 = pygame.transform.scale(bg2,(1200,800))

# 토끼 이미지 객체 
rabbit1 = pygame.image.load("e:/dev/python_workspace/img/rabbit1.png") 
rabbit2 = pygame.image.load("e:/dev/python_workspace/img/rabbit2.png") 

rabbit1 = pygame.transform.scale(rabbit1,(100,100))
rabbit2 = pygame.transform.scale(rabbit2,(100,100))

# 조준경 이미지 객체 

snipe = pygame.image.load("e:/dev/python_workspace/img/snipe.png") 
# 조준경이 너무 커서 크기를 약간줄임 
snipe = pygame.transform.scale(snipe,(100,100))


isRunning = True  # 게임을 계속 진행할지 , 중지 할지를 결정하는 변수 
                  # flag 

pygame.display.set_caption("토끼 사냥")

cnt = 0 
# 토끼 위치 좌표 
rx = 100
ry = 200

# 조준경의 좌표 
snipeX = 300
snipeY = 300 


# 구멍이미지 객체 
holeImg  = pygame.image.load("e:/dev/python_workspace/img/hole.png") 
holeImg = pygame.transform.scale(holeImg,(10,10))

count = 0 
# 시계 변수 
clock = pygame.time.Clock()

# 홀 x, y 좌표 
holeX = 200
holeY = 200

# 배경 좌표 
bg1X = 0
bg2X = 1200

while isRunning:
    cnt += 1
    bg1X -= 2
    bg2X -= 2
    if bg1X <= -1200:
        bg1X = 1200
        bg2X = 0
    if bg2X <= -1200:
        bg2X = 1200
        bg1X = 0
    
    # Frame 지정 
    fps = clock.tick(30) # 화면의 초당 프레임수 30 

    # 프레임이 얼마 인지 확인하려면 
    #print(" fps : " + str(clock.get_fps()))



    for event in pygame.event.get():  # 이벤트 모으기 
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.MOUSEBUTTONUP:
            fSound.play()
            holeX, holeY = pygame.mouse.get_pos()
            dis = pythagoras(holeX, holeY, rx+50, ry+50 )
            # print(dis)
            #만약 dis 의 작으면 맞은것
            # 크면 안맞은것 
            if dis<= 50:
                print("아 아퍼.. ")
                screamSound.play()



            


    #print(pygame.mouse.get_pos())

    #print(pygame.mouse.get_pressed())   
    snipeX , snipeY = pygame.mouse.get_pos()

    



    keys = pygame.key.get_pressed()

    #print(keys[pygame.K_LEFT])
    if keys[pygame.K_LEFT] == 1: # 왼쪽 화살표 버튼이 눌린상태라면 
        if  3 <= rx <= 1105:
            rx -= 5
    if keys[pygame.K_UP] == 1:
        if  3<= ry <= 705:
            ry -= 5
    if keys[pygame.K_RIGHT] == 1:
        if  0 <= rx <= 1100:
            rx += 5
    if keys[pygame.K_DOWN] == 1:
        if  0<= ry <= 700:
            ry += 5
    # 1번키를 누르면 음악 중지 
    if keys[pygame.K_1] == 1:
        pygame.mixer.music.stop()
    if keys[pygame.K_2] == 1:
        pygame.mixer.music.play()

    # 2번키를 누르면 음악 플레이 

    #배경 그리기 
    screen.blit(bg1,(bg1X,0)) 
    screen.blit(bg2,(bg2X,0)) 

    if cnt%2 == 0:
        screen.blit(rabbit1,(rx,ry))
    else:
        screen.blit(rabbit2,(rx,ry))

    # 구멍이미지 그리기 
    screen.blit(holeImg, (holeX, holeY))

    # print(cnt)
    screen.blit(snipe,(snipeX-50,snipeY-50))

    pygame.display.update()  # 게임화면을 다시 그리기 




pygame.quit()
