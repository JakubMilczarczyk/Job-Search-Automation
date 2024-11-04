"""Web scrapping script"""

import requests
from bs4 import BeautifulSoup

def scrape_job_listings(url) -> list:
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    job_listings = soup.find_all('div', class_='offer-details')

    jobs= []

    for listing in job_listings:
        job = {
            'title': listing.find('h3').text.strip(),
            'company': listing.find('span', class_='company-name').text.strip(),
            'location': listing.find('span', class_='location').text.strip(),
            'url': 'https://www.pracuj.pl' + listing.find('a')['href']
        }
        jobs.append(job)
    return jobs

if __name__ == '__main__':
    job_listings_url = 'https://www.pracuj.pl/praca/junior%20data%20engineer;kw?redirect=false'
    job_listings = scrape_job_listings(job_listings_url)

    for job in job_listings:
        print(f"Title: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['location']}")
        print(f"URL: {job['url']}")
        print()
