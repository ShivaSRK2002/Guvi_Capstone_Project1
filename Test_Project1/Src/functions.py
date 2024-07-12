from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrangeHRM:
    @staticmethod
    def login(driver, username, password, locators):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.USERNAME_INPUT))).send_keys(username)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.PASSWORD_INPUT))).send_keys(password)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.SUBMIT_BUTTON))).click()
        try:
            WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, locators.PROFILE_BUTTON))).click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, locators.LOGOUT_BUTTON))).click()
            return "The user has logged in successfully"
        except TimeoutException:
            return "Invalid credentials"

    @staticmethod
    def Login_test(driver, username, password, locators):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.USERNAME_INPUT))).send_keys(username)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.PASSWORD_INPUT))).send_keys(password)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.SUBMIT_BUTTON))).click()
        try:
            WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, locators.PROFILE_BUTTON))).click()
            return "The user has logged in successfully"
        except TimeoutException:
            return "Invalid credentials"

    @staticmethod
    def add_employee(driver, locators):
        WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, locators.PIM_MODULE))).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.ADD_EMPLOYEE_BUTTON))).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.FIRST_NAME_INPUT))).send_keys("Shiva")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.LAST_NAME_INPUT))).send_keys("RK")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.SAVE_BUTTON))).click()
        try:
            success_message = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, locators.SUCCESS_MESSAGE)))
            return success_message.text
        except TimeoutException:
            return "Unable to save"

    @staticmethod
    def edit_employee(driver, locators):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.PIM_MODULE))).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.EMPLOYEE_LIST_BUTTON))).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.SELECT_USER_EDIT))).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.EDIT_BUTTON))).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.MALE_BUTTON))).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.SUBMIT_EDIT_BUTTON))).click()
        try:
            success_message = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, locators.UPDATE_SUCCESS_MESSAGE)))
            return success_message.text
        except TimeoutException:
            return "Unable to update user details"

    @staticmethod
    def delete_employee(driver, locators):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.PIM_MODULE))).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.EMPLOYEE_LIST_BUTTON))).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.SELECT_USER_DELETE))).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.DELETE_BUTTON))).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.CONFIRM_DELETE_BUTTON))).click()
        try:
            success_message = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, locators.DELETE_SUCCESS_MESSAGE)))
            return success_message.text
        except TimeoutException:
            return "Unable to delete the selected user"
