#사용자로부터 글자를 입력받아 이 문자가 대문자인지 소문자인지 판단

#1. 사용자의 입력값을 받아오기
data = input("한글자 입력: ")
print(data)
#2. 이 값의 ascii 코드 값을 구한다.
print(ord(data)) 
code = ord(data)
# 3. A: 65, a: 97
#아스키코드 구하는 함수  #변수에 담아놓고 비교하자고요. 
if code >= 65 and code <= 90:
    print(data + "는 대문자입니다.", code)   #만약 코드가 65보다 크고 90보다 작거나 같으면  # data는 대문자입니다.하고 코드 표시
elif code >= 97 and code <= 122:  # 특수기호도 있으므로 else가 아닌 elif를 쓴다.  
    print(data + "는 소문자입니다.", code) #

# 4. 65~90: 대문자      97~122:소     B: 66  2진수로 한갓
#  5. 판단 후 출력   #한글로 이것을 쓸 수 있어야 한다. --- '의사코드'라고도 함. 논리적으로 맞으면 문법으로 바꿈.

#이 글자를 소문자로 변환시키고자 합니다. 
#ord(문자) ------> ascii code
#chr(숫자)_______------> 문자 

#1. 각 글자의 ASCII 코드 값을 구한다/. 
#2. 대문자의 범위 : 65~90이라면 이것을 대문자로 바꾼다. 
# ..소문자  : 97~122   #아스키코드 32의 차이가 있음 #차이값 구함  
msg = "PyThon"    
print(len(msg)) #5   #msg의 길이를 구해라 
for i in range(len(msg)):   #길이 구한 것을 i에 넣고 반복 
    #print(msg[i]) 잘 되었는지 찍어봄 
    code = ord(msg[i]) #이 글자의 ascii code    #코드는 아스키코드를 구한 값을 대입한 것 
    if code >= 65 and code <= 90: #대문자라면     만약 코드가 65보다 크거나 같고 90보다 작거나 같으면  
        print(chr(code+32), end = "") #공백 안 주게 출력   #이렇게 출력 캐릭터로 32로 출력 대문자일 때 소문자로 변경 
    elif code >= 97 and code < = 122: #소문자일 거야 
        print(chr(code-32), end = "")    
#값을 입력받는다.
#list 97에서 소, 대 
msg = Input("단어를 입력하세요") 
print(len(msg)) #5   #msg의 길이를 구해라 
for i in range(len(msg)):   #길이 구한 것을 i에 넣고 반복  
    code = ord(msg[i]) #이 글자의 ascii code    #코드는 아스키코드를 구한 값을 대입한 것 
    if code >= 65 and code <= 90: #대문자라면     만약 코드가 65보다 크거나 같고 90보다 작거나 같으면  
        print(chr(code+32), end = "") #공백 안 주게 출력   #이렇게 출력 캐릭터로 32로 출력 대문자일 때 소문자로 변경 
    elif code >= 97 and code < = 122: #소문자일 거야 
        print(chr(code-32), end = "")
        
        #소문자일 때 대
    
#3. 변환된 값을 코드로 출력 


