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

        # page.get_by_placeholder("Username").fill("test101")
        # page.get_by_placeholder("Password").fill("123456789")

        page.get_by_placeholder("Username").fill("izuchukwu")
        page.get_by_placeholder("Password").fill("password123")

        page.get_by_role("button", name="Sign In").click()
        page.wait_for_timeout(5000)


        page.locator("button:has(svg[viewBox='0 0 20 20'])").first.click()
        page.wait_for_timeout(5000)

        page.get_by_text("Download").click()
        page.wait_for_timeout(10000)

        page.get_by_text("Delete").click()
        page.wait_for_timeout(10000)

        # page.get_by_placeholder("Enter 6-digit code").fill("335577")
        # page.get_by_role("button", name="Verify Code").click()
        # page.wait_for_timeout(10000)

        page.set_input_files("input[type='file']", "/Users/praiseben/SWECOOSC369/mummy.pdf")
        page.wait_for_timeout(25000)


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


        page.locator("button:has(span:has-text('Ask'))").click()
        page.wait_for_timeout(5000)

        with open("chat_ask_chatbot.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        
        page.locator("select").select_option("improvement")
        page.wait_for_timeout(2000)

        page.get_by_placeholder("Brief summary of your feedback").fill(
            "Enhance File Upload Feedback Mechanism"
        )

        page.get_by_placeholder("Please provide detailed feedback...").fill(
            "Limited file type support for uploads. When users attempt to upload unsupported "
            "file types, they receive a generic error message that does not specify which formats "
            "are acceptable. This can lead to confusion and frustration as users may not understand "
            "why their upload failed or what types of files they can successfully upload."
        )

        page.get_by_role("button", name="Submit Feedback", exact=True).click()

        page.wait_for_timeout(10000)

        page.get_by_title("Show History").click()

        page.wait_for_timeout(5000)

        page.locator("button.ml-2").first.click()
        
        page.wait_for_timeout(10000)

