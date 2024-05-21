from selenium.webdriver.common.by import By
from utils.driver import chrome_driver

def valid_login():
    try:
        driver = chrome_driver()
        driver.get("http://localhost:5000/login")
        driver.find_element(By.XPATH, "//input[@name=\'username\']").click()
        driver.find_element(By.XPATH, "//input[@name=\'username\']").send_keys("xyzabc")
        driver.find_element(By.XPATH, "//input[@name=\'password\']").click()
        driver.find_element(By.XPATH, "//input[@name=\'password\']").send_keys("123456")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/button").click()
        driver.implicitly_wait(30)
        driver.find_element(By.XPATH, "//span[contains(.,\'Home\')]").click()
        driver.find_element(By.XPATH, "//span[contains(.,\'Notifications\')]").click()
        driver.find_element(By.XPATH, "//span[contains(.,\'Profile\')]").click()
        driver.quit()
        
        return True
    
    except:
        return False
    
def invalid_login():
    try:
        driver = chrome_driver()
        driver.get("http://localhost:5000/login")
        driver.find_element(By.XPATH, "//input[@name=\'username\']").click()
        driver.find_element(By.XPATH, "//input[@name=\'username\']").send_keys("abcdefg") # Try login with non existing user
        driver.find_element(By.XPATH, "//input[@name=\'password\']").click()
        driver.find_element(By.XPATH, "//input[@name=\'password\']").send_keys("123456")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/button").click()
        driver.implicitly_wait(30)
        driver.find_element(By.XPATH, "//span[contains(.,\'Home\')]").click()
        driver.find_element(By.XPATH, "//span[contains(.,\'Notifications\')]").click()
        driver.find_element(By.XPATH, "//span[contains(.,\'Profile\')]").click()
        driver.quit()
        
        return False
    
    except:
        return True
