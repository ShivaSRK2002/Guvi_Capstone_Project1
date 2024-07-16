import os
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from Test_Project1.Src.locators import PIMPageLocators
from Test_Project1.Src.locators import LoginPageLocators
from Test_Project1.Src.functions import OrangeHRM


# Add comments to explain the purpose of this fixture
@pytest.fixture(scope="class")
def setup(request):
    # Specify the path to the ChromeDriver executable
    chromedriver_path = r"C:\Users\shiva\OneDrive\Desktop\chromedriver.exe"
    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"ChromeDriver not found at path: {chromedriver_path}")

    # Add the ChromeDriver directory to the system PATH
    os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # Initialize the Chrome WebDriver
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    # Set the WebDriver instance as a class attribute
    request.cls.driver = driver
    yield
    # Clean up: quit the WebDriver
    driver.quit()


# Mark the test class to use the "setup" fixture
@pytest.mark.usefixtures("setup")
class TestOrangeHRM:

    # Test case: valid login
    def test_login_valid(self):
        self.driver.get(LoginPageLocators.LOGIN_URL)
        result = OrangeHRM.login(self.driver, LoginPageLocators.VALID_USERNAME, LoginPageLocators.VALID_PASSWORD,
                                 LoginPageLocators)
        assert result == "The user has logged in successfully"

    # Test case: invalid login
    def test_login_invalid(self):
        self.driver.get(LoginPageLocators.LOGIN_URL)
        result = OrangeHRM.login(self.driver, LoginPageLocators.INVALID_USERNAME, LoginPageLocators.INVALID_PASSWORD,
                                 LoginPageLocators)
        assert result == "Invalid credentials"

    # Test case: add employee
    def test_add_employee(self):
        self.driver.get(LoginPageLocators.LOGIN_URL)
        OrangeHRM.Login_test(self.driver, LoginPageLocators.VALID_USERNAME, LoginPageLocators.VALID_PASSWORD,
                             LoginPageLocators)
        result = OrangeHRM.add_employee(self.driver, PIMPageLocators)
        assert result == "Successfully Saved"

    # Test case: edit employee
    def test_edit_employee(self):
        self.driver.get(LoginPageLocators.LOGIN_URL)
        result = OrangeHRM.edit_employee(self.driver, PIMPageLocators)
        assert result == "Successfully Updated"

    # Test case: delete employee
    def test_delete_employee(self):
        self.driver.get(LoginPageLocators.LOGIN_URL)
        result = OrangeHRM.delete_employee(self.driver, PIMPageLocators)
        assert result == "Successfully Deleted"


# Execute the test suite if this script is run directly
if __name__ == "__main__":
    pytest.main(["-v", "test_login.py"])
