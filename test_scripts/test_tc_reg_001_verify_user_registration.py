"""
Test Case ID: TC_REG_001
Title: Verify user registration with valid details
Description: This test case verifies that a new user can successfully register on the 
application by providing valid details including username, email, password, and personal 
information. The test covers the complete registration flow from navigating to the 
registration page to receiving a confirmation message.
"""

import traceback
import pytest
from core.playwright_manager import PlaywrightManager
from core.settings import framework_logger
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.registration_success_page import RegistrationSuccessPage
from playwright.sync_api import expect
import test_flows_common.test_flows_common as common
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@pytest.mark.usefixtures("main_execution")
def test_tc_reg_001_verify_user_registration(stage_callback, tc_tracer, reporter):
    tcid = "TC_REG_001"
    current_step = "Step 0"
    current_validation = "Initialization"
    
    try:
        common.setup()
        
        # Generate unique test data to avoid conflicts
        base_email = common.generate_tenant_email()
        username = f"testuser_{base_email.split('@')[0]}"
        email = base_email
        password = "Test@1234"
        first_name = "John"
        last_name = "Doe"
        
        framework_logger.info(f"[{tcid}] Generated test data: username={username}, email={email}")
        
        # ── Step 1: Navigate to the application URL ──
        current_step = "Step 1"
        current_validation = "Application home page should be displayed"
        
        with PlaywrightManager() as page:
            home_page = HomePage(page)
            home_page.navigate_to_home_page()
            expect(home_page.home_page_container).to_be_visible(timeout=30000)
            
            stage_callback("step1_home_page", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 1: Navigated to application home page successfully")
            reporter.validate(True, f"[{tcid}] Step 1: Navigated to application home page successfully")
            
            # ── Step 2: Click on 'Register' button ──
            current_step = "Step 2"
            current_validation = "Registration page should be displayed"
            
            home_page.click_register_button()
            registration_page = RegistrationPage(page)
            expect(registration_page.registration_form).to_be_visible(timeout=30000)
            
            stage_callback("step2_registration_page", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 2: Registration page displayed successfully")
            reporter.validate(True, f"[{tcid}] Step 2: Registration page displayed successfully")
            
            # ── Step 3: Enter username in the 'Username' field ──
            current_step = "Step 3"
            current_validation = "Username should be entered successfully"
            
            registration_page.enter_username(username)
            expect(registration_page.username_input).to_have_value(username, timeout=10000)
            
            framework_logger.info(f"[{tcid}] Step 3: Username entered successfully")
            reporter.validate(True, f"[{tcid}] Step 3: Username entered successfully")
            
            # ── Step 4: Enter email in the 'Email' field ──
            current_step = "Step 4"
            current_validation = "Email should be entered successfully"
            
            registration_page.enter_email(email)
            expect(registration_page.email_input).to_have_value(email, timeout=10000)
            
            framework_logger.info(f"[{tcid}] Step 4: Email entered successfully")
            reporter.validate(True, f"[{tcid}] Step 4: Email entered successfully")
            
            # ── Step 5: Enter password in the 'Password' field ──
            current_step = "Step 5"
            current_validation = "Password should be entered successfully"
            
            registration_page.enter_password(password)
            expect(registration_page.password_input).to_have_value(password, timeout=10000)
            
            framework_logger.info(f"[{tcid}] Step 5: Password entered successfully")
            reporter.validate(True, f"[{tcid}] Step 5: Password entered successfully")
            
            # ── Step 6: Enter confirm password in the 'Confirm Password' field ──
            current_step = "Step 6"
            current_validation = "Confirm password should be entered successfully"
            
            registration_page.enter_confirm_password(password)
            expect(registration_page.confirm_password_input).to_have_value(password, timeout=10000)
            
            framework_logger.info(f"[{tcid}] Step 6: Confirm password entered successfully")
            reporter.validate(True, f"[{tcid}] Step 6: Confirm password entered successfully")
            
            # ── Step 7: Enter first name in the 'First Name' field ──
            current_step = "Step 7"
            current_validation = "First name should be entered successfully"
            
            registration_page.enter_first_name(first_name)
            expect(registration_page.first_name_input).to_have_value(first_name, timeout=10000)
            
            framework_logger.info(f"[{tcid}] Step 7: First name entered successfully")
            reporter.validate(True, f"[{tcid}] Step 7: First name entered successfully")
            
            # ── Step 8: Enter last name in the 'Last Name' field ──
            current_step = "Step 8"
            current_validation = "Last name should be entered successfully"
            
            registration_page.enter_last_name(last_name)
            expect(registration_page.last_name_input).to_have_value(last_name, timeout=10000)
            
            framework_logger.info(f"[{tcid}] Step 8: Last name entered successfully")
            reporter.validate(True, f"[{tcid}] Step 8: Last name entered successfully")
            
            # ── Step 9: Click on 'Submit' button ──
            current_step = "Step 9"
            current_validation = "Registration should be submitted successfully"
            
            registration_page.click_submit_button()
            page.wait_for_load_state("networkidle", timeout=30000)
            
            stage_callback("step9_form_submitted", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 9: Registration form submitted successfully")
            reporter.validate(True, f"[{tcid}] Step 9: Registration form submitted successfully")
            
            # ── Step 10: Verify success message ──
            current_step = "Step 10"
            current_validation = "Success message 'Registration successful' should be displayed"
            
            success_page = RegistrationSuccessPage(page)
            expect(success_page.success_message).to_be_visible(timeout=15000)
            expect(success_page.success_message).to_contain_text("Registration successful", timeout=10000)
            
            stage_callback("step10_success_message", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 10: Success message 'Registration successful' displayed")
            reporter.validate(True, f"[{tcid}] Step 10: Success message 'Registration successful' displayed")
            
    except Exception as e:
        framework_logger.error(
            f"[{tcid}] Test failed at {current_step} — {current_validation}: "
            f"{e}\n{traceback.format_exc()}"
        )
        reporter.validate(False, f"[{tcid}] FAIL at {current_step} — {current_validation}: {str(e)}")
        raise
