try:
     import urllib.request
except Exception as e:
     print(f"Somthing is wrong with imports {e}" )

# So there is 1170 gift images, in which 745 is . jpg and after that till 117e is png

for i in range(746,1170):
    
     #https://vkclub.su/_data/gifts/l.jpg
     try:
         if i <= 1170:
           urllib.request.urlretrieve(f'https://vkclub.su/_data/gifts/{i}.png',f"gifts\{i}.png")
         else:
           urllib. request.urlretrieve(f'https://vkclub.su/_data/gifts/{i}.jpg',f"gifts\{i}.png")
     except:
        print ("error")



            
