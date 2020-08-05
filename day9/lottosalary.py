import random

def raise_rnd_salary(sal):
    rnd = random. randint(0,1)
    if rnd == 0 :
        print("강화성공!!")  #있으니까 강화성공까지 찍힘  def 만들때 이렇게 만들어서 
        return sal*1.5
    else: 
        return sal

def reduce_rnd_salary(sal):  #reduce_rnd_salary란 함수를 만들고 매게변수를 sal로 한다. 
    rnd = random.randint(0,1)   #random
    if rnd == 0 :
        return sal*0.5
    else:
        return sal 

if __name__== "__main__":
    print(raise_rnd_salary(2000))
    print(reduce_rnd_salary(2000))  

    

