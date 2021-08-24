from random import *

#0.0 이상 1.0 미만의 임의의 값 생성
print(random())
##0.0 이상 10.0 미만의 임의의 값 생성
print(random() * 10)
#0이상 10 미만의 임의의 값 생성
print((int)(random()*10))
#1이상 10 이하의 임의의 값 생성
print((int)(random()*10)+1)
#randrange : 앞의 수 포함, 뒤의 수 미포함
#1이상 11 미만의 임의의 값 생성
print(randrange(1,11))
#randint : 앞의 수, 뒤의 수 모두 포함
#1이상 10 이하의 임의의 값 생성
print(randint(1,10))