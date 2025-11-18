# pytest -s forms.py

# PWDEBUG=1 pytest -s forms.py

import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
load_dotenv()

def test_upload(): 

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://app.grabdocs.com/login")

        page.get_by_placeholder("Username").fill("test101")
        page.get_by_placeholder("Password").fill("123456789")

        page.get_by_role("button", name="Sign In").click()
        page.wait_for_timeout(3000)

        page.get_by_placeholder("Enter 6-digit code").fill("335577")
        page.get_by_role("button", name="Verify Code").click()
        page.wait_for_timeout(10000)

        page.get_by_role("button", name="Forms").click()
        page.wait_for_timeout(5000)

        with open("forms_dom.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        
        page.get_by_text("RSVP Form", exact=True).click()
        page.wait_for_timeout(5000)
        # with open("forms_rsvp_dom.html", "w", encoding="utf-8") as f:
        #     f.write(page.content())

        
        page.get_by_placeholder("Enter your full name").fill("Praise Ben")
        page.get_by_placeholder("your.email@example.com").fill("praiseben13@gmail.com")
        page.locator("select").nth(0).select_option("No, I cannot attend")
        page.locator("select").nth(1).select_option("1 guest")
        page.get_by_role("button", name="Save Form").click()
        # page.locator('button[title="Save Form"]').click()





        page.wait_for_timeout(5000)






        

        """
        i wanna click on the RSVP Form
        
        """