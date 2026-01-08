from .conftest import page, test_user

def test_auth_page_loads(page, live_server):
    page.goto(live_server.url + "/login/")
    assert page.title() != ""

def test_login_form_exists(page, live_server):
    page.goto(live_server.url + "/login/")

    assert page.locator("input[name='username']").is_visible()
    assert page.locator("input[name='password']").is_visible()
    assert page.locator("button[type='submit']").is_visible()

def test_login_success(page, test_user, live_server):
    page.goto(live_server.url + "/login/")

    page.fill("input[name='username']", "testuser")
    page.fill("input[name='password']", "testpassword")
    page.click("button[type='submit']")

    page.wait_for_url(live_server.url + "/")

    assert page.url == live_server.url + "/"
