import pytest
from pages.login import *
from pages.dashboard import *
from pages.addCourse import *
from pages.enrollment_page import *
import time

@pytest.mark.usefixtures("activatebrowser")
class TestMoodleAutomation:
    def test_login_create_course_enroll(self):
        try:
            # Login 
            login = LoginPageinfo(self.driver)
            login.loginpage('admin', 'Admin@123')
            
            # Wait for login to complete
            time.sleep(2)
            
            # Dashboard
            dash = DashBoardPage(self.driver)
            dash.go_to_course_creation()
            
            # Wait for course creation page to load
            time.sleep(2)
            
            # Add a new course
            course = AddNewCourse(self.driver)
            course.create_course("Personal Home Page", "PHP")
            
            # Verify course creation
            assert course.is_course_created("Personal Home Page"), "Course was not created successfully"
            time.sleep(2)
            # Enroll user
            enroll = EnrollmentPage(self.driver)
            enrollment_success=enroll.enroll_user("Pardeep Singh")
            
            # Final assertion
            assert enrollment_success=="User enrollment done","User enrollment failed"
            print("Enrollment process completed")

            #Additional verification
            time.sleep(3)
            
                
        except Exception as e:
            # Take screenshot for debugging
            self.driver.save_screenshot(f'test_failure_{int(time.time())}.png')
            print(f"Test failed with error: {str(e)}")
            raise