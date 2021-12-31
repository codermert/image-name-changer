#!/usr/bin/env python
import os
import requests

def createFolder(fname):
	if not os.path.exists(fname):
		try:						
			os.mkdir(fname)
		except OSError:			
			print("Create directory failed")

print("example url: https://vkclub.su/en/stickers/sanoya/")
url = input("input url: ")
_ = 0
if (url[-1]=="/"):
    url = url[:-1]
name = url.split("/")[-1]



createFolder(os.getcwd()+"\\result\\"+name)
while True:
    increment = "{:03d}".format(_)
    img_path = img = "https://vkclub.su/_data/stickers/"+name+"/sticker_vk_"+name+"_"+increment+".png"
    response = requests.get(img_path)
    _ += 1
    filename = name+"_"+str(increment)+".png"
    if response.status_code == 200:
        file = open("result/"+name+"/"+filename, "wb")
        file.write(response.content)
        file.close()
        print(filename+" downloaded!")
    else:
        print("all sticker from "+name+" already downloaded!")
        break