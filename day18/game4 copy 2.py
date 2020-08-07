import pygame  #기본구조 

#쓰기 전에 초기화 항상 해줘야 함

pygame. init() #기본구조 

#화면 크기 지정함(밑에)
screen_width = 1200 #기본구조 
screen_height = 800  #기본구조

screen = pygame.display.set_mode((screen_width,screen_height)) #기본구조 
#배경 그리기 
#bg = 배경이미지   
bg1 = pygame.image.load("e:/dev/python_workspace/img/img/bg.jpg") #배경을 넣음 
bg2 = pygame.image.load("e:/dev/python_workspace/img/img/bg.jpg") #배경을 넣음 
bg1 = pygame.transform.scale(bg1,(1200,800))
bg2 = pygame.transform.scale(bg2,(1200,800))
rabbit1 = pygame.image.load("e:/dev/python_workspace/img/img/rabbit1.png") #토끼1을 넣음
rabbit2 = pygame.image.load("e:/dev/python_workspace/img/img/rabbit2.png") #토끼 2을 넣음 
#토끼의 사이즈 줄이기 
rabbit1 = pygame.transform.scale(rabbit1,(100,100)) #100,100은 너비, 높이의 값   
rabbit2 = pygame.transform.scale(rabbit2,(100,100))
#시계변수 
 


isRunning = True  #게임을 계속 진행할지, 중지 할지를 결정하는 변수 
                   #flag#플레그성 반복할건지 빠져나올건지 결정하는 변수를 플래그성 변수라고 한다.
pygame.display.set_caption("토끼 사냥") #창 틀에 토끼사냥이라고 적음 

cnt = 0 #반복문 증가할 때마다 1씩 증가 
#1번 까박 1번찍고 2번 깜박 2번찍기 
#토끼 위치좌표 
rx = 100  #다른 위치 주면 다른 위치에 감. 토끼의 위치 지정 
ry = 200 
count = 0 
#시계변수
clock = pygame.time.Clock() #배경을 오-왼 토끼가 달리는 것 처럼 보임 
#배경 좌표 
#배경이 끝나 토끼만 그림. 덮어쓰고 또 그림. #그래서 배경 2개 주고 계속 움직임... 계속 움직임, 무한 반복으로 팽스클럴 종 스크롤 게임 다 이럼. 
#배경 좌표
bg1x = 0 
bg2x = 1200 #
while isRunning: #플레그성 반복할건지 빠져나올건지 결정하는 변수를 플래그성 변수라고 한다.isrunning이 플레그성 변수 
    cnt +=1
    bg1x-= 2 
    bg2x-= 2
    if bg1x <= -1200: #2Tlr 3Tlrgkaus vlrtpf dks akwrleh gka 2식 3식하면 픽셀 안 맞기도 함
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
    # if event.type == pygame.KEYUP:
        
        #이벤트 중에 게임 종료 이밴트가 있으면 종료해. 그 다음 반복문 돌아올 때 탈출  클릭 마우스 , 이벤트 들중에 하나 꺼내서 담아서 종료하는 이벤트면 FALSE로 변경 FALSE니까 빠져나옴.
# print(keys[pygame.K_LEFT]) #
    if keys[pygame.K_LEFT] == 1: #왼쪽 화살표 버튼이 눌린상태라면 
       
            rx -= 5    #rx를 -5로 옮김 
         
      
    if keys[pygame.K_UP] == 1: #위쪽 화살표 버튼이 눌린상태라면 
        
            ry -= 5       #ry를 -5로 옮김 
            
    if keys[pygame.K_RIGHT] == 1: #오른쪽 화살표 버튼이 눌린상태라면 
        
            rx += 5         #rx를 +5로 옮김 
           
    if keys[pygame.K_DOWN] == 1:   #아랫쪽 화살표 버튼이 눌린상태라면 
         
            ry += 5                #ry를 +5로 옮김 
        
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
    screen.blit(bg1,(bg1x,0)) #bg배경을 변수로 bgx, bgy로 선언한다. #배경이 오른쪽으로 가면 이상함, y좌표 안 달라지고 x만 달라짐 그래서 0
    screen.blit(bg2,(bg2x,0)) #y좌표 안달라지고 x만 달라짐. 
    #현재 창 0,0기준으로 좌측 상단점 시작해서 배경 그려 
    if cnt%2 ==0: #홀수 짝수 해서 움직이게 
        screen.blit(rabbit1,(rx,ry)) #100,200 
    else:
        screen.blit(rabbit2,(rx,ry))
    
    
    pygame.display.update() #

pygame.quit() #가장 기본구조 