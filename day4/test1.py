'''
 set : 순서가 없고 중복도 할 수가 없음 
'''

a = {1,2,3,1}

print(a, type(a))

#print(a[0])  #set은 순서를 지정할 수 없어서

b= {3,4}

#두 개 붙이고 싶어요. union   합집합의 결과 
print(a.union(b)) 
#교집합 intersection
print(a.intersection(b)) #교집합 

print(a-b,a|b, a&b)  #차집합 기호로 &할수도 있음 
#추가하고 싶습니다. 중복이 안 되지 추가는됩, 변경도 가능 
#b ={3,4} 
b.add(5)
print(b)

b.update({6,7})   #update통해 set, list, turple추가 가능#set
print(b) 

b.update((8,9))   #소괄호니까 튜플
print(b)

b.update([10,11])
print(b) 

b.discard(7) #값을 삭제하고 싶어요 
print(b)  #몇번째 위치로 삭제해는 못해, 순서가 없으니까 중복된 값은 없어 딱 그거 하나는 삭제 가능

b.remove #remove로 삭제할 수도 있음, 요소 제거 가능 
print(b)   #remove와 discard의 차이점은 없음. 

print("---------------------------------------------------------------")
#형변환
c = set()
c = b
c.clear()  
c = print(c)


print(c)
#clear 값 사라짐? 
#다음 리스트의 종복된 값을 제거하려고 한다. 
m = [2,3,11, 29, 3, 2, 7, 8, 11] #리스트는 순서있고 중복이 가능한 게체 
#1. set으로 형변환 가능, 그러면 중복된 값이 사라진다.
# #2. 리스트로 변경
# #3. 정렬????  
print(m) #[2,3,7,,8,11,29]정렬이 된 채 나왔으면 좋겠음 
m = set(m)
print(m, type(m))
m = list(m)  #새로운 객체 나오면서 다른 애 됨, 이름만 같은 애 
print(m, type(m))
#정렬
m.sort()
print(m) # [2,3,7,8,11,29]
