from signup import valid_signup, invalid_signup
from login import valid_login, invalid_login


def test(unit, unit_name):
    if unit == True:
        print(f"{unit_name} Test - Passed ✅")
        
    else:
        raise Exception(f"{unit_name} Test - Failed ❌")

if __name__ == "__main__":
    # Signup page test
    test(unit = valid_signup(), unit_name = "Valid Signup")
    test(unit = invalid_signup(), unit_name = "Invalid Signup")
    
    # Login page test
    test(unit = valid_login(), unit_name = "Valid Login")
    test(unit = invalid_login(), unit_name = "Invalid Login")
