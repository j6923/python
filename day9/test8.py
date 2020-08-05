# 처음부터닫는 거 함께 만들면 좋잖아
#with open("파일명", 파일모드)as 파일객체:
#     코드 
#열면서 처리하면서 닫아줌. 이거 실행하면 닫도록 만듦. \

# with open("./day9/msg.txt",'w') as file:

#     file.write(" 오늘은 여기까지... \n")


with open("./day9/msg.txt",'r') as file:
    # print(file.read(),type(file.read()))

#메모장 EUCKR로 바꾸기 
   #write하면 덮어써버림 

    data = file.read().split()  #for문 돌려서 0이상이야 count번호해서 집어주면 됨. 
    print(data)
    # data.find("노트북")   
    #우측마우스 페이지 리소스 