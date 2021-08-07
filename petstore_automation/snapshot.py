def take_screenshot(driver, animal):
    driver.save_screenshot(f"snapshots/{animal}_snapshot.png")