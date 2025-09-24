from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
# ADD THIS LINE:
from selenium.common.exceptions import TimeoutException
import time

class EnrollmentPage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,20)

    def enroll_user(self,username):
        try:
            # Click on Participants
            self.driver.find_element(By.LINK_TEXT,'Participants').click()
            #enrol button
            enrol_btn=self.driver.find_element(By.CSS_SELECTOR,"input.btn-primary[value='Enrol users']")
            enrol_btn.click()
            time.sleep(2)
            # Wait for the search input to be visible and interactable
            search_input=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[contains(@id,'form_autocomplete_input-') and @placeholder='Search']")))
            #Clear and enter the username
            search_input.clear()
            search_input.send_keys(username)
            time.sleep(2)
            user_found=self._select_user_from_dropdown(username)
            if not user_found:
                raise Exception(f"User '{username}' not found in the dropdown")
            #Select Student role
            self.select_student_role()
            #Click final enroll button
            return self._click_final_enroll_btn()
            #Wait for enrollment to complete and verify
            # return self._verify_enrollment_success(username)
        
        except TimeoutException as e:
                    print(f"Timeout error during enrollment: {e}")
                    raise
        except Exception as e:
                print(f"Error during user enrollment: {e}")
                raise
    def _select_user_from_dropdown(self,username):
                # Wait for suggestions dropdown to appear
                try:
                    user_dropdown=self.wait.until(EC.presence_of_element_located((By.XPATH,"//ul[starts-with(@id,'form_autocomplete_suggestions-') and @aria-label='Suggestions']")))
                    user_options=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//ul[starts-with(@id,'form_autocomplete_suggestions-') and @aria-label='Suggestions']//li[@role='option']")))
            # user_list=user_dropdown.find_elements(By.TAG_NAME,"li")
                    for user in user_options:
                        try:
                    # Look for the span containing the name (second span in the structure)
                            name_spans=user.find_elements(By.XPATH,".//span/span")
                            if name_spans:
                                user_name=name_spans[0].text.strip()
                                print(f"Found user option: {user_name}")  # Debug print
                                if user_name==username:
                                    self.driver.execute_script("arguments[0].scrollIntoView(true);",user)
                                    time.sleep(1)
                                    user.click()
                                    print(f"Selected user: {username}")  # Debug print
                                    return True
                        except Exception as e:
                            print(f"Error processing user option:{e}")
                            continue
                    return False
                except Exception as e:
                    print(f"Error selecting user from dropdown: {e}")
                    raise

    def select_student_role(self):
        """Select Student role from dropdown"""
        try:
            time.sleep(2)
            #self.wait.until(EC.presence_of_element_located((By.XPATH,"//input[contains(id,'form_autocomplete_input-') and @placeholder='Search']"))).click()
            select_role= self.wait.until(EC.presence_of_element_located((By.ID,"id_roletoassign")))
            selected_role=Select(select_role)
            selected_role.select_by_visible_text("Student")
            print("Selected Student role")  # Debug print
            time.sleep(2)
        except Exception as e:
            print(f"Error selecting role: {e}")
            raise
    def _click_final_enroll_btn(self):
          try:
            time.sleep(2)
            final_enrol_button=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Enrol users') and @type='button']")))
            final_enrol_button.click()
            print("Clicked final enrol button")  # Debug print
            time.sleep(3)
            print("Enrollment process completed success")
            return "User enrollment done" 
          except Exception as e:
            print(f"Error clicking final enrol button: {e}")
            raise
          
    
                
        

        



        # #.driver.find_element(By.ID,"form_autocomplete_downarrow-1757487267475").click()
        # dropdown=self.driver.find_elements(By.CSS_SELECTOR,"ul#form_autocomplete_suggestions-1757487267475[role='listbox']//li")
        # for i in dropdown:
        #     if username in i.text:
        #         i.click()
        #         break
        # suggestion=Select(self.driver.find_element(By.NAME,"roletoassign"))
        # suggestion.select_by_visible_text("Student")
        # self.driver.find_element(By.CSS_SELECTOR,"btton.btn-primary[type='button']").click()
