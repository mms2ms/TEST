import random

try_time  = 3
 
while  True:
	a = random.randint(1, 100)
	b = random.randint(1, 100)
	print(a, "+", b, "=")
	c = input()
	d = int(c)
	for _ in range(try_time):
		if d == a+b:
			print('당신은 산수쟁이')
			break
		else:
			print(a+b, '당신은 돌대가리 %d 번 틀렸음'%(_+1))
	
	print('다음 문제')