from pathlib import Path
# Path("./img/test").mkdir(exist_ok=True) #.은 python_workspace img라는 폴더 그 밑에 test없다면 저 폴더를만들어 주고 싶어 
#저 디렉토리 만들어주세요. #존재하면 됐고 없으면 만들어. mkdir--makedir 

#aaa/bbb/ccc/test #test 위의 디렉토리 없어 부모 디렉토리 다 만들어 
Path("./img/aaa/bbb/ccc/test").mkdir(parents=True,exist_ok=True) 