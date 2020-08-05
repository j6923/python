#list 순서가 있고 중복이 있으며 변경도 가능한 것이 특징 

a = [1,2,3]
print(a, type(a))
#다양한 자료형 가질수 있습니다. 


b = [10, a, True, '문자열']

print(b)
print(b[1])
print(b[1][2]) #1번째 있는 것의 2번째 

c = [[1,2], [3,4,5], [6,7,8,9]] #이렇게도 가능 0번째, 1번째, 3번째,, 각 엘리번트 또 
print(c[1][1])   #c의 1번의 1번=1
print(c[2][2]) 


print("-----------------------------------------------------------------------")

#동물 
pet = ['강아지', '고양이', '거북이','고슴도치']
print(pet)
pet.append("열대어")
print(pet)
pet.remove("거북이") #거북이 삭제하고 싶어요. 
print(pet) 
pet.insert(0,"이구아나") #몇번째 삽입할수 있어요.   #append 는 맨 끝에 삽입하는 것  
#insert는 중간에 삽입하는 걳 
pet.extend(["토끼","햄스터"])  #extend란? 
print(pet)
#연산도 가능
pet += ["돼지"]
print(pet)


#몇개 갯수 알고싶어요 
print(len(pet))
#고슴도치 제거하고 싶어요. 
pet.remove("고슴도치")
print(pet)

del pet[3] #pet의 3번 삭제,   위치로 삭제도 가능합니다. 
print(pet)
animal = pet 
#웹에서 긁어온 것 정재할 때 많이 씀. ---함수들 
#팻 복사하고 싶어요. 
print("animal :" , animal)
print("pet :", pet) 
pet[0] = '멍멍이'
print("-----------------------------------------------------------------")
print("animal :" , animal)
print("pet:", pet)
#animal도 바뀌어 있음 

print(id(animal), id(pet)) #같은 대상을 참조 