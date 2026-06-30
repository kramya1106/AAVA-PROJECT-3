"""
Page object for the application home page.
This page represents the entry point to the application and provides navigation to the registration page.
"""

from playwright.sync_api import Page
from pages.base_page_object import BasePageObject


class HomePage(BasePageObject):
    """Page object for the application home page."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.elements.home_page_container = "[data-testid='home-page']"
        self.elements.register_button = "[data-testid='register-button']"
    
    def navigate_to_home_page(self):
        """
        Navigate to the application home page using the base URL from configuration.
        Waits for the page to load and verifies the home page container is visible.
        """
        self.page.goto("/")
        self.page.wait_for_load_state("networkidle", timeout=30000)
        self.home_page_container.wait_for(state="visible", timeout=30000)
    
    def click_register_button(self):
        """
        Click the Register button to navigate to the registration page.
        Waits for the button to be clickable before clicking.
        """
        self.register_button.wait_for(state="visible", timeout=10000)
        self.register_button.click()
        self.page.wait_for_load_state("networkidle", timeout=30000)
