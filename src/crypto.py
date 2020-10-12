from PIL import Image
import random
from pathlib import Path

def encrypt(path,seed,output):
    im = Image.open(path) 
    pix = im.load()
    h,w =  im.size 

    print(path)
    random.seed(seed)
    for i in range (0,h):
        for j in range(0,w):
            val = pix[i,j]
            r = val[0]
            g = val[1]
            b = val[2]
            n = random.randint(0,255)
            r = (r+n) % 255
            g = (g+n) % 255
            b = (b+n)%255

            pix[i,j] = (r,g,b,1)

    im.save(output)

def decrypt(seed,path,output):

    im  = Image.open(path)
    pix = im.load()
    h,w =  im.size  
    random.seed(seed)

    for i in range (0,h):
        for j in range(0,w):
            val = pix[i,j]
            r = val[0]
            g = val[1]
            b = val[2]
            n =  n = random.randint(0,255)
            r = (r-n) % 255
            g = (g-n) % 255
            b = (b-n) % 255
            pix[i,j] = (r,g,b,1)
            
    im.save(output)