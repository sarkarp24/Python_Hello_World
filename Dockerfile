FROM python:3.9-slim-buster

LABEL Name="Python Flask Demo App" Version=3.1.0
LABEL org.opencontainers.image.source = "https://github.com/sarkarp24/Python_Hello_World.git"

ARG srcDir=src
WORKDIR /app
COPY $srcDir/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Hello_World.py .

EXPOSE 5000

CMD ["gunicorn", "-b", "127.0.0.1:5000", "Hello_World:app"]