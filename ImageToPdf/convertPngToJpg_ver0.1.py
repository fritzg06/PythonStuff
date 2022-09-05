# References:
# https://www.programmersought.com/article/90754952932/

import os
from PIL import Image

dirname_read="C:/Greenshot/PLUK Branch Assembly June 2021/png/"  # Note the trailing slash
dirname_write="C:/Greenshot/PLUK Branch Assembly June 2021/jpg/"
names=os.listdir(dirname_read)
count=0
for name in names:
    img=Image.open(dirname_read+name)
    name=name.split(".")
    if name[-1] == "png":
        name[-1] = "jpg"
        name = str.join(".", name)
        #r,g,b,a=img.split()
        #img=Image.merge("RGB",(r,g,b))
        to_save_path = dirname_write + name
        img = img.convert('RGB')#RGBA means red, green, blue, Alpha color space, Alpha refers to transparency. And JPG does not support transparency, so either discard Alpha or save as a .png file
        img.save(to_save_path)
        count+=1
        print(to_save_path, "------count：",count)
    else:
        continue

