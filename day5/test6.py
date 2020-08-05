# #1.사용자로부터 숫자 10개를 입력받는다.(랜덤하게 10개의 숫자를 생성 1-999) 

# # import random
# # #리스크가 있어야 담겠죠
# data = []
# for i in range(10):
#     n=random.randint(1,999)
    



# # #2. 이것을 리스트에 담는다. 
#     data.append(n)

# print(data)

# # #3. 임시변수를 선언한다.
# # temp = -1 

# # #4. 리스트의 모든 요소와 비교해서 큰 값을 임시변수에 담는다. 
# # #반복문을 사용해서 리스크에 모든 요소를 출력 
# for i in data:
#     #print(i)
#     if i > temp : 
#         temp = i
# # #5. 임시변수에 들어있는 값이 최대값 : --> 출력 
# print(temp)
# #1.맨 앞것과 맨 뒤의 것 비교 큰 것을 변수에 담음. 큰 값을 담아놓고 그 마지막에 큰 값만 출력  #임시변수에 담아서 비교 %d %s #작으면 안하고 


#최소값 #요소에 첫번째것 두번째 것 할 수 있음 ---- 리스트는 

import random
data = []
for i in range(10):
    n=random.randint(1,999)
    data.append(n)
print(data)
temp = -1 
for i in data:
    #print(i)
    if i > temp : 
        temp = i
print(temp)
#아~~ 허무해.. 밑의 것으로 해도 되요. 
print(min(data), max(data))