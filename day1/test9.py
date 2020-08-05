#숫자를 입력 받아 2로 나눈 나머지를 출력 
x=  int(input("숫자를 입력하세요"))
x %= 2
print(x) 

#2개의 숫자 받아올게요 
x,y = input(" 두 개의 숫자를 입력하세요 ") .split()#꼭 찍어야 
print(" x ", x , " y : ", y) 


#사용자로부터 국어, 영어, 수학 점수를 입력받아 
#총점과 평균을 출력 

#90 80 70 

#국어 : 90 영어 80 수학 70 
#총점 : ..... 평균 : ..... 

#x= 90 
#y= 80 
#z=70
#x=int(input("첫번째 숫자를 입력하세요").split()
#y=int(input("두번째 숫자를 입력하세요").split()
#z=int(input("세번째 숫자를 입력하세요").split()
#print("x", x, "y : ", y , "z: ",z)


kor, eng, mat = input("국어 영어 수학 점수를 입력하세요 :").split()

print("국어 : ", kor, "영어: ", eng,"수학 :" + mat)
kor = int(kor); eng = int(eng) ; mat = int(mat) 
print("총점 : ", (kor+eng+mat), "평균: ", (kor+eng+mat/3))