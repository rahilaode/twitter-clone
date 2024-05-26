from selenium.webdriver.common.by import By
from utils.driver import chrome_driver

def valid_signup():    
    """
    Attempts a valid signup using valid credentials.
    This function simulates a user signing up with valid credentials.
    It navigates to the signup page, inputs the correct username and password, and submits the form.
    After signing up, it navigates through several pages to ensure the signup was successful.
    If any step fails, it will handle the exception and return False indicating the test failed.
    Returns:
        bool: True if the signup was successful, False otherwise.
    """
    try:
        driver = chrome_driver()
        driver.get("http://localhost:5000/signup")
        driver.implicitly_wait(60)
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").send_keys("xyz@gmail.com")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label/input").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label/input").send_keys("xyz")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label[2]/input").send_keys("xyzabc")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label[2]").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label[2]/input").send_keys("123456")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/button").click()
        driver.implicitly_wait(60)
        driver.find_element(By.XPATH, "//span[contains(.,\'Home\')]").click()
        driver.find_element(By.XPATH, "//span[contains(.,\'Notifications\')]").click()
        driver.find_element(By.XPATH, "//span[contains(.,\'Profile\')]").click()
        driver.quit()
        
        return True
        
    except:
        return False
        
def invalid_signup():
    """
    Attempts an invalid signup using invalid credentials.
    This function simulates a user signing up with invalid credentials.
    It navigates to the signup page, inputs the incorrect username and password, and submits the form.
    The function checks if the signup attempt fails as expected and returns True if it does,
    indicating the test passed. If the signup unexpectedly succeeds, it returns False.
    Returns:
        bool: True if the invalid signup test passed (signup failed), False otherwise.
    """
    try:
        driver = chrome_driver()
        driver.get("http://localhost:5000/signup")
        driver.implicitly_wait(60)
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").send_keys("xyzagmail.com") # Try don't use @ sign
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label/input").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label/input").send_keys("xyza")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/div/label[2]/input").send_keys("xyzabc")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label[2]").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label[2]/input").send_keys("123456")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/button").click()
        driver.implicitly_wait(60)
        driver.find_element(By.XPATH, "//span[contains(.,\'Home\')]").click()
        driver.find_element(By.XPATH, "//span[contains(.,\'Notifications\')]").click()
        driver.find_element(By.XPATH, "//span[contains(.,\'Profile\')]").click()
        driver.quit()
        
        return False
    
    except:
        return True