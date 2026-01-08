from .imports import page, local_url

def test_auth_page_loads(page):
    page.goto(local_url + "login/")
    assert page.title() != ""

def test_login_form_exists(page):
    page.goto(local_url + "login/")

    assert page.locator("input[name='username']").is_visible()
    assert page.locator("input[name='password']").is_visible()
    assert page.locator("button[type='submit']").is_visible()


