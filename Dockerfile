from python:alpine

ADD . /

RUN pip install -r requirements.txt

CMD ["python3","put_csv_to_s3.py"]
