
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def take_screenshots():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        driver.get('http://localhost:8000/sitemap')
        time.sleep(1) # Allow page to load

        # Light mode screenshot
        driver.save_screenshot('/home/jules/verification/04_sitemap_light.png')

        # Dark mode screenshot
        theme_switcher = driver.find_element(By.ID, 'theme-switcher')
        theme_switcher.click()
        time.sleep(1) # Allow theme to change
        driver.save_screenshot('/home/jules/verification/04_sitemap_dark.png')

    finally:
        driver.quit()

if __name__ == "__main__":
    take_screenshots()
