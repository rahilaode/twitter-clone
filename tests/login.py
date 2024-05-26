from selenium.webdriver.common.by import By
from utils.driver import chrome_driver

def valid_login():
    """
    Attempts a valid login using predefined credentials.

    This function simulates a user logging into the application with valid credentials.
    It navigates to the login page, inputs the correct username and password, and submits the form.
    After logging in, it navigates through several pages to ensure the login was successful.
    If any step fails, it will handle the exception and return False indicating the test failed.

    Returns:
        bool: True if the login was successful, False otherwise.
    """
    try:
        driver = chrome_driver()
        driver.get("http://localhost:5000/login")
        driver.implicitly_wait(60)
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").send_keys("xyz")
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label[2]/input").click()
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
    
def invalid_login():
    """
    Attempts an invalid login using incorrect credentials.

    This function simulates a user trying to log into the application with incorrect credentials.
    It navigates to the login page, inputs an incorrect username and password, and submits the form.
    The function checks if the login attempt fails as expected and returns True if it does,
    indicating the test passed. If the login unexpectedly succeeds, it returns False.

    Returns:
        bool: True if the invalid login test passed (login failed), False otherwise.
    """
    try:
        driver = chrome_driver()
        driver.get("http://localhost:5000/login")
        driver.implicitly_wait(60)
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").click()
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label/input").send_keys("abc") #Try login with non existing user
        driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/div[2]/form/label[2]/input").click()
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
