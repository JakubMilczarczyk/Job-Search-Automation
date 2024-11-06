from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Opcje dla Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Uruchom w tle (bez GUI)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Ścieżka do chromedrivera
service = Service("ścieżka/do/chromedriver")  # Upewnij się, że masz zainstalowanego chromedrivera

# Inicjalizacja przeglądarki
driver = webdriver.Chrome(service=service, options=chrome_options)

# Adres URL No Fluff Jobs z parametrami wyszukiwania
url = f"https://nofluffjobs.com/pl/praca-zdalna/Python?criteria=city%3Dhybrid,warszawa%20%20seniority%3Dtrainee,junior"

# Przechodzimy na stronę
driver.get(url)
time.sleep(3)  # Czekaj na załadowanie strony

# Znalezienie wszystkich ofert
jobs = driver.find_elements(By.CLASS_NAME, "posting-list-item")  # Klasa może się różnić, sprawdź w inspektorze przeglądarki

for job in jobs[:3]:  # Pobieranie tylko 3 ofert
    title_element = job.find_element(By.CLASS_NAME, "posting-title__position")
    title = title_element.text.strip()
    link = "https://nofluffjobs.com" + job.get_attribute('href')

    # Przechodzenie do szczegółów oferty
    driver.get(link)
    time.sleep(3)  # Czekaj na załadowanie szczegółów oferty

    # Pobieranie tytułu i opisu
    meta_title = driver.find_element(By.CSS_SELECTOR, 'meta[property="og:title"]')
    title_and_company = meta_title.get_attribute("content") if meta_title else "Brak informacji o tytule i firmie"
    
    meta_description = driver.find_element(By.CSS_SELECTOR, 'meta[property="og:description"]')
    description = meta_description.get_attribute("content") if meta_description else "Brak opisu"

    print(f"Tytuł i firma: {title_and_company}")
    print(f"Opis: {description}")
    print(f"Link: {link}")
    print("-----")

    driver.back()  # Powrót do strony z listą ogłoszeń
    time.sleep(3)  # Czekaj na załadowanie listy

# Zamknięcie przeglądarki
driver.quit()
