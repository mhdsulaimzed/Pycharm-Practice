from PIL import Image

img_1 = Image.open(r'/home/user/Desktop/2022-10-12-232112.jpg')
img2=img_1.convert('RGB')
img2.save(r'/home/user/Desktop/pdfsam/2022-10-12-232112.pdf')


