from selenium import webdriver

def test_on_grid(browser):
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )
    driver.get("http://localhost:5000")
    assert "Home" in driver.title
    driver.quit()

if __name__ == "__main__":
    # Test on Chrome
    test_on_grid('chrome')
    
    # Test on Firefox
    test_on_grid('firefox')