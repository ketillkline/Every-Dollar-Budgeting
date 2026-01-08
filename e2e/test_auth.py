from .conftest import page, test_user

local_url = "http://127.0.0.1:8000/"

def test_auth_page_loads(page, live_server):
    page.goto(local_url + "login/")
    assert page.title() != ""

def test_login_form_exists(page, live_server):
    page.goto(local_url + "login/")

    assert page.locator("input[name='username']").is_visible()
    assert page.locator("input[name='password']").is_visible()
    assert page.locator("button[type='submit']").is_visible()

def test_login_success(page, test_user, live_server):
    page.goto(local_url + "login/")

    page.fill("input[name='username']", "testuser")
    page.fill("input[name='password']", "testpassword")
    page.click("button[type='submit']")

    page.wait_for_url(local_url, timeout=5000)

    assert "login" not in page.url
