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

time.sleep(0.3)


#음식점 이름 
# for i in range(1,21): 
#     ulElem= browser.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.place_list > div.list_area > ul")
    
#     lists = ulElem.find_elements_by_css_selector(".list_item.type_restaurant")
#     for store in lists:
#         print(store.find_element_by_css_selector("div.tit > span > a > span").text)
        

#     pyautogui.click(765,580)

#_business_33068253 > div > div > div.tit > span > a > span  #
#_business_1708165940 > div > div > 

    #_business_33068253
# print(lists)
    #_business_33068253

    
    #_business_33068253

### 음식점 종류
print("=======================================------------------------------------------------------------------------------") 

# 검색 결과에서 다음 버튼을 누르면 검색  : 20 개 
for j in range(1,21):
    # 현재 브라우저에서 "#place_main_ct > div > div > div.sc_box.place_list > div.list_area > ul") 선택자를 갖는 객체를 선택 
    ulElem1= browser.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.place_list > div.list_area > ul") #전체 큰 거 
    # 6개의 식당 목록 객체를 가져오기 
    lists1=ulElem1.find_elements_by_css_selector(".list_item.type_restaurant") 

    # 그 식당 목록 에서 1개씩 꺼내 원하는 데이터를 가져오기 
    for store1 in lists1:

        
        # 업종이 존재할때만 검사 
        try : 
            store1.find_element_by_css_selector(".category")
            #print( store1.find_element_by_css_selector(".category").text) # 이건 뭐지? 
            # 카테고리가 존재 
            categoryName = store1.find_element_by_css_selector(".category").text

            if categoryName != "주점" and categoryName != "호프" and categoryName != "맥주" and categoryName != "다방" and categoryName != "맥주, 호프":
                print(store1.find_element_by_css_selector("div.tit > span > a > span").text) #음식점이름 
                print(store1.find_element_by_css_selector(".category").text) # 이건 뭐지? 
                print(store1.find_element_by_css_selector(".item").text) #리뷰수 
            
        except:
            pass
            # print(" 카테고리 없음 ")
            





            #####최종판
             



            
        




        # categoryName = store1.find_element_by_css_selector(".category").text
        # if categoryName != "주점" and categoryName != "호프" and categoryName != "맥주" and categoryName != "다방" :
        #     print(store1.find_element_by_css_selector("div.tit > span > a > span").text)
        # else:
        #     pass 

        # 업종중 주점 , 호프 , 맥주 , 다방 , 맥주, 호프 등의 업종 명을 가진 식당은 제외  

        # if len(store1.find_element_by_css_selector(".category"))==0:
        #     pass
        # else print(store1.find_element_by_css_selector(".category"):
        # if store1.find_element_by_css_selector(".category").text=="주점":
        #     pass
        # elif store1.find_element_by_css_selector(".category").text=="호프":
        #     pass
        # elif store1.find_element_by_css_selector(".category").text=="맥주":
        #     pass
        # elif store1.find_element_by_css_selector(".category").text=="다방":
        #     pass
        # elif store1.find_element_by_css_selector(".category").text=="맥주, 호프":
        #     pass
        # else:
        #     print(store1.find_element_by_css_selector(".category").text) #식당종류 
        # print(store1.find_element_by_css_selector(".item").text) #리뷰수 
        # print(ulElem1.find_element_by_css_selector(".rating").text) #별점 
        
        # print(store1.find_elements_by_css_selector(".txt address").text)
        # print(store1.find_elements_by_css_selector("location_area").text)
        # print(store1.find_elements_by_css_selector(".label_address"))
    
        # if len(store1.find_elements_by_css_selector("div > div > div.txt.address")) == 0 :  #현재 페이지에서 갯수를 세서 그런 애가 0이면(없다면)
        #     pass #패스 
        # else: #그렇지 않으면 
        #     print(store1.find_element_by_css_selector("div > div > div.txt.address").text) #그런애를 출력해주세요. 
        print("==========================================================================================")
        


        #store1.find_elements_by_css_selector(".txt.address").text==True:
        #div > div > div.txt.address
        #addr
        
    # print(ulElem1.find_element_by_css_selector("map_area.type_dynamic._map_area"))
    #만약에 이게 있으면 출력 
    #이게 없으면 skip 
        
    #location
    time.sleep(0.3)
    pyautogui.click(765,656)
    #pyautogui.click(763,694)

print(store1)

#_business_33068253 > div > div > div.tit > span > span

#list_item type_restaurant
#_list_dynamic_map

#주소 




#리뷰수 

