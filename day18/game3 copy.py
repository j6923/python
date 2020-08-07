import pygame  #기본구조 

#쓰기 전에 초기화 항상 해줘야 함

pygame. init() #기본구조 

#화면 크기 지정함(밑에)
screen_width = 1200 #기본구조 
screen_height = 800  #기본구조

screen = pygame.display.set_mode((screen_width,screen_height)) #기본구조 
#배경 그리기 
#bg = 배경이미지   
bg = pygame.image.load("e:/dev/python_workspace/img/img/bg.jpg") #배경을 넣음 
rabbit1 = pygame.image.load("e:/dev/python_workspace/img/img/rabbit1.png") #토끼1을 넣음
rabbit2 = pygame.image.load("e:/dev/python_workspace/img/img/rabbit2.png") #토끼 2을 넣음 
#토끼의 사이즈 줄이기 
rabbit1 = pygame.transform.scale(rabbit1,(100,100)) #100,100은 너비, 높이의 값   
rabbit2 = pygame.transform.scale(rabbit2,(100,100))

isRunning = True  #게임을 계속 진행할지, 중지 할지를 결정하는 변수 
                   #flag#플레그성 반복할건지 빠져나올건지 결정하는 변수를 플래그성 변수라고 한다.
pygame.display.set_caption("토끼 사냥") #창 틀에 토끼사냥이라고 적음 

cnt = 0 #반복문 증가할 때마다 1씩 증가 
#1번 까박 1번찍고 2번 깜박 2번찍기 
#토끼 위치좌표 
rx = 100  #다른 위치 주면 다른 위치에 감. 토끼의 위치 지정 
ry = 200 
count = 0 

while isRunning: #플레그성 반복할건지 빠져나올건지 결정하는 변수를 플래그성 변수라고 한다.isrunning이 플레그성 변수 
    cnt +=1
    #이벤트가 있으면 
    for event in pygame.event.get(): #이벤트 모으기  게임에서 다양한 이벤트가 일어나면 모음 for문이니니까 담음, 이벤트 종류 담아서 
        if event.type ==pygame.QUIT: #발생한는 이벤트 1개꺼내서 반복, 종료나오면 종료 
            isRunning = False
    # if event.type == pygame.KEYUP:
        
        #이벤트 중에 게임 종료 이밴트가 있으면 종료해. 그 다음 반복문 돌아올 때 탈출  클릭 마우스 , 이벤트 들중에 하나 꺼내서 담아서 종료하는 이벤트면 FALSE로 변경 FALSE니까 빠져나옴.
    keys = pygame.key.get_pressed()#눌러진 애들을 통째로 갖다놓을 수 있음 
# print(keys[pygame.K_LEFT]) #
    if keys[pygame.K_LEFT] == 1: #왼쪽 화살표 버튼이 눌린상태라면 
        if count == 5:  #5번에 한번만 움직이게 함. #
            rx -= 5
            count =0
        else:
            count += 1 
    if keys[pygame.K_UP] == 1:
        if count == 5:
            ry -= 5
            count = 0
        else:
            count += 1 
    if keys[pygame.K_RIGHT] == 1:
        if count ==5:
            rx += 5
            count = 0
        else:
            count += 1 
    if keys[pygame.K_DOWN] == 1:
        if count == 5:
            ry += 5
            count =0
        else:
            count += 1 

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
#배경그리기 
    screen.blit(bg,(0,0)) #bg배경을 0,0으로 그려 
    #현재 창 0,0기준으로 좌측 상단점 시작해서 배경 그려 
    if cnt%2 ==0: #홀수 짝수 해서 움직이게 
        screen.blit(rabbit1,(rx,ry)) #100,200 
    else:
        screen.blit(rabbit2,(rx,ry))
    
    
    pygame.display.update() #

pygame.quit() #가장 기본구조 