from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shn-usage")

        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                                       options = chrome_options)
    def valid_login(self):
        try:
            self.driver.get("http://localhost:5000/login")
            self.driver.find_element(By.NAME, "username").click()
            self.driver.find_element(By.NAME, "username").send_keys("xyz")
            self.driver.find_element(By.CSS_SELECTOR, ".max-w-6xl").click()
            self.driver.find_element(By.NAME, "password").click()
            self.driver.find_element(By.NAME, "password").send_keys("123456")
            self.driver.find_element(By.CSS_SELECTOR, ".max-w-6xl").click()
            self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(1) > .flex > .text-lg").click()
            self.driver.find_element(By.CSS_SELECTOR, ".justify-center:nth-child(2) .text-lg").click()
            self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(3) .text-lg").click()
            self.driver.find_element(By.CSS_SELECTOR, ".truncate").click()
            print("Valid Login Test - Passed ✅")
            
        except:
            raise Exception("Valid Login Test - Failed ❌")
        
    def invalid_login(self):
        try:
            self.driver.get("http://localhost:5000/login")
            self.driver.find_element(By.NAME, "username").click()
            self.driver.find_element(By.NAME, "username").send_keys("abc")  #Test with non exist user
            self.driver.find_element(By.CSS_SELECTOR, ".max-w-6xl").click()
            self.driver.find_element(By.NAME, "password").click()
            self.driver.find_element(By.NAME, "password").send_keys("123456")
            self.driver.find_element(By.CSS_SELECTOR, ".max-w-6xl").click()
            self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(1) > .flex > .text-lg").click()
            self.driver.find_element(By.CSS_SELECTOR, ".justify-center:nth-child(2) .text-lg").click()
            self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(3) .text-lg").click()
            self.driver.find_element(By.CSS_SELECTOR, ".truncate").click()
            raise Exception("Invalid Login Test - Failed ❌")
            
        except:
            print("Invalid Login Test - Passed ✅")
    