from PIL import Image # import pillow library (can install with "pip install pillow")
im = Image.open('C:\\Users\\Ashutosh\\Desktop\\elon\\icard\\IMG-20220222-WA0002.jpg')
im = im.crop( (30, 320, 250,560) ) # previously, image was 826 pixels wide, cropping to 825 pixels wide
im.save('C:\\Users\\Ashutosh\\Desktop\\elon\\icard\\IMG-20220222-WA00021.jpg') # saves the image
# im.show() # opens the image