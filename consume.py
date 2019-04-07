
import cv2 as cv
import sys
import datetime
import time
#import argparser
import time
import cv2 as cv
import boto3
import urllib.request as urllib
import numpy as np
from botocore.client import Config
import matplotlib.pyplot as plt

ACCESS_KEY_ID = 'AKIAID4WS4EX33JATYCA'
ACCESS_SECRET_KEY = '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'
bucket_name = 'hctn'


s3_resource = boto3.resource(
's3',
aws_access_key_id=ACCESS_KEY_ID,
aws_secret_access_key=ACCESS_SECRET_KEY,
config=Config(signature_version='s3v4'))


def main():

    while True:

        # Read stream
        urllib.URLopener().retrieve('https://s3.amazonaws.com/hctn/after.jpg', 'after.jpg')
        img = cv.imread('after.jpg')
        cv.imshow('after', img)

main()
