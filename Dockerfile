FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app/app

CMD python manage.py makemigrations && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 app.wsgi:application
