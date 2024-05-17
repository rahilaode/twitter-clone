from signup import SignupPage
from login import LoginPage

if __name__ == "__main__":
    # Signup page test
    signup_page_test = SignupPage()
    signup_page_test.valid_signup()
    signup_page_test.invalid_signup()
    signup_page_test.driver.quit()
    
    # Login page test
    login_page_test = LoginPage()
    login_page_test.valid_login()
    login_page_test.invalid_login()
    login_page_test.driver.quit()
