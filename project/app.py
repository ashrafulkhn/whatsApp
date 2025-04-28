from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Edge WebDriver without any options
driver = webdriver.Edge('msedgedriver.exe')

# Open WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code and log in
wait = WebDriverWait(driver, 120)  # Extend the timeout to 120 seconds
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]')))

# Find the chat input field and enter the recipient's name
search_box = driver.find_element(By.XPATH, '//div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]')
search_box.send_keys("Ashraful")
wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(@title,"Ashraful")]')))
search_box.send_keys(Keys.ENTER)

# Wait for the chat to load
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="_3u328 copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]')))

# Send the message repeatedly
for i in range(10):
    message_box = driver.find_element(By.XPATH, '//div[@class="_3u328 copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]')
    message_box.send_keys("Your Message")
    message_box.send_keys(Keys.ENTER)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//div[@class="_3XJ_-"]//span[contains(@class,"_3-8er")]'), "Your Message"))
    # Wait for 1 minute before sending the next message
    wait.until(EC.invisibility_of_element_located((By.XPATH, '//span[contains(@title,"typing...")]')))

# Close the browser
driver.quit()
