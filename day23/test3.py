
#자동화 하기 
from selenium import webdriver #selenium에서 함수 webdriver를 불러온다. 

from selenium.webdriver.common.keys import Keys  #selenium.webdriver.common.keys에서 keys함수를 불러옴. 
import time  #time을 불러옴. 

#코레일 열차표 예매 

browser = webdriver.Chrome("e:/dev/chromedriver.exe") # webdriver로 chrome으로  

print(browser) #browser 띄워지는 지 띄워봄 

browser.get("http://www.letskorail.com/")

print(browser.window_handles)

#browser.window_handles[1] #현재창으로 전환해야함 

browser.switch_to.window(browser.window_handles[1]) #창을 바꿀거에요.  버전바뀔러면 #현재 창으로 변경 

browser.close()  
browser.switch_to.window(browser.window_handles[1]) #창을 바꿀거에요.  버전바뀔러면 #현재 창으로 변경 

browser.close()  #앞의 팝업창이 더 있어서 2개 더 해야 다 닫음. 

print(browser.window_handles) #먼저 뜬 것이 0번 

browser.switch_to.window(browser.window_handles[0])


#css선택자 >>> enter치면 다 쫙 나오는 것 어느 부모 밑에 누구 css임  link된 text link_text , x엘리먼트 css선택자보다 더 줄일 양식 (xpath)>>>xml에서 자원의 위치를 표시하는 방법
#css선택자로 하고 싶어요. 

#클릭. 우측마우스 카피 그 옆에 뭘로 찾아줄까 copy selector>>> css로 카피해줌 


#browser.find_elements_by_css_selector("#txtGoStar")
# browser.find_elements_by_xpath('//*[@id="txtGoStar"]')



#도착역 지우고 바꾸고 싶어요 


element = browser.find_element_by_css_selector("#txtGoEnd")  #여러개 묶음 있을 때는 s 하나있을 때는 s없는 것 
element.click()
element.send_keys(Keys.BACKSPACE)
element.send_keys(Keys.BACKSPACE)
element.send_keys("포항")
element.send_keys(Keys.ENTER)




element = browser.find_element_by_xpath('//*[@id="res_cont_tab01"]/form/div/fieldset/ul[2]/li[1]/a/img')
#표본조사 방법론 
element.click()
browser.switch_to.window(browser.window_handles[1]) #딱 뜬 창으로 포커스 맞춤  팝업으로 


element = browser.find_element_by_id("d20200815") #15일날짜 엘리먼트 클릭  
#매인 쪽 
element.click()
browser.switch_to.window(browser.window_handles[0])

#램덤하게 살짝 해야 똑같으면 사람맞아? 기계인지 아닌지 
#시간도 램덤하게 

#시 
element = browser.find_element_by_css_selector("#time>option:nth-child(13)")
element.click()
#승차예매 
element = browser.find_element_by_css_selector("#res_cont_tab01 > form > div > fieldset > p > a > img") 
element.click()



