from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub',
    options=options
)

driver.get(f'https://nofluffjobs.com/pl/praca-zdalna/Python?criteria=city%3Dhybrid,warszawa%20%20seniority%3Dtrainee,junior')
print('Title:', driver.title)

driver.quit()
