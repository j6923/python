from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 
import pyautogui
import cx_Oracle


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
            storename = store1.find_element_by_css_selector("div.tit > span > a > span").text
            if categoryName != "주점" and categoryName != "호프" and categoryName != "맥주" and categoryName != "다방" and categoryName != "맥주, 호프":
                print(store1.find_element_by_css_selector("div.tit > span > a > span").text) #음식점이름 
                print(store1.find_element_by_css_selector(".category").text) # 이건 뭐지? 
                print(store1.find_element_by_css_selector(".item").text) #리뷰수 
            
        except:
            pass
        
    time.sleep(1)
    #pyautogui.click(765,656)
    #pyautogui.click(763,610)
    pyautogui.click(763,583)
    resultList=[]
    resultList.append(store1)
    for i in resultList:
        print()

#resultList.append(x)

def create(self):
#         #객체생성하기 
    connection = cx_Oracle.connect("oralce", "scott","192.168.0.32:1521/orcl")
    print(connection)
        #cur 생성
    cur = connection.cursor()

        #사용할 sql문
    sql = """ 
    CREATE TABLE FOOD
        (NAME VARCHAR2(10),
        FOOD_CATEGORY VARCHAR2(10),
        address VARCHAR2
        REVIEW NUMBER(9));
    """

    connection.commit()

    connection.close()

def save(self):
    connection1 = cx_Oracle("oracle","scott","192.168.0.32:1521/orcl")
    print(connection1)
    cur = connection.cursor()

    sql = """
    INSERT INTO NAME VALUES(:)
    """
    #실행
    # cur.execute(sql,)

    connection.close()
    connection1.close()

    # self.clicked.connect(self)


#             #####최종판




            
        




        


    
#_business_33068253 > div > div > div.tit > span > span

#list_item type_restaurant
#_list_dynamic_map

#주소 




#리뷰수 

