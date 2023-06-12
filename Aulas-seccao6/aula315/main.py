# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 20

    options = ()
    browser = make_chrome_browser(*options)

    browser.get('https://www.google.com/')
    # Aceitar cookie
    element = browser.find_element(By.XPATH, '//*[@id="L2AGLb"]/div')
    element.click()

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    # Escreve no input
    search_input.send_keys('Hello World!')

    # Pesquisa o que foi escrito no input
    searching = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
    searching.click()

    # Resultados
    results = browser.find_element(By.ID, 'search')

    # clicando no primeiro resultado que aparece
    links = results.find_elements(By.TAG_NAME, 'a')
    links[0].click()

    # Fechar navegador
    # browser.quit()


    sleep(TIME_TO_WAIT)