from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class SignupPage:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                                       options = chrome_options)
    def valid_signup(self):
        try:
            self.driver.get("http://localhost:5000/signup")
            self.driver.find_element(By.NAME, "email").click()
            self.driver.find_element(By.NAME, "email").send_keys("xyz@gmail.com")
            self.driver.find_element(By.CSS_SELECTOR, ".max-w-6xl").click()
            self.driver.find_element(By.NAME, "username").click()
            self.driver.find_element(By.NAME, "username").send_keys("xyz")
            self.driver.find_element(By.CSS_SELECTOR, ".max-w-6xl").click()
            self.driver.find_element(By.NAME, "fullName").click()
            self.driver.find_element(By.NAME, "fullName").send_keys("xyzabc")
            self.driver.find_element(By.CSS_SELECTOR, ".max-w-6xl").click()
            self.driver.find_element(By.NAME, "password").click()
            self.driver.find_element(By.NAME, "password").send_keys("123456")
            self.driver.find_element(By.CSS_SELECTOR, ".max-w-screen-xl").click()
            self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(6)").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(1) > .flex > .text-lg").click()
            self.driver.find_element(By.CSS_SELECTOR, ".justify-center:nth-child(2) .text-lg").click()
            self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(3) .text-lg").click()
            self.driver.find_element(By.CSS_SELECTOR, ".truncate").click()
            print("Valid Signup Test - Passed ✅")
            
        except:
            raise Exception("Valid Signup Test - Failed ❌")
        
    def invalid_signup(self):
        try:
            self.driver.get("http://localhost:5000/signup")
            self.driver.find_element(By.NAME, "email").click()
            self.driver.find_element(By.NAME, "email").send_keys("xyzgmail.com")  # Test remove @ sign 
            self.driver.find_element(By.CSS_SELECTOR, ".max-w-6xl").click()
            self.driver.find_element(By.NAME, "username").click()
            self.driver.find_element(By.NAME, "username").send_keys("xyz")
            self.driver.find_element(By.CSS_SELECTOR, ".max-w-6xl").click()
            self.driver.find_element(By.NAME, "fullName").click()
            self.driver.find_element(By.NAME, "fullName").send_keys("xyzabc")
            self.driver.find_element(By.CSS_SELECTOR, ".max-w-6xl").click()
            self.driver.find_element(By.NAME, "password").click()
            self.driver.find_element(By.NAME, "password").send_keys("123456")
            self.driver.find_element(By.CSS_SELECTOR, ".max-w-screen-xl").click()
            self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(6)").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(1) > .flex > .text-lg").click()
            self.driver.find_element(By.CSS_SELECTOR, ".justify-center:nth-child(2) .text-lg").click()
            self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(3) .text-lg").click()
            self.driver.find_element(By.CSS_SELECTOR, ".truncate").click()
            raise Exception("Invalid Signup Test - Failed ❌")
            
        except:
            print("Invalid Signup Test - Passed ✅")
    