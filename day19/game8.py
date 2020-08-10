import pygame  #기본구조 
import math 
#쓰기 전에 초기화 항상 해줘야 함
import random
pygame. init() #기본구조 
#qoruddmadkr background music 

#토끼의 중심좌표와 마우스 클릭 위치의 거리를 구하기 
#토끼의 정중앙좌표와 마우스 클릭 하는 자리는 피타고라스 정리 
def pythagoras(x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)) #(X2-X1)*(X2-X1) Y2-Y1제곱을 더하면 C의 제곱,, 루트 씌워주면됨 
#총알 클릭할 때마다 

#배경음악 
pygame.mixer.music.load("e:/dev/python_workspace/img/sounds/backsound.mp3")
pygame.mixer.music.set_volume(0.2)#0~0.1 볼륨 

pygame.mixer.music.play(1) #1,play once  


#총소리 객체 
fSound=pygame.mixer.Sound("e:/dev/python_workspace/img/sounds/fire.wav")
#비명소리 객체 
screamSound=pygame.mixer.Sound("e:/dev/python_workspace/img/sounds/scream.wav")
#특정 사운드 객체 
fSound.set_volume(0.2)
fSound.play()


#화면 크기 지정함(밑에)
screen_width = 1200 #기본구조 
screen_height = 800  #기본구조

screen = pygame.display.set_mode((screen_width,screen_height)) #기본구조 #스크린넣음??? 
#배경 그리기 
#bg = 배경이미지   
bg1 = pygame.image.load("e:/dev/python_workspace/img/img/bg.jpg") #배경을 넣음 
bg2 = pygame.image.load("e:/dev/python_workspace/img/img/bg.jpg") #배경을 넣음 
bg1 = pygame.transform.scale(bg1,(1200,800)) #1200, 800으로 사이즈 조정 
bg2 = pygame.transform.scale(bg2,(1200,800)) #1200, 800으로 사이즈 조정 

rabbit1 = pygame.image.load("e:/dev/python_workspace/img/img/rabbit1.png") #토끼1을 넣음
rabbit2 = pygame.image.load("e:/dev/python_workspace/img/img/rabbit2.png") #토끼 2을 넣음 
#조준경 이미지 객체 
snipe = pygame.image.load("e:/dev/python_workspace/img/bac/snipe.png")
#구멍이미지 객체 만듦 
holeImg = pygame.image.load("e:/dev/python_workspace/img/bac/hole.png")
#토끼의 사이즈 줄이기 
rabbit1 = pygame.transform.scale(rabbit1,(100,100)) #100,100은 너비, 높이의 값   
rabbit2 = pygame.transform.scale(rabbit2,(100,100))
#조준경이 너무 거서 크기를 약간 줄임 
snipe =pygame.transform.scale(snipe,(100,100))
holeImg = pygame.transform.scale(holeImg,(10,10))

#시계변수 
 


isRunning = True  #게임을 계속 진행할지, 중지 할지를 결정하는 변수 
                   #flag#플레그성 반복할건지 빠져나올건지 결정하는 변수를 플래그성 변수라고 한다.
pygame.display.set_caption("토끼 사냥") #창 틀에 토끼사냥이라고 적음 

cnt = 0 #반복문 증가할 때마다 1씩 증가 
#1번 까박 1번찍고 2번 깜박 2번찍기 
#토끼 위치좌표 
rx = 100  #다른 위치 주면 다른 위치에 감. 토끼의 위치 지정 
ry = 200 
#조준경의 좌표 
snipeX = 300     #변수를 써서 바꿀 
snipeY = 300
#홀 x, y 좌표 
holeX =200 #마우스 클릭하면 
holeY =200
count = 0 
#시계변수
clock = pygame.time.Clock() #배경을 오-왼 토끼가 달리는 것 처럼 보임 
#배경 좌표 
#배경이 끝나 토끼만 그림. 덮어쓰고 또 그림. #그래서 배경 2개 주고 계속 움직임... 계속 움직임, 무한 반복으로 팽스클럴 종 스크롤 게임 다 이럼. 
#배경 좌표
bg1x = 0 
bg2x = 1200 #

#홀리스트만듦
holeList= [] #클릭할 때마다 구멍들을 하나씩 추가.

while isRunning: #플레그성 반복할건지 빠져나올건지 결정하는 변수를 플래그성 변수라고 한다.isrunning이 플레그성 변수 
    cnt +=1
    bg1x-= 2 
    bg2x-= 2
    if bg1x <= -1200: #2Tlr 3Tlrgkaus vlrtpf dks akwrleh gka
        bg1x = 1200
        bg2x = 0
    if bg2x <= -1200:
        bg2x = 1200
        bg1x = 0
    #이벤트가 있으면 
    #frame 지정
    fps = clock.tick(100) #화면에 초당 프레임수 30--괄호안 숫자  , 너무 높으면 정지되어 있는 것처럼 
    #프레임이 얼마인지 확인하려면
    # print("fps :"+str(clock.get_fps()))  #29... 초당 30정도 되는 것 
    for event in pygame.event.get(): #이벤트 모으기  게임에서 다양한 이벤트가 일어나면 모음 for문이니니까 담음, 이벤트 종류 담아서 
        if event.type ==pygame.QUIT: #발생한는 이벤트 1개꺼내서 반복, 종료나오면 종료 
            isRunning = False
        if event.type == pygame.MOUSEBUTTONUP:
            fSound.play()
            holeX,holeY = pygame.mouse.get_pos()
       
    # print(pygame.mouse.get_pressed())#마우스 뭐가 눌렸는지 안 눌렸는지 감지 
    # if event.type == pygame.KEYUP:
        
            #리스트에 있는 애들 반복문으로 한개씩그려주세요. 
            dis = pythagoras(holeX,holeY,rx+50,ry+50)
            #holeList.append((holeX,holeY)) 에 있으면 여기저기 다 뚫림. 어디에 append되어있냐에 따라서 다름. 
            print(dis)
            #만약 dis 의 작으면 맞은것
            #크면 안 맞은것 
        #이벤트 중에 게임 종료 이밴트가 있으면 종료해. 그 다음 반복문 돌아올 때 탈출  클릭 마우스 , 이벤트 들중에 하나 꺼내서 담아서 종료하는 이벤트면 FALSE로 변경 FALSE니까 빠져나옴.
             #추가해야 한개로 추가 가능 
            if dis <= 50:
                print("아, 아퍼")
                screamSound.play()
                #holeList.append((holeX,holeY)) #토끼한테 맞을 때만 구멍꿀림 
                holeList.append((rx+50-holeX,ry+50-holeY)) #토끼를기준으로 얼마만큼 바뀐
                #상처가 따라갔으면 좋겠어요. 총알 화면 절대위치여서 총알 그대로 
                #토끼의 어느위치로 저장하면 상대적위치에 구멍좌표 사용 
        #print("홀 리스트 :", holeList) #프린트되는지 확인하느라고 넣음.  
        #화면의 상대적 위치 --- 토끼원래 위치의 상대적위치 얼마지정해줌 
             
            #구멍이미지 그리기 
            #맞으면 토끼가 램덤위치로 이동 
        
                rx = random.randint(1,1200) #x의 사이좌표 
                ry = random.randint(1,700) #y의 사이좌표   #if안에 들어있어야 맞으면이 됨. 
    keys = pygame.key.get_pressed()#눌러진 애들을 통째로 갖다놓을 수 있음 
            #print("마우스 클릭됨")    
# print(keys[pygame.K_LEFT]) #찍어 봄 
    if keys[pygame.K_LEFT] == 1: #왼쪽 화살표 버튼이 눌린상태라면 
       if 3 <= rx <=1105:
            rx -= 5
         
      
    if keys[pygame.K_UP] == 1:
        if 3 <=ry <= 705:
            ry -= 5
            
    if keys[pygame.K_RIGHT] == 1:
         if 0 <=rx <= 1100:
        
            rx += 5
           
    if keys[pygame.K_DOWN] == 1:
         if 0<=ry <= 700: #창 벋어나지 않음 
            ry += 5

    if keys[pygame.K_1]==1:
        pygame.mixer.music.stop()
    if keys[pygame.K_2]==1:  #it is diffent from A key board num and next key board 아스키코드가 달라서 옆쪽 자판에서는 안됨. 
        pygame.mixer.music.play()
    #press 1 stop music, press 2 play music (1번키를 누르면 음악 플레이) #picture always leftupper is 기준. 그림은 항상 왼쪽상단이 기준  
    #print(pygame.mouse.get_pos()) #마우스 좌표 찍힘   튜플로 되어 있는 것 
    snipeX, snipeY = pygame.mouse.get_pos()#마우스 움직이게 
    keys= pygame.key.get_pressed() #마우스 움직이게 #커서가 그점을 기준으로 좌즉 상단점 
    #좌측 상단점이 좌표값 
 
    # if event.key == pygame.K_LEFT:  #만약에 키보드가 떼지면 
        #     rx-=5
    #elif에서 if로 하면 
   
        

        # elif event.key == pygame.K_UP:
        #     ry -=5
        # elif event.key == pygame.K_RIGHT:
        #     rx += 5
        # elif event.key == pygame.K_DOWN:
        #     ry +=5            
         #게임화면을 다시 그리기 
        #게임이 진행되는 동안 
# pygame.display.update #게임화면을 다시 그리기, 갱신함. 기본구조 
#배경의 좌표 
#배경그리기 
    screen.blit(bg1,(bg1x,0)) #bg배경을 변수로 bgx, bgy로 선언한다. #배경이 오른쪽으로 가면 이상 y좌표 안 달라지고 x만 달라짐 그래서 0
    screen.blit(bg2,(bg2x,0))#배경 그리고 토끼 그림 
    #현재 창 0,0기준으로 좌측 상단점 시작해서 배경 그려 
    if cnt%2 ==0: #홀수 짝수 해서 움직이게  #토끼 그리게  blit 그 사물을 그려 
        screen.blit(rabbit1,(rx,ry)) #100,200 
    else:
        screen.blit(rabbit2,(rx,ry))
    #구멍이미지 그리기 
    for holeX, holeY in holeList:
            screen.blit(holeImg,(rx+50-holeX,ry+50-holeY)) #토끼 50이어서 같은만큼 50넣어줌. 
    
    screen.blit(snipe,(snipeX-50,snipeY-50)) #고정된 것이 아니어서 좌표  
    
#좌표에서 빼는 방법 #그릴때 빼는 방법 커서를 이동  #높이의 절반, 너비의 절반 
    pygame.display.update() #게임화면을 다시 그리기 

pygame.quit() #가장 기본구조 

#토끼 좌측 상단과의 거리와 비교하느라고 좌표값 다름. 
#클릭하는 것은 
#뿅 사라졌다 토끼의 좌표를 램덤해서 이동 --- 
# 