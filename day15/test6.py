#CPU
#Thread : 하나의 포로세스 내에서 진행되는 하나의 실행 단위를 의미 
#프로그램이 하나로 흘러가는 것처럼 실타래처럼 하는 것을의미 
# MULtiThread : 

#프로세서 : 메모장, 워드, 카톡과 같이 ,,데이터 share 안함.
# 멀티 쓰레드 : 카톡프로그램에서 채팅가능, 파일 전송가능, 하나의 프로그램 내에서 동시에 여러애들을 처리하는 것 
# 
# 
# 
# 파이썬에서 멀티 쓰레드  구현하는 방법 
# 1. thread가 실행할 수 있는 실행할 함수 혹은 메서드를 작성하는방식으로 할 수 있다. 
# 2. threading.Thread로 부터 파생된 파생클래스를 작성하여 사용하는 방식 
# 
# 
# 1번부터 
import threading #모듈있음 불러옴 

def run(who): #함수 만듦. 
    for i in range(1,101): #1부터 100까지의 수를 하나씩 뽑아냄. 
        print(str(i)+"미터 달리는 중",who) #글자를 넣으면 글자를 나옴. 위의 라인부터 한줄씩 실행 1의 쓰레드 사용해서 
        #위로 가서 다 처리하고 다 하고 위의 것 끝나고 난 다음에 아래것 처리 
        #미친 듯이 같이 달리게 하고 싶어요.

        #이런 함수 있다고 하게요. 구분값으로 who줌
        # 
run("번개") #함수불러야지요 
run("천둥") #앞의 것을 먼저 하고 뒤의 것을 실행

#멀티 쓰레드로 처리하고 싶어요/ 
t1 =threading.Thread(target=run, args=("번개",)) #target은 함수명 , arg 전달할거니 
t2 =threading.Thread(target=run,args = ("천둥",)) #argu는 튜플로 넣어야 
#start() : 쓰레드를 동작시킨다. 
t1.start()
t2.start()

print("main Thread end.....................................")

#사용하려는 것이 star

#start t1준비되었으면 해 t2준비되었으면 해, start인 나는 끝 누가 먼저 시작하는지 모름. 엉켜 멀티 같이 하기 때문에 , 동시에 같이 처리할 수있도록 만드는 것 

#두번째 방법 
