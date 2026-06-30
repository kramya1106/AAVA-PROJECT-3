"""
Page object for the user registration page.
This page represents the registration form where users can create a new account by providing
username, email, password, and personal information.
"""

from playwright.sync_api import Page
from pages.base_page_object import BasePageObject


class RegistrationPage(BasePageObject):
    """Page object for the user registration page."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.elements.registration_form = "[data-testid='registration-form']"
        self.elements.username_input = "[data-testid='username-input']"
        self.elements.email_input = "[data-testid='email-input']"
        self.elements.password_input = "[data-testid='password-input']"
        self.elements.confirm_password_input = "[data-testid='confirm-password-input']"
        self.elements.first_name_input = "[data-testid='first-name-input']"
        self.elements.last_name_input = "[data-testid='last-name-input']"
        self.elements.submit_button = "[data-testid='submit-button']"
    
    def enter_username(self, username: str):
        """
        Clear and enter username in the username input field.
        
        Args:
            username: The username to enter
        """
        self.username_input.wait_for(state="visible", timeout=10000)
        self.username_input.clear()
        self.username_input.fill(username)
    
    def enter_email(self, email: str):
        """
        Clear and enter email in the email input field.
        
        Args:
            email: The email address to enter
        """
        self.email_input.wait_for(state="visible", timeout=10000)
        self.email_input.clear()
        self.email_input.fill(email)
    
    def enter_password(self, password: str):
        """
        Clear and enter password in the password input field.
        
        Args:
            password: The password to enter
        """
        self.password_input.wait_for(state="visible", timeout=10000)
        self.password_input.clear()
        self.password_input.fill(password)
    
    def enter_confirm_password(self, confirm_password: str):
        """
        Clear and enter confirm password in the confirm password input field.
        
        Args:
            confirm_password: The confirm password to enter (should match password)
        """
        self.confirm_password_input.wait_for(state="visible", timeout=10000)
        self.confirm_password_input.clear()
        self.confirm_password_input.fill(confirm_password)
    
    def enter_first_name(self, first_name: str):
        """
        Clear and enter first name in the first name input field.
        
        Args:
            first_name: The first name to enter
        """
        self.first_name_input.wait_for(state="visible", timeout=10000)
        self.first_name_input.clear()
        self.first_name_input.fill(first_name)
    
    def enter_last_name(self, last_name: str):
        """
        Clear and enter last name in the last name input field.
        
        Args:
            last_name: The last name to enter
        """
        self.last_name_input.wait_for(state="visible", timeout=10000)
        self.last_name_input.clear()
        self.last_name_input.fill(last_name)
    
    def click_submit_button(self):
        """
        Click the Submit button to submit the registration form.
        Waits for the button to be clickable before clicking.
        """
        self.submit_button.wait_for(state="visible", timeout=10000)
        self.submit_button.click()
    
    def fill_registration_form(self, username: str, email: str, password: str, 
                               first_name: str, last_name: str):
        """
        Composite method to fill all registration form fields with provided data.
        
        Args:
            username: The username to enter
            email: The email address to enter
            password: The password to enter (will be used for both password and confirm password)
            first_name: The first name to enter
            last_name: The last name to enter
        """
        self.enter_username(username)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
