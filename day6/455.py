

def sumvalue2(*b):  #(a, *b):
    print("a: ", a)
    print("b :", b)

    #왜 에러가 나지? >>>>  b*는 여러개 받아줄 수 있지, 없는 것을 받아줄 수
    #는 없음. 여기서 변수 a가 없기 때문에 에러가 남. 




    def hap(a, *b): #*b: 가변인수   #수가 안 맞아서 가변인수 씀 
    print("a :", a)
    print("b :", b)
    v=a    #a의 변수를 v에 대입, 100을 
    for k in b:
             #자료형 튜플, 앞의 것 꺼내서 담고 앞의 것 꺼내서 담어
        v +=k  #v = v+k      v+k는 누적하려고 이렇게 씀. 
        print(k)  #누적했으면 k가 아니라 v가 되어야 함. 
#정수랑 튜플 바로 계산 못하니까 튜플하나씩 꺼내서 정수랑 계산
# a에 100을 담으면 나머지는 b에 담음 
# 앞의 것 쓰고 나머지 b에 담음 
#b라는 튜플 k에 할당--- for k in b: 

 
print(hap(100,200))
print(hap(100,200,300))


#이해 안 가.   둘 다 투플 

#a를 꺼내면 정수 


