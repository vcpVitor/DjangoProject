FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install Django

CMD python manage.py runserver
