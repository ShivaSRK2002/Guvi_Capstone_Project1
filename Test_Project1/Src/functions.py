from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Define the OrangeHRM class with static methods to interact with the OrangeHRM application
class OrangeHRM:

    # Static method to log in to the application
    @staticmethod
    def login(driver, username, password, locators):
        # Wait for the username input to be present and then enter the username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.USERNAME_INPUT))).send_keys(username)

        # Wait for the password input to be present and then enter the password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.PASSWORD_INPUT))).send_keys(password)

        # Wait for the submit button to be present and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.SUBMIT_BUTTON))).click()

        try:
            # Wait for the URL to contain 'dashboard', indicating a successful login
            WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

            # Wait for the profile button to be present and then click it
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, locators.PROFILE_BUTTON))).click()

            # Wait for the logout button to be present and then click it
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, locators.LOGOUT_BUTTON))).click()

            return "The user has logged in successfully"
        except TimeoutException:
            return "Invalid credentials"

    # Static method to test login functionality
    @staticmethod
    def Login_test(driver, username, password, locators):
        # Wait for the username input to be present and then enter the username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.USERNAME_INPUT))).send_keys(username)

        # Wait for the password input to be present and then enter the password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.PASSWORD_INPUT))).send_keys(password)

        # Wait for the submit button to be present and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.SUBMIT_BUTTON))).click()

        try:
            # Wait for the URL to contain 'dashboard', indicating a successful login
            WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

            # Wait for the profile button to be present and then click it
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, locators.PROFILE_BUTTON))).click()

            return "The user has logged in successfully"
        except TimeoutException:
            return "Invalid credentials"

    # Static method to add a new employee
    @staticmethod
    def add_employee(driver, locators):
        # Wait for the PIM module to be present and then click it
        WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, locators.PIM_MODULE))).click()

        # Wait for the add employee button to be present and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.ADD_EMPLOYEE_BUTTON))).click()

        # Wait for the first name input to be present and then enter the first name
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.FIRST_NAME_INPUT))).send_keys("Shiva")

        # Wait for the last name input to be present and then enter the last name
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.LAST_NAME_INPUT))).send_keys("RK")

        # Wait for the save button to be present and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.SAVE_BUTTON))).click()

        try:
            # Wait for the success message to be present and then return its text
            success_message = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, locators.SUCCESS_MESSAGE)))
            return success_message.text
        except TimeoutException:
            return "Unable to save"

    # Static method to edit an employee's details
    @staticmethod
    def edit_employee(driver, locators):
        # Wait for the PIM module to be present and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.PIM_MODULE))).click()

        # Wait for the employee list button to be present and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.EMPLOYEE_LIST_BUTTON))).click()

        # Wait for the user to be selected for editing and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.SELECT_USER_EDIT))).click()

        # Wait for the edit button to be present and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.EDIT_BUTTON))).click()

        # Wait for the male button to be present and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.MALE_BUTTON))).click()

        # Wait for the submit edit button to be present and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.SUBMIT_EDIT_BUTTON))).click()

        try:
            # Wait for the update success message to be present and then return its text
            success_message = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, locators.UPDATE_SUCCESS_MESSAGE)))
            return success_message.text
        except TimeoutException:
            return "Unable to update user details"

    # Static method to delete an employee
    @staticmethod
    def delete_employee(driver, locators):
        # Wait for the PIM module to be present and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.PIM_MODULE))).click()

        # Wait for the employee list button to be present and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.EMPLOYEE_LIST_BUTTON))).click()

        # Wait for the user to be selected for deletion and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.SELECT_USER_DELETE))).click()

        # Wait for the delete button to be present and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.DELETE_BUTTON))).click()

        # Wait for the confirm delete button to be present and then click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.CONFIRM_DELETE_BUTTON))).click()

        try:
            # Wait for the delete success message to be present and then return its text
            success_message = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, locators.DELETE_SUCCESS_MESSAGE)))
            return success_message.text
        except TimeoutException:
            return "Unable to delete the selected user"
