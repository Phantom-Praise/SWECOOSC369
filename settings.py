# pytest -s settings.py

# PWDEBUG=1 pytest -s settings.py

import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
load_dotenv()

def test_upload(): 

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://app.grabdocs.com/login")

        page.get_by_placeholder("Username").fill("test202")
        page.get_by_placeholder("Password").fill("123abc@#%")

        page.get_by_role("button", name="Sign In").click()
        page.wait_for_timeout(3000)

        page.get_by_placeholder("Enter 6-digit code").fill("335577")
        page.get_by_role("button", name="Verify Code").click()
        page.wait_for_timeout(10000)

        # page.get_by_placeholder("Username").fill("izuchukwu")
        # page.get_by_placeholder("Password").fill("password123")
        # page.get_by_role("button", name="Sign In").click()
        # page.wait_for_timeout(5000)

        with open("settings_dom.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        
        page.locator("button.rounded-full.bg-blue-600").click()
        page.wait_for_timeout(5000)
        
        page.get_by_role("link", name="Settings").click()
        page.wait_for_timeout(5000)
        
        page.get_by_label("Phone Number").fill("12345678910")
        page.wait_for_timeout(1500)

        page.get_by_role("button", name="Display").click()

        page.select_option("select", "dark")
        page.wait_for_timeout(1000)

        page.get_by_role("button", name="Usage").click()
        page.wait_for_timeout(5000)


        page.get_by_role("button", name="Refresh").click()
        page.wait_for_timeout(5000)
        
        page.get_by_role("button", name="Preferences").click()
        with open("settings_preferences_dom.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        page.wait_for_timeout(1000)

        chat_card = page.locator(
            "div",
            has=page.locator("h3", has_text="Chat email notifications")
        )
        chat_notification_toggle = chat_card.locator("button").first
        chat_notification_toggle.click()
        page.wait_for_timeout(500)



        email_frequency_select = page.locator(
            "label",
            has_text="Email frequency"
        ).locator("..").locator("select")

        email_frequency_select.select_option("15min_digest")
        page.wait_for_timeout(500)



        skip_email_input = page.locator(
            "label",
            has_text="Skip emails if active in the last"
        ).locator("..").locator("input[type='number']")

        skip_email_input.fill("4")
        page.wait_for_timeout(500)

        page.wait_for_timeout(5000)


        