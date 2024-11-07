"""Sctipt created to find your dream work."""
import csv
import json
import re
import requests

def load_values(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        lines = file.readlines()

    keywords = [line.strip() for line in lines if line.strip()]
    return keywords



def fetch_jobs_offers(api_key, keywords, locations, job_type):
    url = f"https://pl.jooble.org/api/{api_key}"
    headers = {'kontent-Type': 'appication/json'}
    
    query = {
        'keywords': " ".join(keywords),
        'location': " ".join(locations),
        'page': 1,
        'filters': {
            job_type: True
        }
    }

    all_jobs = []

    while True:

        response = requests.post(url, json=query, headers=headers).json()

        
        jobs = response.get['jobs', []]     # TODO TypeError: 'builtin_function_or_method' object is not subscriptable
        if not jobs:
            break
        all_jobs.extend(jobs)
        query['page'] += 1
        
    
    return all_jobs

    def clean_html(raw_html):
        clean_text = re.sub('<.*?>', '', raw_html)
        return clean_text
    

    def save_to_csv(jobs, filename='job_offers.csv'):
        fieldnames = ['title', 'location', 'snippet', 'salary', 'source', 'type', 'link', 'company', 'updated']

        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for job in jobs:
                job['snippet'] = clean_html(job['snippet'])
                writer.writerow({field: job.get(field, '') for field in fieldnames})

if __name__ == '__main__':

    api_key_path = 'keys/jooble_key.txt'
    keywords = ['python', 'junior', 'trainee']
    locations = ['Warszawa', 'Łódź']
    job_type = 'hybrid'
    
    with open(api_key_path, "r") as file:
        api_key = file.read().strip()


    job_offers = fetch_jobs_offers(keywords=keywords, api_key=api_key, locations=locations, job_type=job_type)
    save_to_csv(job_offers)
