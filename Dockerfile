FROM python:3.9

WORKDIR /usr/src/app

COPY . .

EXPOSE 8000

RUN pip install -r requirements.txt

CMD uvicorn main:app
