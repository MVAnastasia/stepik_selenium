import time



def test_guest_should_see_login_link(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket")