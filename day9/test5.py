#임포트 하는 방법 3가지 
#1. improt 모듈명 

# import random 
# import math
print(dir()) 

#현재사용할 수있는 애있음, 묘듈이 물러와 있는 것 
#안 쓰는 것까지 불러오면 메모리낭비 -- 느려짐 


#2. from 모듈명 import 함수명 
#어디에서 어떤 함수만 가져올 게 . 구체적으로 쓰는 것 
#이 경우 다른 모듈에 동일한 함수가 있을 경우 충돌날 우려 있음
from random import randint
from debak import randint #만들었다 치자  이름 똑같은 애 두개 있을 수 없음, 똑같은 애 있으면 구분 안됨, 모듈 안에 뭐해야써야지, 같은 이름 있어서 충돌남. 
n = randint(100,200) 
print(n) #어디 소속이 함수 이름 그냥 불러서 써서 모듈명 써지 않아도 됨. (장점)
#모듈에 다른 함수 쓰려면 다시 지정해야함 
print(dir())
#3. from 모듈명 import * #결과치불러올수 있음  #모듈에 있는 것 다 불러와, 몽땅 다 randint안 쓰고 써도 됨, 이름 같으면 충돌 가능성 있음 
#from random import* #모듈명 필요 없음, 낱개 전부 다 가져옴. 
from random import*
print(dir())
#숙제 
#구현할 로직 쓰면 됨 2두개 이쌍 리턴할 수 잇죠  