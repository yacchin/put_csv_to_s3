import boto3
from settings import AWS_S3_BUCKET_NAME

if __name__ == '__main__':
    s3_client = boto3.client('s3')
    csv_file = open('null.csv', 'w')
    csv_file.close()
    s3_client.upload_file('null.csv', AWS_S3_BUCKET_NAME, 'null.csv')
