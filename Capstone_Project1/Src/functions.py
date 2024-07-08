import os
import time
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Src.locators import LoginLocators as lc


class testmethods:
    @pytest.fixture
    def browser(self):
        # Path to the ChromeDriver executable
        chromedriver_path = r"C:\Users\shiva\OneDrive\Desktop\chromedriver.exe"
        if not os.path.exists(chromedriver_path):
            raise FileNotFoundError(f"ChromeDriver not found at path: {chromedriver_path}")
        os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

        # Set Chrome options
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        # Initialize the WebDriver service
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Provide the driver to the test and quit after the test is done
        yield driver
        time.sleep(6)
        driver.quit()

    @staticmethod
    def login_to_OrangeHRM(driver, username, password):
        # Wait for the username field to be present and enter the username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.username_element))).send_keys(username)

        # Wait for the password field to be present and enter the password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.password_element))).send_keys(password)

        # Wait for the submit button to be present and click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.submit_element))).click()

        try:
            # Wait for the dashboard URL to indicate successful login
            WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

            # Wait for the profile button and click it
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, lc.profile_button_element))).click()

            # Wait for the logout button and click it
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, lc.logout_button_element))).click()

            return "The user has logged in successfully"
        except TimeoutException:
            return "Invalid credentials"

    @staticmethod
    def add_new_employee(driver):
        # Click the PIM module
        pim_module = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.pim)))
        pim_module.click()

        # Click the add employee button
        add_employee = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.add_employee)))
        add_employee.click()

        # Enter first name and last name
        first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.fir_nam)))
        last_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.las_nam)))
        first_name.send_keys("Shiva")
        last_name.send_keys("RK")

        # Click the save button
        save_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.save)))
        save_button.click()

        try:
            # Wait for the success message and return its text
            toaster = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, lc.saved_success)))
            value = toaster.text
            return value
        except TimeoutException:
            value = "Unable to save"
            return value

    @staticmethod
    def edit_employee_details(driver):
        # Click the PIM module
        pim_module = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.pim)))
        pim_module.click()

        # Click the employee list
        employee_list = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.employee_list)))
        employee_list.click()

        # Select the user to edit and click the edit button
        select_user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.sel_user_edit)))
        select_user.click()
        edit_user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.click_edit)))
        edit_user.click()

        # Click the male gender button
        male_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.male_button)))
        male_button.click()

        # Click the submit button to save changes
        submit_edited_user = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.submit_edit_user)))
        submit_edited_user.click()

        try:
            # Wait for the success message and return its text
            toaster = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, lc.update_success)))
            value = toaster.text
            return value
        except TimeoutException:
            value = "Unable to update user details"
            return value

    @staticmethod
    def login_to_OrangeHRM_stat(driver, username, password):
        # Wait for the username field to be present and enter the username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.username_element))).send_keys(username)

        # Wait for the password field to be present and enter the password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.password_element))).send_keys(password)

        # Wait for the submit button to be present and click it
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.submit_element))).click()

        try:
            # Wait for the dashboard URL to indicate successful login
            WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
            return "The user has logged in successfully"
        except TimeoutException:
            return "Invalid credentials"

    @staticmethod
    def delete_employee(driver):
        # Click the PIM module
        pim_module = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.pim)))
        pim_module.click()

        # Click the employee list
        employee_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.employee_list)))
        employee_list.click()

        # Select the user to delete and click the delete button
        select_user_del = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.sel_user_del)))
        select_user_del.click()
        delete_user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.delete_user)))
        delete_user.click()

        # Confirm the deletion
        confirm_delete = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.confirm_del)))
        confirm_delete.click()

        try:
            # Wait for the success message and return its text
            toaster = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, lc.del_success)))
            value = toaster.text
            return value
        except TimeoutException:
            value = "Unable to delete the selected user"
            return value
