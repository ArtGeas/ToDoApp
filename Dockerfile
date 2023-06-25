FROM python:3.11.4-slim

WORKDIR app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY todolist/ .
CMD python manage.py runserver