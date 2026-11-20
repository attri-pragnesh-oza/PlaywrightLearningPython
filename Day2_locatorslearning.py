from playwright.sync_api import sync_playwright
 
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.wait_for_timeout(5000)
 
    username = page.locator("#user-name")
    password = page.locator("#password")
    login_button = page.get_by_role("button", name="Login")
 
    print("Username visible:", username.is_visible())
    print("Password visible:", password.is_visible())
    print("Login visible:", login_button.is_visible())
 
    browser.close()