# pytest -s delete_calendar_event.py

# PWDEBUG=1 pytest -s delete_calendar_event.py


from playwright.sync_api import sync_playwright

def test_get_past_event_dom():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login
        page.goto("https://app.grabdocs.com/login")
        page.get_by_placeholder("Username").fill("test101")
        page.get_by_placeholder("Password").fill("123456789")
        page.get_by_role("button", name="Sign In").click()
        page.wait_for_timeout(3000)

        # page.get_by_placeholder("Username").fill("izuchukwu")
        # page.get_by_placeholder("Password").fill("password123")
        # page.get_by_role("button", name="Sign In").click()
        # page.wait_for_timeout(3000)

        page.get_by_placeholder("Enter 6-digit code").fill("335577")
        page.get_by_role("button", name="Verify Code").click()
        page.wait_for_timeout(5000)

        # Go to Calendar
        page.get_by_role("button", name="Calendar").click()
        page.wait_for_timeout(3000)

        # Click "Past Events"
        page.get_by_role("button", name="Past Events").click()
        page.wait_for_timeout(3000)

        # Click the first past event
        page.locator("div.cursor-pointer").first.click()
        page.wait_for_timeout(3000)

        delete_btn = page.locator("button.border-red-300")
        delete_btn.click()
        page.wait_for_timeout(3000)
        
        page.get_by_role("button", name="Delete Event").click()


        page.wait_for_timeout(3000)

        page.pause()


