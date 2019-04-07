import urllib2
import cv2 as cv
import numpy as np


while True:
    response = urllib2.urlopen('https://s3.console.aws.amazon.com/s3/buckets/hctn/before.jpg')
    image = np.asarray(bytearray(response.read()), dtype='uint8')
    image = cv.imdecode(image, cv.IMREAD_COLOR)
    print (image) 
    cv.imshow('img', image)
