import os
import sys
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Src.functions import testmethods as tm
from Src.locators import LoginLocators as vl
import Src.locators as lc



@pytest.fixture(scope="class")
def setup(request):
    chromedriver_path = r"C:\Users\shiva\OneDrive\Desktop\chromedriver.exe"
    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"ChromeDriver not found at path: {chromedriver_path}")
    os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    time.sleep(6)
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestLoginPage:

    def test_TC_login_01(self):
        self.driver.get(lc.login_url)
        result = tm.login_to_OrangeHRM(self.driver, vl.valid_username, vl.valid_password)
        assert result == "The user has logged in successfully"

    def test_TC_login_02(self):
        self.driver.get(lc.login_url)
        result = tm.login_to_OrangeHRM(self.driver, vl.valid_username, vl.invalid_password)
        assert result == "Invalid credentials"

    def test_TC_PIM_01(self):
        self.driver.get(lc.login_url)
        tm.login_to_OrangeHRM_stat(self.driver, vl.valid_username, vl.valid_password)
        result = tm.add_new_employee(self.driver)
        assert result == "Successfully Saved"

    def test_TC_PIM_02(self):
        self.driver.get(lc.login_url)
        # tm.login_to_OrangeHRM_stat(self.driver, vl.valid_username, vl.valid_password)
        result = tm.edit_employee_details(self.driver)
        assert result == "Successfully Updated"

    def test_TC_PIM_03(self):
        self.driver.get(lc.login_url)
        # tm.login_to_OrangeHRM_stat(self.driver, vl.valid_username, vl.valid_password)
        result = tm.delete_employee(self.driver)
        assert result == "Successfully Deleted"


if __name__ == "__main__":
    pytest.main(["-v", "test_login.py"])
