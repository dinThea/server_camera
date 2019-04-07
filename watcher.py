import time
import cv2 as cv
import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAID4WS4EX33JATYCA'
ACCESS_SECRET_KEY  = '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'
bucket_name = 'hctn'

s3_resource = boto3.resource(
's3',
aws_access_key_id=ACCESS_KEY_ID,
aws_secret_access_key=ACCESS_SECRET_KEY,
config=Config(signature_version='s3v4')
)

cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()
    cv.imwrite('before.jpg', frame)

    s3_resource.Object(bucket_name, 'before.jpg').upload_file(Filename='before.jpg')
    time.sleep(0.01)

