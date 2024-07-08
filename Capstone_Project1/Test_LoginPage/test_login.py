import os
import sys
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Add the project source directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the necessary modules and classes from the project
from Src.functions import testmethods as tm
from Src.locators import LoginLocators as vl
import Src.locators as lc
from Capstone_Project1.Src.locators import LoginLocators as vl


@pytest.fixture(scope="class")
def setup(request):
    # Path to the ChromeDriver executable
    chromedriver_path = r"C:\Users\shiva\OneDrive\Desktop\chromedriver.exe"
    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"ChromeDriver not found at path: {chromedriver_path}")

    # Add the directory containing ChromeDriver to the system path
    os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # Initialize the WebDriver service
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Maximize the browser window
    driver.maximize_window()

    # Attach the WebDriver instance to the test class
    request.cls.driver = driver

    # Provide the driver to the test and quit after the test is done
    yield
    time.sleep(6)
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestLoginPage:

    def test_TC_login_01(self):
        # Navigate to the login URL
        self.driver.get(lc.login_url)

        # Perform login with valid credentials
        result = tm.login_to_OrangeHRM(self.driver, vl.valid_username, vl.valid_password)

        # Assert that login was successful
        assert result == "The user has logged in successfully"

    def test_TC_login_02(self):
        # Navigate to the login URL
        self.driver.get(lc.login_url)

        # Perform login with invalid credentials
        result = tm.login_to_OrangeHRM(self.driver, vl.valid_username, vl.invalid_password)

        # Assert that login failed
        assert result == "Invalid credentials"

    def test_TC_PIM_01(self):
        # Navigate to the login URL
        self.driver.get(lc.login_url)

        # Perform login with valid credentials
        tm.login_to_OrangeHRM_stat(self.driver, vl.valid_username, vl.valid_password)

        # Add a new employee
        result = tm.add_new_employee(self.driver)

        # Assert that the new employee was added successfully
        assert result == "Successfully Saved"

    def test_TC_PIM_02(self):
        # Navigate to the login URL
        self.driver.get(lc.login_url)

        # Perform login with valid credentials (commented out if not needed again)
        # tm.login_to_OrangeHRM_stat(self.driver, vl.valid_username, vl.valid_password)

        # Edit employee details
        result = tm.edit_employee_details(self.driver)

        # Assert that the employee details were updated successfully
        assert result == "Successfully Updated"

    def test_TC_PIM_03(self):
        # Navigate to the login URL
        self.driver.get(lc.login_url)

        # Perform login with valid credentials (commented out if not needed again)
        # tm.login_to_OrangeHRM_stat(self.driver, vl.valid_username, vl.valid_password)

        # Delete an employee
        result = tm.delete_employee(self.driver)

        # Assert that the employee was deleted successfully
        assert result == "Successfully Deleted"


if __name__ == "__main__":
    # Run the tests
    pytest.main(["-v", "test_login.py"])
