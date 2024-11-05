FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scrapers/ /app/scrapers/
COPY aws_configs/ /app/aws_configs/

CMD ["python3", "scrapers/gpt_scraper.py"]