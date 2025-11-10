# pytest -s test_login.py

import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
load_dotenv()

def test_login_page(): 

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://app.grabdocs.com/login")

        page.get_by_placeholder("Username").fill("test101")
        page.get_by_placeholder("Password").fill("123456789")

        page.screenshot(path="img/test_login_page_input_credentials.png")
        print("Screenshot taken and saved as test_login_page_input_credentials.png")

        page.get_by_role("button", name="Sign In").click()
        page.wait_for_timeout(3000)

        page.screenshot(path="img/test_login_page_sign_in_click.png")
        print("Screenshot taken and saved as test_login_page_sign_in_click.png")

        page.get_by_placeholder("Enter 6-digit code").fill("335577")
        page.screenshot(path="img/login_page_otp_code.png")
        print("Screenshot taken and saved as login_page_otp_code.png")

        page.get_by_role("button", name="Verify Code").click()
        page.wait_for_timeout(10000)
        page.screenshot(path="img/login_page_otp_code_after.png")
        print("Screenshot taken and saved as login_page_otp_code_after.png")

        assert "upload" in page.url.lower()
        # browser.close()

