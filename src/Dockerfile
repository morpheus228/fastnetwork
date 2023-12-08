FROM python:3.10-slim-buster
WORKDIR /web

# Upgrade installed packages
RUN apt-get -y update
RUN apt-get -y upgrade

# Install requirements
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]