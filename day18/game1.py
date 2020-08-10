import pygame  #기본구조 

#쓰기 전에 초기화 항상 해줘야 함

pygame. init() #기본구조 

#화면 크기 지정함(밑에)
screen_width = 1200 #기본구조 
screen_height = 800  #기본구조

screen = pygame.display.set_mode((screen_width,screen_height)) #기본구조  #게임화면을 다시 그리기, 갱신함.
#배경 그리기 
#bg = 배경이미지  #플레그성 반복할건지 빠져나올건지 결정하는 변수를 플래그성 변수라고 한다. 
bg = pygame.image.load("e:/dev/python_workspace/img/img/bg.jpg") #배경화면을 넣는다 
rabbit1 = pygame.image.load("e:/dev/python_workspace/img/img/rabbit1.png") #토끼 1을 넣는다. 
rabbit2 = pygame.image.load("e:/dev/python_workspace/img/img/rabbit2.png") #토끼 2를 넣는다. 
px =500  
isRunning = True  #게임을 계속 진행할지, 중지 할지를 결정하는 변수 
                   #flag
pygame.display.set_caption("토끼 사냥") #위에 창틀에 "토끼 사냥"을 적음. 

cnt = 0 #반복문 증가할 때마다 1씩 증가 
#1번 까박 1번찍고 2번 깜박 2번찍기 
#토끼 위치좌표 
rx = 100  #다른 위치 주면 다른 위치에 감. 
ry = 200 

while isRunning: #반복문을 넣어야 지 보여주고 딱 끊나지 않음. 
    cnt +=1
    
    for event in pygame.event.get(): #이벤트 모으기  게임에서 다양한 이벤트가 일어나면 모음 for문이니니까 담음, 이벤트 종류 담아서 
        #이벤트 중에 게임 종료 이밴트가 있으면 종료해. 그 다음 반복문 돌아올 때 탈출  클릭 마우스 , 이벤트 들중에 하나 꺼내서 담아서 종료하는 이벤트면 FALSE로 변경 FALSE니까 빠져나옴.
        if event.type ==pygame.QUIT:
            isRunning = False
        
         #게임화면을 다시 그리기 
        #게임이 진행되는 동안 
# pygame.display.update #게임화면을 다시 그리기, 갱신함. 기본구조 
#배경그리기 
    screen.blit(bg,(0,0)) #bg배경을 0,0으로 그려 
    #현재 창 0,0기준으로 좌측 상단점 시작해서 배경 그려 
    if cnt%2 ==0:   #짝수이면 토끼1 
        screen.blit(rabbit1,(rx,ry)) #100,200 
    else:  #짝수가 아니면 토끼 2  
        screen.blit(rabbit2,(rx,ry)) #토끼가 겹치지 않게 함. 
    
    
    pygame.display.update() #게임화면을 다시 그리기, 갱신함. 기본구조 

pygame.quit() #가장 기본구조 