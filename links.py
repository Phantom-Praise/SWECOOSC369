# pytest -s links.py

# PWDEBUG=1 pytest -s links.py

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

        with open("links_dom.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        
        page.get_by_role("button", name="New Link").click()

        page.get_by_placeholder("Enter link name").fill("Praise Test")
        with open("links_dom_create_upload_link2.html", "w", encoding="utf-8") as f:
            f.write(page.content())

        max_size_input = page.locator("label:has-text('Max File Size (MB)') + input")
        max_size_input.fill("5")

        page.get_by_role("button", name="Create Link").click()



        page.wait_for_timeout(4000)

        
        # link name enter Praise test 
        # Max file size edit 5 
        # Click Create link
