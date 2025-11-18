# pytest -s

import re 
from playwright.sync_api import sync_playwright, Page, expect

def test_has_title(): 
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://grabdocs.com")

        print(f"The Page Title Is {page.title()}")
        expect(page).to_have_title(re.compile("GrabDocs"))

        page.screenshot(path="img/test_has_title.png")
        print("Screenshot taken and saved as test_has_title.png")

        browser.close()