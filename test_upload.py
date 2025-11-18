# pytest -s test_upload.py

# PWDEBUG=1 pytest -s test_upload.py

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

        # print("\n\n===== PAGE CONTENT =====\n\n")
        # print(page.content())
        # print("\n\n=========================\n\n")a

        page.set_input_files("input[type='file']", "/Users/praiseben/SWECOOSC369/praisebenunofficialTranscript.pdf")
        page.set_input_files("input[type='file']", "/Users/praiseben/SWECOOSC369/mummy.pdf")
        page.wait_for_timeout(10000)
        # page.screenshot(path="img/upload_dialog.png")

        # page.get_by_role("button", name="Ask").click()
        # page.screenshot(path="img/ask_chatbot_opened.png")

        page.get_by_placeholder("Ask anything or send a message ...").fill(
            "What is this document about?"
        )
        page.locator("button[title='Send message']").click()
        # page.screenshot(path="img/ask_sent.png")

        page.wait_for_timeout(10000)
        page.wait_for_selector("text=GrabDocs may not give perfect answers", timeout=20000)
        # page.screenshot(path="img/response_received.png")

        page.get_by_role("button", name="Reach").click()
        page.wait_for_timeout(2000)
        # page.screenshot(path="img/click_reach.png")

        page.get_by_role("button", name="Calendar").click()
        page.wait_for_timeout(2000)
        # page.screenshot(path="img/click_calendar.png")

        page.get_by_role("button", name="Links").click()
        page.wait_for_timeout(2000)
        # page.screenshot(path="img/click_links.png")

        page.get_by_role("button", name="Forms").click()
        page.wait_for_timeout(2000)
        # page.screenshot(path="img/click_forms.png")

        page.get_by_role("button", name="Workspace").click()
        page.wait_for_timeout(2000)
        # page.screenshot(path="img/click_workspace.png")

        page.get_by_role("link", name="Home").click()
        page.wait_for_timeout(2000)
        # page.screenshot(path="img/return_home.png")

        page.get_by_role("button", name="Ask").click()
        # page.screenshot(path="img/ask_chatbot.png")

        # browser.close()

