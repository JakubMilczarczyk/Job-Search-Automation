FROM python:3.12-slim

WORKDIR /scrapers

COPY . /scrapers
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["code", "scrapper.py"]