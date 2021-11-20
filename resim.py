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




