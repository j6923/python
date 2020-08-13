#현재 상영영화의 포스터를 얻고 싶어요 
#현재 상영작의 번호를 안다 개발자 도구 
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from pathlib import Path
url = "https://movie.naver.com/movie/running/current.nhn" #url의 주소를 입력한다. 

res = requests.get(url)   #url을 요청한다. 

res.raise_for_status()   

# pprint(res.text)

soup = bs(res.text,'lxml') #

#아까보다 보기 좋은 코드 
# pprint(soup)

divs = soup.find_all("div", attrs={"class", "thumb"}) #클래스가 class thumb 

# pprint(divs)
idx = 0 #for의 밖에 선언 

for div in divs:   #FOR문으로 돌려 반복문으로 가져옴. 
#     pprint(div)
# print("-----------------------------------------------------------------------")
#자손인 a태그 하이퍼 래퍼런스 

    aTag = div.find("a") #태그에 a를 찾아라. 
    # pprint(aTag['href'].split("=")[1]) #대괄호[속성]   #하이퍼인 애들만 갖고 오고 싶어요.  #=로 끊어옴 
    #print("---------------------------------------")
    movieNO = aTag['href'].split("=")[1]    #번호끝의 것을 가져오기 위해 SPLIT으로 끊고 슬라이싱함. 
  #영화코드의 끝의 번호를 가져오기 
    url2 = "https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode="+movieNO
    # print(url2)  attrs 함수 만든사람이 대괄호로 ???  
  
    #요청
#request가 get으로 해서 결과를 가져옵니다, 주소를 주면 결과를 반환해줄거야 함수 만들어놓음 설명 reqests.get(url) 
    res2 = requests.get(url2)
    #pprint(res2)
    #저장하기 
    soup2 = bs(res2.text,'lxml')
    img = soup2.find("img")
    #img인 큰 사진 가져온다. 
    print(img['src'])
    #이미지 파일 저장하기 
    imgpath = img['src']
    res3 = requests.get(imgpath)
    Path("./img/movie_poster").mkdir(parents = True, exist_ok=True)
    idx +=1 #안 하면 덧붙입 
    with open("./img/movie_poster/movie{}.jpg".format(idx),'wb') as f: #파일 1234 만듦 i씩 증가할 때마다 증가 ,, 
        f.write(res3.content)



#설계가 잘된 사이트에서 가져와야 크롤링도 쉬움. 
#옷 하다가 배달한다고 바꾼 그런 사이트는 덧붙여져 누더기 같아 크롤링도 어려움. 



#ttps://pypi.org/project/requests/2.7.0/   에서 볼 수 있음. 

#자동화 시킬 수 있음 





#python 은 

#r   