# WhatsApp Automation

This project automates sending personalized messages and images to contacts via WhatsApp Web using Python.

## Features
- Sends custom messages to contacts listed in an Excel file (`contacts.xlsx`).
- Can send images from the `image/` directory along with messages.
- Uses browser automation (Selenium or pyautogui) to interact with WhatsApp Web.

## Prerequisites
- Python 3.7+
- Google Chrome or Microsoft Edge browser
- Required Python packages:
  - pandas
  - pyautogui
  - pyperclip
  - selenium (if using the Selenium version)

## Setup
1. **Clone the repository** and navigate to the project directory.
2. **Install dependencies:**
   ```powershell
   pip install pandas pyautogui pyperclip selenium
   ```
3. **Prepare your contacts:**
   - Add your contacts to `project/contacts.xlsx` with columns: `Name` and `Phone` (phone numbers in international format, e.g., 919876543210).
4. **Add images:**
   - Place images you want to send in the `project/image/` directory.

## Running the Script

### Using pyautogui (default)
1. Open your browser and maximize the window.
2. Run the script:
   ```powershell
   python project/app.py
   ```
3. The script will open WhatsApp Web. Scan the QR code if prompted.
4. The script will automatically send messages and images to each contact.

### Using Selenium (recommended for reliability)
1. Download the appropriate WebDriver for your browser:
   - **Chrome:** [ChromeDriver](https://chromedriver.chromium.org/downloads)
   - **Edge:** [Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
2. Update the script to use the correct WebDriver path and browser.
3. Run the script as above.

## Notes
- Make sure WhatsApp Web remains in focus and is not interrupted during automation.
- For pyautogui, you may need to provide a screenshot of the attachment icon as `attachment_icon.png` for image sending to work.
- Use responsibly and respect WhatsApp's terms of service.

## License
See [LICENSE](LICENSE) for details.
