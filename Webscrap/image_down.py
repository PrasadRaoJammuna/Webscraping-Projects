import random
import urllib.request

def img_download(url):
    img_name = random.randrange(100,500)
    full_name = str(img_name)+'.jpg'
    urllib.request.urlretrieve(url,full_name)

img_download('https://www.dailypioneer.com/uploads/2019/story/images/big/msd-turns-a-year-older--team-a-bit-wiser-2019-07-07.jpg')

print('Done..!')

'''def img(url):
    img_name = random.randrange(100,200)
    full_name = str(img_name)+'.jpg'
    urllib.request.urlretrieve(url,full_name)
img('image_link')'''
