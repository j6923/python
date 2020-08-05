with open("./day9/msg3.txt",'r',encoding='utf-8') as file:
    # data = file.read()
    data = file.readlines()
    print(data)  #이걸로 읽어오세요 
#한번에 리스트형식으롤 가져올 수 있음.
#읽고 올 때 read있고 readline있음 

lines = ['안녕하세요\n',"오늘은 금요일\n", "이면 좋겠네요\n"]


with open("./day9/msg3.txt",'w',encoding = "utf-8") as file:
    file.writelines(lines)  #리스트를 한줄 한줄 넣는것 lines #유니코드로 저장하고 싶어요.  