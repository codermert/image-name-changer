import os

for i in os.listdir("result1"):
    data = r'{"image_file": "https://raw.githubusercontent.com/codermert/image-name-changer/main/stickers/'+ i +'", \n "emojis": ["",""] \n },'
    print(data)