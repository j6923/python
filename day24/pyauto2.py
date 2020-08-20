import pyautogui  #pyautogui를 불러와 
import time #time을 불러와 

pyautogui.moveTo(400,400,2) #여기로 이동해  400,400위치에서 2초 간격으로 움직여 

#moveto는 절대위치로 함. 

#moveToRelative() #지금 위치에서 얼마만큼, 상대적으로 얼마만큼 

pyautogui.moveRel(100,100,3) #그 지점에서 x로 부터 얼마 ,y로 부터 얼마만큼 움직여




#계산기 클릭하고 싶어요 
pyautogui.moveTo(-924,520,4)  #pyautogui로 moveTo를 실행하는 데 x좌표 -924, y좌표 520, 4초 간격으로 움직여
pyautogui.click(clicks=2, interval=2) #클릭을 두번 더블클릭을 2초간격으로 해 


pyautogui.doubleClick() #아예 더블 클릭 

time.sleep(1) #1초 잠들어 
pyautogui.typewrite('Hello') #커서 깜박이면 글자씀 

#화면 자체의 gui 클릭, 버튼 이미지 있으면 그 위치 찾아서 클릭하는 등 


