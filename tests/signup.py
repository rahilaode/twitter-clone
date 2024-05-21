from selenium.webdriver.common.by import By
from utils.driver import chrome_driver

def valid_signup():    
    try:
        driver = chrome_driver()
        driver.get("http://localhost:5000/signup")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").send_keys("xyz@gmail.com")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label/input").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label/input").send_keys("xyz")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label[2]/input").send_keys("xyzabc")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label[2]").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label[2]/input").send_keys("123456")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/button").click()
        # driver.implicitly_wait(30)
        # driver.find_element(By.XPATH, "//span[contains(.,\'Home\')]").click()
        # driver.find_element(By.XPATH, "//span[contains(.,\'Notifications\')]").click()
        # driver.find_element(By.XPATH, "//span[contains(.,\'Profile\')]").click()
        driver.quit()
        
        return True
        
    except:
        return False
        
def invalid_signup():
    try:
        driver = chrome_driver()
        driver.get("http://localhost:5000/signup")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").send_keys("xyzagmail.com") # Try don't use @ sign
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label/input").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label/input").send_keys("xyza")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label[2]/input").send_keys("xyzabc")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label[2]").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label[2]/input").send_keys("123456")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/button").click()
        # driver.implicitly_wait(30)
        # driver.find_element(By.XPATH, "//span[contains(.,\'Home\')]").click()
        # driver.find_element(By.XPATH, "//span[contains(.,\'Notifications\')]").click()
        # driver.find_element(By.XPATH, "//span[contains(.,\'Profile\')]").click()
        driver.quit()
        
        return False
    
    except:
        return True