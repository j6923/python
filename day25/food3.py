from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 
import pyautogui

url = "https://www.naver.com/"
browser = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")
browser.get(url)
browser.maximize_window()
elem = browser.find_element_by_id("query")
elem.click()
time.sleep(3)
elem.send_keys("종로3가 맛집")
elem.send_keys(Keys.ENTER)

pyautogui.scroll(-1500)

## 음식점 종류 
for j in range(1,21):
    ulElem1= browser.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.place_list > div.list_area > ul") #전체 큰 거 
    lists1=ulElem1.find_elements_by_css_selector(".list_item.type_restaurant") 
    for store1 in lists1:
        print(store1.find_element_by_css_selector("div.tit > span > a > span").text) #음식점이름 
        print(ulElem1.find_element_by_css_selector(".category").text) #식당종류 
        print(ulElem1.find_element_by_css_selector(".item").text) #리뷰수 
        

        
    #
    pyautogui.click(765,580)

print(lists1)
### 음식점 종류 

ulElem1= browser.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.place_list > div.list_area > ul") #전체 큰 거 
lists1=ulElem1.find_elements_by_css_selector(".list_item.type_restaurant") 
# for store1 in lists1:
    # print(store1.find_element_by_css_selector("div.tit > span > a > span").text)
    # 가게 번호 33068253
stroeid = 33068253 
url3 = "https://map.naver.com/v5/search/%EC%A2%85%EB%A1%9C3%EA%B0%80%20%EB%A7%9B%EC%A7%91/place/"+str(stroeid)  #
browser.get(url3)


#
# pyautogui.click(765,580)
time.sleep(2)
# iframes = browser.find_elements_by_tag_name("iframe")

ifrm = browser.find_element_by_id("entryIframe")   #iframe에서 id로 찾기 쉬워서 id로 찾아옴. 
browser.switch_to.frame(ifrm)

ulElem2 = browser.find_element_by_css_selector("div > span._2yqUQ")
print(ulElem2.text)

#주소 




#리뷰수 

