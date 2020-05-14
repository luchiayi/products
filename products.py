import os 
#讀取檔案
products = []
if os.path.isfile('abc.csv'): #檢查檔案在不在
	print('yeah!')
	with open('abc.csv', 'r', encoding= 'utf-8') as f:
		for line in f:
			if'商品,價格' in line:
				continue
			name,price = line.strip().split(',')
			products.append([name, price])	
	print(products)
else:
	print('找不到檔案')

#使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')	
	price = int(price)
	#p.append(name)
	#p.append(price)   # =  p = [name, price]
	products.append([name, price])
print(products)

#印出所有商品紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#'abc'+'123' = 'abc123'
#'abc'* 3 = 'abcabcabc'
#寫入檔案
with open('1.csv', 'w', encoding= 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')

