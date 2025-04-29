import time
import pandas as pd
import pyautogui
import pyperclip
import webbrowser
import os

def send_whatsapp_message_with_image(phone_number, messages, image_path, delay_between=5):
    for message in messages:
        pyperclip.copy(message)
        print(f"Sending message: {message} to {phone_number}")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")
        time.sleep(delay_between)

    # Send the image
    if os.path.exists(image_path):
        print(f"Sending image: {image_path} to {phone_number}")
        # Locate and click the attachment icon
        attachment_icon = pyautogui.locateOnScreen('attachment_icon.png', confidence=0.8)
        if attachment_icon:
            pyautogui.click(attachment_icon)
            time.sleep(1)
            pyautogui.write(image_path)
            pyautogui.press("enter")
            time.sleep(delay_between)
        else:
            print("Attachment icon not found on the screen.")
    else:
        print(f"Image not found: {image_path}")

def main():
    contacts = pd.read_excel("contacts.xlsx")

    print("Available contacts:")
    for idx, name in enumerate(contacts['Name']):
        print(f"{idx + 1}. {name}")

    # Open WhatsApp Web once
    webbrowser.open("https://web.whatsapp.com")
    time.sleep(15)  # Wait for WhatsApp Web to load

    for idx in range(len(contacts)):
        print(f"{idx + 1}. {contacts['Name'][idx]}")
        choice = idx  # Simulate user input for testing
        time.sleep(1)
        print(f"Selected contact: {contacts['Name'][choice]}")

        if choice < 0 or choice >= len(contacts):
            print("Invalid choice.")
            return

        phone_number = str(contacts.loc[choice, 'Phone'])

        # Update the phone number in the current tab
        pyautogui.hotkey('ctrl', 'l')  # Focus on the address bar
        pyperclip.copy(f"https://web.whatsapp.com/send?phone={phone_number}")
        pyautogui.hotkey('ctrl', 'v')  # Paste the new URL
        pyautogui.press("enter")
        time.sleep(10)  # Wait for the chat to load

        messages = [
            "I am trying to develop an automated whatsapp messenger using Python. Do not panic, you are not being hacked and you are one of my \
            closest friends. I am just trying to learn how to use Python and I am using you as a test subject.",
        ]

        image_path = os.path.join("project", "image", "Chat-GPT-Marketing.png")

        send_whatsapp_message_with_image(phone_number, messages, image_path, delay_between=4)
        print(f"Messages and image sent to {contacts['Name'][choice]} ({phone_number})")

if __name__ == "__main__":
    main()
