#salary모듈 불러오고 싶어 
import salary as s #별칭 줄수 있어요, as s 로  ,,, 길거나 너무 디테일하게 ,s는 별칭
#불러와서 실행한 것 볼 수 있음. 
#불러왔지 실행은 안햄 

#import할 때 같이 딸려와서  앞의 것이 

#__main__
#나오는 것 모듈 이름-- 지금 이거 실행하고 있어 __name__이 모듈의 이름. 
#실행하고 있는 나는 main이라고 부름. 
#다른 데서 불러올 때는 모듈의 이름. 

print(s.raise_sal(5000)) #주석을 써놨다면 주석도 보여줌 #
print(s.reduce_sal(3000))
print("-------------------------------------------------------------------------") 
import lottosalary as ls #로또 셀러리 불러온것 
#50% 확률로 급여가 20%인상
print(ls.raise_rnd_salary(2000))
#50% 확률로 급여가 20%감소 
print(ls.reduce_rnd_salary(2000))
#램덤하게 0과 1구해서 0이면 인상X 1나오면 인상 




