from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 
import pyautogui

url = "https://www.naver.com/"
browser = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")
browser.get(url)
browser.maximize_window()
elem = browser.find_elements_by_id("query")
elem.click()
time.sleep(3)
elem.send_keys("종로3가 맛집")
elem.send_keys(Keys.ENTER)

pyautogui.scroll(-1500)



# for i in range(1,21):
#     ulElem= browser.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.place_list > div.list_area > ul")#browser에 있는 
#     lists = store.find_elements_by_css_selector(".list_item.type_restaurant")  #더블클릭 ctrl+c ctrl+v 함  #하나의 전체 부분 
#     for store in lists:
#         print(store.find_element_by_css_selector("div.tit > span > a > span").txt)

#     pyautogui.click(765,580)

# #_business_33068253 > div > div > div.tit > span > a > span  #    business_33068253 >는 id unique함 반복문 쓰려고 반복되는 것만 씀 
#div > div > div.tit > span > a > span   #이걸 다 써도 되지만 div.tit짧게 이 부분만 넣어도 되서  이 부분만 용산구00아파트만 해도 다 알아보기 때문에 이렇게 함. 
#_business_1708165940 > div > div > 

    #_business_33068253
print(lists)
    #_business_33068253

    
    #_business_33068253