import PIL
import os
import os.path
from PIL import Image

f = r'C:\\Users\\Ashutosh\\Desktop\\elon\\sample'
i=0
for file in os.listdir(f):
    f_img = f+"\\"+file
    img = Image.open(f_img)
    img = img.resize((300,300))
    img.save(f_img)
    print("pass")