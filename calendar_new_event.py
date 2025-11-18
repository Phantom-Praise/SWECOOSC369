# pytest -s main.py

# PWDEBUG=1 pytest -s main.py

import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
load_dotenv()

def create_calendar_event(): 

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://app.grabdocs.com/login")
        page.get_by_placeholder("Username").fill("test101")
        page.get_by_placeholder("Password").fill("123456789")
        page.get_by_role("button", name="Sign In").click()
        page.wait_for_timeout(3000)
        page.get_by_placeholder("Enter 6-digit code").fill("335577")
        page.get_by_role("button", name="Verify Code").click()
        page.wait_for_timeout(5000)

        page.get_by_role("button", name="Calendar").click()
        page.get_by_text("November").wait_for()

        with context.expect_page() as page_info:
            page.get_by_role("button", name="New Event").click()

        event_page = page_info.value  
        event_page.wait_for_load_state()
    

        html = event_page.content()
        with open("create_event_dom2.html", "w", encoding="utf-8") as f:
            f.write(html)
        # FILL EVENT TITLE
        event_page.get_by_placeholder("Team Meeting, Client Call, etc.").fill(
            "SWE Group 1 Team Meeting"
        )

        # DESCRIPTION
        event_page.get_by_placeholder("Add details about the event...").fill(
            "Discuss project requirements and assign tasks."
        )

        # START DATE
        event_page.locator("input[type=date]").nth(0).fill("2025-11-24")

        # START TIME
        event_page.locator("input[type=time]").nth(0).fill("19:30")  # 07:30 PM

        # END DATE
        event_page.locator("input[type=date]").nth(1).fill("2025-11-24")

        # END TIME
        event_page.locator("input[type=time]").nth(1).fill("20:30")  # 08:30 PM

        # HOST REACH MEETING checkbox
        event_page.locator("label:has-text('Host Reach Meeting') input").check()

        # LOCATION
        event_page.get_by_placeholder("Conference Room A").fill("BSU Computer Science Lab")

        # PARTICIPANT
        event_page.get_by_placeholder("email@example.com").fill("praiseben13@gmail.com")
        # Click + button
        # event_page.locator("div.flex.space-x-1 button.bg-blue-600").click()
        event_page.locator("div.flex.space-x-1 > button[type=button]").click()


        # Reminders (click all)
        reminder_section = event_page.locator("div.flex.flex-wrap.gap-1")

        for r in ["5 min before", "30 min before", "1 hr before", "2 hr before"]:
            reminder_section.get_by_role("button", name=r, exact=True).click()

        # Toggle Recurring Event
        event_page.locator("h2:has-text('Recurring Event') ~ label div.w-11").click()
        event_page.wait_for_timeout(500)
        page.screenshot(path="img/create_calendar_event.png")
        event_page.pause()


        html_after = event_page.content()
        with open("recurring_dom.html", "w", encoding="utf-8") as f:
            f.write(html_after)
        
        frequency = event_page.locator("label:has-text('Frequency') + select")
        frequency.select_option("DAILY")
        event_page.wait_for_timeout(200)
        frequency.select_option("WEEKLY")
        event_page.wait_for_timeout(200)

        repeat_section = event_page.locator("label:has-text('Repeat on')").locator("..")

        # Click specific weekdays
        for day in ["Mon", "Wed", "Sun"]:
            repeat_section.get_by_role("button", name=day, exact=True).click()

        event_page.locator("label:has-text('Number of Occurrences') + input").fill("5")

        page.screenshot(path="img/create_calendar_event5.png")
        page.wait_for_timeout(300)

        # SUBMIT
        event_page.get_by_role("button", name="Create Event").click()

        page.wait_for_timeout(3000)