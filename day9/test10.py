import pickle
#  pickle.dump(name,file) 
#     pickle.dump(age,file) 
#     pickle.dump(addrs,file) 
#     pickle.dump(strength,file) 
#     pickle.dump(intelligence,file) 
#     pickle.dump(money,file) 
#     pickle.dump(exp,file) 
#     pickle.dump(level,file) 
with open('LOL.dat','rb') as file: #바이너리 타입 rb 
    name = pickle.load(file) 
    age = pickle.load(file) 
    addrs = pickle.load(file) 
    strength = pickle.load(file) 
    intelligence = pickle.load(file) 
    money = pickle.load(file) 
    exp = pickle.load(file) 
    level = pickle.load(file) 


print("이름 :", name)
print("나이 :", age)
print("주소 :", addrs)
print("힘 :", strength)
print("지능 :", intelligence)
print("머니 :", money)
print("경험치 :", exp)
print("레벨 :", level)
    