#
# 사용자로부터 국어, 영어, 수학 점수를 입력받는다.
# 문자를 정수형으로 형변환해서 각 변수에 담는다. 


#총점을 계산한다.
#평균을 계산한다

#평균점수가 90점이상이면 A 
#평균점수가 80점이상이면 B 
#평균점수가 70점이상이면 C 
#평균점수가 60점이상이면 D 
 #평균점수가 그 외는 F 

kor, eng, mat = input("점수입력:").split()
kor = int(kor)
eng= int(eng)
mat = int(mat)
tot = kor + eng + mat 
avg = tot/3
print(kor, eng, mat, tot, avg)
if avg >= 90:
    print(avg, "A")
elif avg >= 80:
    print(avg, "B")
elif avg >= 60:
    print(avg, "D")
else:
    print(avg, "F")
#쥐띠 
#태어난 연도를 입력하면 어떤 띠인지를 출력 
#자  축  인  묘  진  사  오 미 신 유 술 해 
#쥐 소   호  토  용  뱀  말 양 원 닭 개 돼 
#태어난 년도를 4자리로 입력 : 2020 
#당신의 쥐띠 입니다.  #3으로 나누면 3의 배수인지알 수 있어. 년도를 12로 나눈 나머지 
#4 5 6 7 8 9 10 11 0 1 2 3 
input("년도입력")
a = 2020% 12
print(2020%12) 
if a 
