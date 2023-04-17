FROM python:3

EXPOSE 5000
VOLUME /usr/src/app/ssl

WORKDIR /usr/src/app

COPY ./app/ ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]
