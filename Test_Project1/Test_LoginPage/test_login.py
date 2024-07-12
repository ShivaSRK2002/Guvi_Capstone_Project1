import os
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from Test_Project1.Src.locators import PIMPageLocators
from Test_Project1.Src.locators import LoginPageLocators
from Test_Project1.Src.functions import OrangeHRM
sys.path.insert(0, '../Test_Project1')


# Add the project source directory to the system path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# from Test_Project1.Src.functions import OrangeHRM
# from Test_Project1.Src.locators import LoginPageLocators, PIMPageLocators
# from E:\Git\Guvi_Capstone_Project1\Test_Project1\Src
# from ..Src.locators import LoginPageLocators, PIMPageLocators
# from ..Src.functions import OrangeHRM


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
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestOrangeHRM:

    def test_login_valid(self):
        self.driver.get(LoginPageLocators.LOGIN_URL)
        result = OrangeHRM.login(self.driver, LoginPageLocators.VALID_USERNAME, LoginPageLocators.VALID_PASSWORD,
                                 LoginPageLocators)
        assert result == "The user has logged in successfully"

    def test_login_invalid(self):
        self.driver.get(LoginPageLocators.LOGIN_URL)
        result = OrangeHRM.login(self.driver, LoginPageLocators.INVALID_USERNAME, LoginPageLocators.INVALID_PASSWORD,
                                 LoginPageLocators)
        assert result == "Invalid credentials"

    def test_add_employee(self):
        self.driver.get(LoginPageLocators.LOGIN_URL)
        OrangeHRM.Login_test(self.driver, LoginPageLocators.VALID_USERNAME, LoginPageLocators.VALID_PASSWORD,
                             LoginPageLocators)
        result = OrangeHRM.add_employee(self.driver, PIMPageLocators)
        assert result == "Successfully Saved"

    def test_edit_employee(self):
        self.driver.get(LoginPageLocators.LOGIN_URL)
        result = OrangeHRM.edit_employee(self.driver, PIMPageLocators)
        assert result == "Successfully Updated"

    def test_delete_employee(self):
        self.driver.get(LoginPageLocators.LOGIN_URL)
        result = OrangeHRM.delete_employee(self.driver, PIMPageLocators)
        assert result == "Successfully Deleted"


if __name__ == "__main__":
    pytest.main(["-v", "test_login.py"])
