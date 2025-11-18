# pytest -s chat.py

# PWDEBUG=1 pytest -s chat.py

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

        # page.set_input_files("input[type='file']", "/Users/praiseben/SWECOOSC369/praisebenunofficialTranscript.pdf")
        page.set_input_files("input[type='file']", "/Users/praiseben/SWECOOSC369/mummy.pdf")
        page.wait_for_timeout(15000)


        page.get_by_placeholder("Ask anything or send a message ...").fill(
            "@mummy."
        )
        page.wait_for_timeout(5000)

        page.wait_for_selector("div.absolute.bottom-full")
        page.locator("button:has-text('mummy.pdf')").first.click()
        page.wait_for_timeout(5000)

        page.get_by_placeholder("Ask anything or send a message ...").fill(
            "Please summarize the key points from the uploaded document."
        )

        page.locator("button[title='Send message']").click()
        page.wait_for_timeout(50000)

