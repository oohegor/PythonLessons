FROM python:3.6

RUN mkdir -p /usr/src/app 
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python","app.py"]