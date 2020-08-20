import pyautogui  #pyautogui를 불러와 
#이미지로 클릭하기 

#현재 화면에 
i = pyautogui.locateOnScreen("e:/dev/python_workspace/img/search.png")  #여기 이미지 있는 곳에서 
print(i)  #i를 출력 
#q버튼 중간쯤 클릭
pos = pyautogui.center(i)   #여기 중간지점으로 클릭해줌 
pyautogui.click(pos)
#중간 쯤 클릭하게 됨 
#왼쪽, 오른쪽 화면 달라져도 찾아냄>>> 장점 
#앨리먼트, 자바로 변경되어도 위치 정확히 찾을 수있음. 

# pyautogui.screenshot("p.png",region=(1154,172,58,57)) #캡쳐 잡아서 파일 만들어줌 
#region(x,y,너비, 높이)
# #x좌표 y좌표 너비 높이 #정수로 #대충 50 50 함 
# 캡쳐를 떠줌. 
#이미지 저장해서 해도 됨. 

