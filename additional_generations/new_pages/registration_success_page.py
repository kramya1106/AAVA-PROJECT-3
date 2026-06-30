"""
Page object for the registration success/confirmation page.
This page is displayed after successful user registration and shows a success message.
"""

from playwright.sync_api import Page
from pages.base_page_object import BasePageObject


class RegistrationSuccessPage(BasePageObject):
    """Page object for the registration success page."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.elements.success_message = "[data-testid='success-message']"
    
    def verify_success_message_visible(self):
        """
        Verify that the success message is visible on the page.
        Waits for the success message element to be visible.
        
        Returns:
            bool: True if success message is visible, False otherwise
        """
        try:
            self.success_message.wait_for(state="visible", timeout=15000)
            return self.success_message.is_visible()
        except Exception:
            return False
    
    def get_success_message_text(self) -> str:
        """
        Get the text content of the success message.
        
        Returns:
            str: The text content of the success message
        """
        self.success_message.wait_for(state="visible", timeout=15000)
        return self.success_message.text_content()
    
    def verify_success_message_text(self, expected_message: str) -> bool:
        """
        Verify that the success message displays the expected text.
        
        Args:
            expected_message: The expected text to verify (can be partial match)
        
        Returns:
            bool: True if message text matches expected, False otherwise
        """
        actual_message = self.get_success_message_text()
        return expected_message in actual_message
