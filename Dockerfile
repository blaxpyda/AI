FROM python:3.13-alpine

ADD requirements.txt .

ADD main.py .

ADD .env .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]
