from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class DashBoardPage:
    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 3)
        driver.get('http://localhost/moodle/my/')
        
    def go_to_course_creation(self):
        #time.sleep(5)
        site_admin=self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Site administration")))
        site_admin.click()
        course=self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Courses")))
        course.click()
        add_course=self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Add a new course")))
        add_course.click()

        #wait until course creation form appears
        #self.wait.until(EC.presence_of_element_located((By.ID,"id_fullname")))
        