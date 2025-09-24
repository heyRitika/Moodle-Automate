from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class LoginPageinfo:
    def __init__(self,driver):
        self.driver=driver

    def loginpage(self,username,password):
        self.driver.get('http://localhost/moodle/login/index.php')
        self.driver.find_element(By.ID,"username").send_keys(username)
        self.driver.find_element(By.NAME,"password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,"div.login-form-submit button#loginbtn").click()