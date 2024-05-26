from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def chrome_driver():
    """
    Creates and returns a headless Chrome WebDriver.

    This function initializes a Chrome WebDriver with specific options to run headlessly,
    which means it operates without a graphical user interface. This setup is particularly
    useful for automated testing of web applications in environments that do not support
    a GUI.

    Returns:
        WebDriver: An instance of Chrome WebDriver with configured options.
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--headless")  # Run without a GUI
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=chrome_options)
    
    return driver