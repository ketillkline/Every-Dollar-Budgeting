from .conftest import page, test_user, url

def login(page):
    page.goto(url + "login/")
    page.fill("input[name='username']", "testuser")
    page.fill("input[name='password']", "testpassword")
    page.click("button[type='submit']")

def test_clear_all(page):

    login(page)

    clear_button = page.locator("button[value='clear_all_incomes']")

    page.wait_for_load_state("networkidle")
    assert page.url == url

def test_income_submit(page):
    login(page)

    page.fill("input[name='paycheck']", "700")
    page.fill("input[name='start_date']", "2030-01-12")
    page.fill("input[name='end_date']", "2030-01-26")

    page.click("button[value='add_income']")

    assert page.url == url

def test_add_bill(page):
    login(page)

    page.click()

    page.fill()
    page.fill()
    page.fill()

    page.click()

def test_cancel(page):
    login(page)
