from signup import SignupPage

if __name__ == "__main__":
    # Test signup page
    test_signup_page = SignupPage()
    test_signup_page.valid_signup()
    test_signup_page.invalid_signup()
    test_signup_page.driver.quit()
