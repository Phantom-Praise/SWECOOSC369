# pytest -s test_get_started.py

import re 
from playwright.sync_api import sync_playwright, Page, expect

def test_get_started_link(): 
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://grabdocs.com")
        get_started = page.get_by_role("link", name="Get started", exact=True)
        get_started.click()

        page.screenshot(path="img/test_get_started_link.png")
        print("Screenshot taken and saved as test_get_started_link.png")

        browser.close()

test_get_started_link()