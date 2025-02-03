import pytest
from playwright.sync_api import Playwright, sync_playwright


@pytest.mark.sanity
def test_amazon(playwright: Playwright):
    # Launch browser in non-headless mode
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #Navigate to Amazon India
    page.goto("https://www.amazon.in/")

    # Click on Sign-in button
    #page.get_by_text("Sign in", exact=True).click()
    page.click("text=Hello, sign in")  # Adjust if needed

    # Enter email
    page.fill("input[type='email']", "bhaveshjadhav2523@gmail.com")
    page.click("input#continue")

    # Enter password
    page.fill("input[type='password']", "Bhavesh@9898")
    page.click("input#signInSubmit")

    #If redirected to OTP page, wait for manual entry
    if "mfa" in page.url:
        print("Amazon redirected to OTP page. Please enter OTP manually.")
        page.wait_for_timeout(60000)  # 60 seconds for manual entry
        page.click("input#signInSubmit")

    #Search for "iPhone"
    page.fill("input[name='field-keywords']", "iPhone")
    page.wait_for_timeout(3000)  # Waits for 3 seconds
    import pdb
    pdb.set_trace()


    ###page.press("input[name='field-keywords']", "Enter")
    elements = page.query_selector_all("div.two-pane-results-container")
    texts = [element.inner_text() for element in elements]
    split_list = [item.split('\n') for item in texts]
    print(split_list)
    split_list[0][3]
    page.click(split_list[0][3])
    page.wait_for_timeout(3000)  # Waits for 3 seconds




    #Select the 4th item from the search results
    page.wait_for_selector("div.s-main-slot div[data-component-type='s-search-result']", timeout=10000)
    search_results = page.query_selector_all("div.s-main-slot div[data-component-type='s-search-result']")

    #if len(search_results) >= 4:
        search_results[3].click()  # 4th item (index starts from 0)
    else:
        pytest.fail("Less than 4 search results found")

    #Add the selected item to the cart
    page.wait_for_selector("input#add-to-cart-button", timeout=10000)
    page.click("input#add-to-cart-button")

    #Go to Cart
    page.click("#nav-cart")

    #Log out from Amazon
    page.click("#nav-link-accountList")  # Open account menu
    page.wait_for_selector("text=Sign Out", timeout=10000)
    page.click("text=Sign Out")

    #Close browser
    context.close()
    browser.close()
