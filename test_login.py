from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_valid_login(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user","wrongpassword")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_wrong_password(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user","wrong123")
    expect(login.error).to_contain_text("do not match")

def test_locked_out_user(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("locked_out_user","secret_sauce")
    expect(login.error).to_contain_text("locked out")



