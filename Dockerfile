FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/

RUN pip install requirements.txt

COPY . /app/

CMD [ "python", "main.py" ]