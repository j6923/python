#운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게 해주는 모듈 : os 
#operation system, 윈도우, 리눅스, 유닉스 등 #스마트폰 거의 리눅스 
import os 

# print(dir(os)) #통해서 운영체제 기능 사용가능 
# 현재 작업 디렉토리 알 고 싶어요. 


print(os.getcwd()) #current working directory 현재 뭔가 진행하는 디렉토리 #set--- 지정할 거야 #get -- 

#밑에 e: 파일 디렉토리 

#현재 작업디렉토리에 있는 파일과 디렉토리 목록 검색하고 싶음 

print(os.listdir()) #현재 작업티렉토리에 있는 목록 가져올 수 있음. 
#리스트로 넘겨주는 것 볼 수 있음. 
print(os.listdir('day9')) #day9에 뭐가 있느지 볼 수 있음 
print(os.listdir('.')) #.은 운영체제에서 현재 디렉토리 #..부모디렉토리  

#현재 디렉토리 : PS E:\dev\python_workspace>   e/dev/ .. 부모디렉토리 #상대적으로 지정할 수 있어요. 
# 운영체제 다른 디렉토리 적용가능, 
# workplace는 . 
#파이션 프로그램도 실행파일로 만들 수 있어요. c밑에 어디 밑에 할 수도 있고 어디 위에 어디위에 할 수도 있음 

print(os.listdir("e:\dev\python_workspace"))  #어디밑에 뭐가 있습니다. 나옴.  #역슬래쉬 원래 특수문자 ,,원래 두개 써야 인식--- 윈도우는 역슬래쉬2개혹은 / 

#현재 작업디렉토리에 있는 모든 파일을 출력 
#반복문을 사용해서 한개씩 출력 

# v = os.listdir('.')
# for i in v:     나
#     print(i)
# for file in os.listdir("c:/"):  #c드라이브의여러가지 파일 나오는 것을 볼 수 있음 
# #     print(file)

# for file in os.listdir("c:/"):  #c드라이브의여러가지 파일 나오는 것을 볼 수 있음 
#     print(file)

#확장자가 .zip파일들만 선택 

for file in os.listdir("c:/"):
    if file.find("zip")>0: 
        print(file)


#위에 file있으면 위의 것도 찾아줌 

    if file.endswith("zip"):
for file in os. listdir("c:/"):
        print(file) #뒤의 글자가 zip인 것을 찾을거야.  


