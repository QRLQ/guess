import random
start = input('請輸入範圍起始值:')
end = input('請輸入範圍最終值:')
start = int(start)
end = int(end)
r = random.randint(start ,end)
cont = 0
while True:
	num = input('請輸入數字:')
	num = int(num)
	cont += 1
	if num == r:
		print('你猜對了')
		print('你已經猜了' ,cont ,'次' )
		break
	elif num > r:
		print('太大了')
	elif num < r:
		print('太小了')
	print('你已經猜了' ,cont ,'次' )