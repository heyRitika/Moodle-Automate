from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

class AddNewCourse:
    def __init__(self, driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,15)
    def create_course(self,course_fullname,course_shortname):
         try:
            self.driver.find_element(By.ID,"id_fullname").send_keys(course_fullname)
            self.driver.find_element(By.ID,"id_shortname").send_keys(course_shortname)
                
                #Handle categoy
            self.select_category("Category 1")
            #submit form
            self.submit_form()
         except Exception as e:
             print(f"Error creating course: {str(e)}")

    def select_category(self,category_name):
        try:
            input_element=self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.form-control[placeholder*='Search']")))
            input_element.clear()
            input_element.send_keys(category_name)
            time.sleep(0.5)
            suggestion_container=self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"ul.form-autocomplete-suggestions li")))
            options=suggestion_container.find_elements(By.TAG_NAME,"li")
            category_selected=False
            for option in options:
                if option.text.strip()==category_name:
                    #handle with js
                    self.driver.execute_script("arguments[0].scrollIntoView(true);",options)
                    time.sleep(0.5)
                try:
                    option.click()
                    category_selected=True
                    break
                except ElementClickInterceptedException:
                    self.driver.execute_script("arguments[0].click();",option)
                    category_selected=True

            if not category_selected:
                input_element.send_keys(Keys.ARROW_DOWN)
                input_element.send_keys(Keys.ENTER)
            
            #verify selection was made
            self.verify_category_selection()
        except TimeoutError:
            print("category selection timed out")

    def verify_category_selection(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".form-autocomplete-selection")))
        except TimeoutException:
            print("Warning: Could not verify category selection")

    def submit_form(self):
        """Submit the course creation"""
        try:
            submit_btn=self.wait.until(EC.presence_of_element_located((By.ID,"id_saveanddisplay")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);",submit_btn)
            submit_btn=self.wait.until(EC.element_to_be_clickable((By.ID,"id_saveanddisplay")))
            try:
                submit_btn.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();",submit_btn)
                time.sleep(3)

        except TimeoutException:
            print("Submit button not found or not clickable")

    def is_course_created(self,course_fullname):
        return course_fullname in self.driver.page_source


