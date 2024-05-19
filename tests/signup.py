from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class SignupPage:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shn-usage")

        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                                       options = chrome_options)
    def valid_signup(self):
        try:
            self.driver.get("http://localhost:5000/signup")
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").click()
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").send_keys("xyz@gmail.com")
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label/input").click()
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label/input").send_keys("xyz")
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label[2]/input").click()
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label[2]/input").send_keys("xyzabc")
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label[2]").click()
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label[2]/input").send_keys("123456")
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/button").click()
            print("Valid Signup Test - Passed ✅")
            
        except:
            raise Exception("Valid Signup Test - Failed ❌")
        
    def invalid_signup(self):
        try:
            self.driver.get("http://localhost:5000/signup")
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").click()
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").send_keys("xyzgmail.com") # Test remove @ sign
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label/input").click()
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label/input").send_keys("xyz")
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label[2]/input").click()
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label[2]/input").send_keys("xyzabc")
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label[2]").click()
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label[2]/input").send_keys("123456")
            self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/button").click()
            raise Exception("Invalid Signup Test - Failed ❌")
            
        except:
            print("Invalid Signup Test - Passed ✅")
    