FROM python:3

WORKDIR /usr/src/app

COPY app/requirements.txt ./

RUN pip install -r requirements.txt

COPY ./app .

EXPOSE 8080

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "wsgi:app" ]
# 
