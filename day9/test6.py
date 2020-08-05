import time 
print(time.ctime())


print(time.gmtime(),type(time.gmtime()))

print(time.gmtime().tm_mon) #월부름
print(time.gmtime().tm_mday) #날짜 부름 (일)

