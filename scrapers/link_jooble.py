print('Hello from Docker Container!')

import csv
import json
import re
import requests
from bs4 import BeautifulSoup
import polars as pl


def load_config(file_path):
    config = {}

    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            if line.strip():
                key, value = line.strip().split("=", 1)
                if key == 'keywords':
                    config[key] = value.split(', ')
                elif key == 'locations':
                    config[key] = value.split(', ')
                elif key == 'job_types':
                    config[key] = value.split(', ')
                else:
                    config[key] = value.split()
    return config

def fetch_jobs_offers(api_key):
    url = f"https://pl.jooble.org/api/{api_key}"
    headers = {'Content-Type': 'application/json'}
    
    query = {
        'keywords': 'python',
        'page': 1
    }

    all_jobs = []
    response = requests.post(url, json=query, headers=headers)

    if response.status_code != 200:
        print("Error:", response.status_code)
        print("Response text:", response.text)
        response.raise_for_status()

    try:
        response_data = response.json()
    except requests.exceptions.JSONDecodeError as e:
        print("JSONDecodeError:", e)
        print("Response text:", response.text)
        return []

    while True:
        jobs = response_data.get('jobs', [])
        if not jobs:
            break
        all_jobs.extend(jobs)
        query['page'] += 1
        response = requests.post(url, json=query, headers=headers)
        response_data = response.json()
    
    return all_jobs

def clean_html(raw_html):
    clean_text = BeautifulSoup(text, "html.parser").get_text()
    clean_text = re.sub(r'&nbsp;', ' ', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text

# TODO add def to chenge data into pl.dataframe, split salary column to min and max salary column, set datatypes for columns

def save_to_csv(jobs, file_path='job_offers.csv'):
    fieldnames = ['title', 'location', 'snippet', 'salary', 'source', 'type', 'link', 'company', 'updated']

    with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for job in jobs:
            job['snippet'] = clean_html(job['snippet'])
            writer.writerow({field: job.get(field, '') for field in fieldnames})

if __name__ == '__main__':
    api_key_path = 'config/jooble_key.txt'

    with open(api_key_path, "r") as file:
        api_key = file.read().strip()

    job_offers = fetch_jobs_offers(api_key=api_key)
    save_to_csv(job_offers)
