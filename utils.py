import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WebAutomationLibrary:
    def __init__(self, driver=None):
        self.driver = driver or webdriver.Chrome()
        self.log = logging.getLogger(__name__)

    def open(self, url):
        self.driver.get(url)
        self.log.info("Opened URL: %s", url)

    def login(self, email, password):
        try:
            email_input = self.driver.find_element(By.ID, "login")
            email_input.send_keys(email)
            self.log.info("Email entered")

            password_input = self.driver.find_element(By.ID, "password")
            password_input.send_keys(password)
            self.log.info("Password entered")

            login_button = self.driver.find_element(By.XPATH, "//*[@id='wrapwrap']/main/div/div/div/form/div[3]/button")
            login_button.click()
            self.log.info("Login button clicked")

            login_successful = self.driver.current_url != "https://dev.mobipreshipement.link/web/login"

            if login_successful:
                self.log.info("Login successful")
                return True
            else:
                self.log.error("Login failed: Invalid credentials")
                return False

        except Exception as e:
            self.log.error("Error logging in: %s", str(e))
            return False

    def create_parcel(self, name, phone, address, city, CRBTV, valuev):
        try:
            parent_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'o_menu_sections')))
            self.log.info("Parent element found")

            link = parent_element.find_elements(By.TAG_NAME, 'a')[1]
            href_create_parcel = link.get_attribute('href')
            self.driver.get(href_create_parcel)
            main_info = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))
            self.log.info("Creation page found")

            delivery_type_button = WebDriverWait(main_info, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Livraison à domicile']")))
            delivery_type_button.click()
            self.log.info("Delivery type selected")

            next_button = WebDriverWait(main_info, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-value='next']")))
            next_button.click()
            self.log.info("Next button clicked")

            name_input = WebDriverWait(main_info, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@name='child_name' and contains(@class, 'o_address_street')])[1]")))
            name_input.send_keys(name)
            self.log.info("Name input filled")

            phone_input = WebDriverWait(main_info, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@name='child_phone' and contains(@class, 'o_address_street')])[1]")))
            phone_input.send_keys(phone)
            self.log.info("Phone input filled")

            address_input = WebDriverWait(main_info, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@name='child_street' and contains(@class, 'o_address_street')])[1]")))
            address_input.send_keys(address)
            self.log.info("Address input filled")

            city_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@name='destination_city']//input[contains(@class, 'o_input')]")))
            city_input.send_keys(city)
            dropdown_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//ul[contains(@class, 'ui-autocomplete')]//li/a")))
            dropdown_option.click()

            next_button = WebDriverWait(main_info, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-value='next']")))
            next_button.click()
            self.log.info("Next button clicked")

            CRBT = WebDriverWait(main_info, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@name='cod']//input[contains(@class, 'o_input')]")))
            CRBT.clear()
            CRBT.send_keys(CRBTV)
            self.log.info("CRBT input filled")

            value = WebDriverWait(main_info, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@name='colis_value']//input[contains(@class, 'o_input')]")))
            value.clear()
            value.send_keys(valuev)
            self.log.info("Value input filled")

            save_button = WebDriverWait(main_info, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@special='save']")))
            save_button.click()
            time.sleep(3)
            self.log.info("Save button clicked")
            try:
                notification = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'o_notification_manager')))
                notification_text = notification.text
                self.log.info("Parcel creation failed due to %s", notification_text)
                return False
            except TimeoutException:
                self.log.info("Parcel created successfully")
                return True

        except Exception as e:
            self.log.error("Error creating parcel: %s", str(e))
            return False