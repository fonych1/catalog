FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install pip-tools
RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]