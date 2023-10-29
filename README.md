2028-10-08T23:59:59.999Z


naming sequentially by number

python code :




import os 

path = r'mert'

def rename_files(path):
	count = 1
	for _ in os.listdir(path):
		if _.endswith('.webp'):
			print(_)
			os.rename(_,f'{str(count)}.webp')
			print(_)
			count+=1

rename_files(path)
print('Dosyalar isimlendirildi!')




