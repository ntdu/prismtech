FROM python:3.9

WORKDIR /app
RUN mkdir -p /app/statics

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/