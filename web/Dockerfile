FROM python:alpine

ENV FLASK_PORT=3000

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD app /usr/src/app
WORKDIR /usr/src/app

EXPOSE 3000

CMD ["python3", "main.py"]