import requests
from bs4 import BeautifulSoup
import time

# Parametry wyszukiwania
search_keyword = "Data Engineer"
location = "remote"  # Możesz zmienić na konkretne miasto lub 'remote' 

# Nagłówki HTTP, aby symulować prawdziwą przeglądarkę
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

# Adres URL No Fluff Jobs z parametrami wyszukiwania
url = f"https://nofluffjobs.com/pl/jobs/{location}?criteria=keyword%3D{search_keyword}"

# Wykonanie żądania do strony
response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Znalezienie wszystkich ofert
    jobs = soup.find_all("a", class_="posting-list-item")  # klasa może się różnić, sprawdź w inspektorze przeglądarki

    for job in jobs:
        # Tytuł oferty
        title = job.find("h3", class_="posting-title__position").text.strip()
        company = job.find("span", class_="company-name").text.strip() if job.find("span", class_="company-name") else "Brak nazwy firmy"
        location = job.find("span", class_="location").text.strip() if job.find("span", class_="location") else "Brak lokalizacji"
        link = "https://nofluffjobs.com" + job['href']

        print(f"Tytuł: {title}")
        print(f"Firma: {company}")
        print(f"Lokalizacja: {location}")
        print(f"Link: {link}")
        print("-----")
        time.sleep(1)  # dodaj przerwę, aby uniknąć blokady

else:
    print("Nie udało się połączyć ze stroną.")
