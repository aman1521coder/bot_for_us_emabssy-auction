import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Initialize WebDriver
driver = webdriver.Firefox()

# URL of the login page
login_url = 'https://online-auction.state.gov/en-US/Account/Login?ReturnUrl=%2Fen-US'

# Credentials
username = 'amanesu1521@gmail.com'
password = 'Aman1515@#'

# Initialize your bid
your_bid = 25000

# Open the browser and navigate to the login page
driver.get(login_url)

# Locate username and password fields, and submit button
username_field = driver.find_element(By.ID, 'Email')
password_field = driver.find_element(By.ID, 'Password')
submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

# Enter credentials and submit login form
username_field.send_keys(username)
password_field.send_keys(password)
submit_button.click()

# Wait for login to complete
WebDriverWait(driver, 10).until(EC.url_changes(login_url))

# URL after login
url_after_login = 'https://online-auction.state.gov/en-US/Auction/Lot/88fd20e5-58d5-4461-b0ea-166d40fa54a0?auctionId=5d8c5e3a-9d56-4cf9-8667-cae7369b9232'

# Open the browser and navigate to the URL after login
driver.get(url_after_login)

# Keep track of the last observed price
last_price = 0

# Main loop for monitoring and bidding process
while True:
    try:
        # Locate the current price element
        current_price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'lot_88fd20e5-58d5-4461-b0ea-166d40fa54a0_highest_bid'))
        )

        # Get the current price
        current_price_text = current_price_element.text

        # Remove commas and convert to integer for comparison
        current_price = int(current_price_text.replace(',', ''))

        # Check if the current price is different from the last observed price
        if current_price != last_price:
            # Update the last observed price
            last_price = current_price

            # Click the submit button
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'submitbutton'))
            )
            submit_button.click()

            # Wait for the modal to appear and locate the "Confirm" button
            confirm_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Confirm")]'))
            )
            confirm_button.click()

    except NoSuchElementException as e:
        print(f"Error locating element: {e}")
    except TimeoutException as e:
        print(f"Timeout waiting for element: {e}. Retrying...")

    # Sleep for a short duration before checking again
    time.sleep(0.1)
