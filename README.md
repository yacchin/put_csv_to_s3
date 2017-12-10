# put_csv_to_s3

# create docker image
```
$ docker build -t [tag] .
```

# execute
```
$ docker run -it --env AWS_ACCESS_KEY_ID=[AWS_ACCESS_KEY_ID] --env AWS_SECRET_ACCESS_KEY=[AWS_SECRET_ACCESS_KEY] --env AWS_S3_BUCKET_NAME=[AWS_S3_BUCKET_NAME] [tag]
```
