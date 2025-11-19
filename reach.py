# pytest -s reach.py

# PWDEBUG=1 pytest -s reach.py

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

        page.get_by_role("button", name="Reach").click()

        with open("reach_dom.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        

        page.get_by_role("button", name="Create Meeting").first.click()
        page.wait_for_timeout(5000)
        page.get_by_placeholder("Enter meeting name").fill("Praise Test 29 Again ooo")
        page.get_by_role("button", name="Create Meeting").nth(1).click()
        page.wait_for_timeout(5000)


        page.get_by_role("button", name="Schedule Meeting").click()
        with open("reach_schedule_meeting_dom.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        page.get_by_placeholder("Enter meeting name").fill("Praise Test Again 9.0ooo")
        from datetime import date, timedelta
        next_week = (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")

        page.locator("input[type='date']").fill(next_week)

        page.locator("input[type='time']").fill("10:30")

        page.locator("select").select_option("180")


        page.get_by_placeholder("Enter email address").fill("praiseben13@gmail.com")

        page.wait_for_timeout(2000)
        page.get_by_role("button", name="Add").nth(1).click()
        page.wait_for_timeout(2000)

        page.get_by_role("button", name="Schedule Meeting").nth(1).click()

        page.wait_for_timeout(10000)


        