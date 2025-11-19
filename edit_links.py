# pytest -s edit_links.py

# PWDEBUG=1 pytest -s edit_links.py

import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
load_dotenv()

def test_upload(): 

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://app.grabdocs.com/login")

        # page.get_by_placeholder("Username").fill("test101")
        # page.get_by_placeholder("Password").fill("123456789")

        # page.get_by_role("button", name="Sign In").click()
        # page.wait_for_timeout(3000)

        # page.get_by_placeholder("Enter 6-digit code").fill("335577")
        # page.get_by_role("button", name="Verify Code").click()
        # page.wait_for_timeout(10000)

        page.get_by_placeholder("Username").fill("izuchukwu")
        page.get_by_placeholder("Password").fill("password123")
        page.get_by_role("button", name="Sign In").click()
        page.wait_for_timeout(3000)

        page.get_by_role("button", name="Links").click()
        page.get_by_text("Quick Links").wait_for()

        with open("edit_links_dom.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        
        page.get_by_role("button", name="Options").first.click()
        # page.locator("tbody tr").nth(0).locator("button[aria-label='Options']").click()

        # page.get_by_role("menuitem", name="Delete").click()

        page.get_by_role("button", name="Delete").click()
        page.screenshot(path="delete_link.png")
        page.wait_for_timeout(5000)
        