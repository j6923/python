from bs4 import BeautifulSoup as bs  #bs4에서 불러오는 데 beautifulsoup을 불러오고 bs라는 별칭을 준다. 
from pprint import pprint  #pprint에서 pprint을 가져온다. 
import requests #requests를 불러옴. 
from pathlib import Path
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
#헤더쓰는 대소문장 user agent는 옆의 것
for i in range(1230,1237):
    url = "https://comic.naver.com/webtoon/detail.nhn?titleId=20853&no={}&weekday=tue".format(i)#1200-1237폴더별로 만들기  #숫자 계속 바뀔거니까  #변수를 써서 바꿀거니까 

    #주소 복사, 이 url로 접근 해서 갖고와 


    res = requests.get(url) # 200이면 실행, 아니면 에러 
    #if res.status_code ==200 :   3위의 것 
        #실행
    #else:
    #   에러 
    #의 함수가 res.raise_for_status()
    res.raise_for_status()
    # pprint(res.text)

    #이 페이지가 정상적으로 응답이 온 거면 200 
    #상태값 print(res.status_code)

    soup = bs(res.text,'lxml')  ##이 문서를 해석하자, 해석기 lxml이 성능좋음 이 글자를 이 해석기로 해석해줘  

    # pprint(soup)
    #path와 변수 headers의 headers


    data = soup.find('div',attrs={"class", "wt_viewer"}) #soup에서 find해라 div
    #print(data)

    images = data.findAll("img") #img 몽땅 가져와요 
    pprint(images) #묶음 단위로 리절트 set으로 되어 있음 

    for img in images:
        pprint(img['src']) #각각 떨어져 나오는 것을 볼 수 있음  그리고 src하면 이미지 경로만 가져올 수 있음. 
        #길이 길어서 변수 줌 


        path = img['src']

        #주소창에 넣고 접근해요, 

        # res2 = requests.get(path)
        res2 = requests.get(path,headers=headers) #나는 웹브라우저야 속임. 
        print(res2)        #사진이 여러장이니까 여러번 요청함. 
        #프로그램이 접근하면 자동 접근함,,, 크로링하는 사람이 많아 네이버가 막음. #우회해서 가면 됨. 
        #나 웹브로저야, 하고 속이고 가져옴. 
        #403권한 없음,,, 웹브러우저 아닌 다른 애 접근하면 차단함.
        # #브라우저에 u.애이전트의 값을 알아오면 됨, 사용자를 대신하는 애들을 말함 
        # #what is my user agent
        # #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36
        # #이 정식명칭  
        # window key 화살표 창 여러개 열기 


        #image comic 서버 pstatic 정적인  webtton 에 20853작품번호 1237 화 , 202007270619 2020년 7월 27일 시간 _61f 내부폴더 혹은 암호화 랜덤한 값 생성한 것 
        #파일 이름 같으면 충돌 남 _IMG이미지 01 16번째 저장하고 싶어.   


        #저장할 수 있는 장소인폴더 필요 ---- 폴더 만들어 주세요. 
        #별도 디렉토리를 만들고 그 장소에 이미지 파일을 저장 
        Path("./img/"+path[46:50]).mkdir(parents=True, exist_ok=True) #긴 문자열에서 몇 화 
        with open("./img/"+path[46:50]+"/"+path[-12:],'wb')as f: #이 경로 밑에  #사진은 바이어리 wb  #이 파일에 저장 wb로 하고 그것을 씀 
        # print(path[23:26])# 몇 번인지 찍어줌 
            # f.write("내용")
            f.write(res2.content)
        #몇 화에 있는 이미지 딱 이렇게 되면 좋음 슬라이싱 하고 싶어요 

        


        