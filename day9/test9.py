#파이썬 객체를 파일에 저장하는 과정을 Pickling 이라고 한다. #객체를 담군다해서 
#파이썬 객체를 읽어오는 과정을 Unpickling 이라고 한다. 


#피클링 도와주는 것 
import pickle

name = "쑤진공주"
age = 20
addrs = "율도국"
strength = 7
intelligence = 3
money = 0
exp = 10 
level = 3 
#디스크에 저장하고 싶어요,
#저장할 건데 바이너리 타입:wb --- 바이너리 쓰기 모드로 열기 
with open('LOL.dat','wb') as file:
    pickle.dump(name,file) 
    pickle.dump(age,file) 
    pickle.dump(addrs,file) 
    pickle.dump(strength,file) 
    pickle.dump(intelligence,file) 
    pickle.dump(money,file) 
    pickle.dump(exp,file) 
    pickle.dump(level,file) 
   #깨진 것 아님, 바이너리 타입이라 

   


