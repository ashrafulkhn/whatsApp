import time
import pandas as pd
import pyautogui
import pyperclip
import webbrowser
import os
import random

# ========== Define Messages ==========
love_messages = [
    "I wasn’t trying to prove I know better. I just wanted to know because I care. Can’t you see that? 😔",
    "You always think I ignore your words, but I hang on to every single one you say. 🥺",
    "Tell me what I did wrong, baby. Not through silence — through your voice. 💔",
    "I get curious about your dad’s health because I want to be involved. Not because I don’t trust you.",
    "Maybe I push too much sometimes, but it’s only because I love too much. ❤️",
    "Silence is too loud when it’s from you. Talk to me. Fight with me. Just don’t vanish. 😢",
    "I hate fighting with you. I hate sleeping without your last message. 💬💤",
    "Let’s be real — we’re both stubborn. But I’d rather be wrong than lose you. 🤝",
    "Tell me your doctor, your worries, your thoughts. I want to carry them too, not question them. 🫂",
    "Did I hurt your pride, or your heart? Because I never meant to touch either. 😞",
    "I miss our weird late-night chats more than I miss peace. Come back to me. 💤❤️",
    "You know what's worse than a fight? Pretending I'm fine when I'm not. 🧍‍♂️",
    "I may ask too many questions, but that’s because you mean too much to me. 😓",
    "I want to kiss that anger off your face and replace it with smiles. 😘",
    "You're angry, and I’m still in love. We can fix this. Let me try. 🔧💘",
    "You don't have to forgive me now, but don’t block me out of your world. 🚪",
    "Can we argue while holding hands next time? I miss your fingers between mine. 🤝💞",
    "Punish me, but don’t ignore me. I’m too addicted to you to survive this cold war. ❄️🔥",
    "Remember that night we laughed for hours? I want that again. Not this. 🥹",
    "Let’s fight, cry, shout — but stay. Don't go silent. 💢💔",
    "If you ever doubt your worth to me — just read this: You. Mean. Everything. 💯",
    "You’ve taken over my mind, my heart… and even my sleep schedule. 😵‍💫💗",
    "I love your voice, even when you're scolding me. Just say something. Anything. 📱",
    "Your anger turns me on more than I’d like to admit. 😳🔥",
    "I want to touch you. Not just physically — I want to reach the angry corner of your soul too. 🥰",
    "Your silence is sharp, but I still bleed love for you. ❤️🩸",
    "I’m yours — ego, flaws, impatience, all of it. Take it or teach me. 🙇‍♂️",
    "You looked so hot when you got mad. Just saying. 😍💢",
    "If loving you means messing up and fixing it again and again — I’m in. Forever. 🔁❤️",
    "This pain in my chest isn’t from the fight. It’s from the distance. 😔",
    "You said I act like you don’t know anything. Maybe I do it unknowingly. But I never meant to. 🤦‍♂️",
    "Tell me what you felt. Tell me how I hurt you. Don’t hide it — I want to know. 🫂💬",
    "I didn’t need to know the doctor’s name — I needed to feel involved. That’s it. 😩",
    "I know I’m not perfect, but I’m trying. For you. For us. 🛠️💕",
    "One minute you’re yelling at me. Next minute I want to kiss you breathless. That’s how crazy you make me. 😘💥",
    "Touch my soul, not just my phone. Talk to me, love. 😶‍🌫️",
    "Your anger is sexy. But your love is even hotter. Bring that back. 🥵❤️",
    "Fights are like foreplay for us. Let’s finish this one properly. 😈😉",
    "Let’s stop this cold war and heat things up a little? 😏🔥",
    "Want to punish me? I’m all yours. But don't lock me out of your heart. 🔐❤️",
    "You make me feel like a schoolboy again — dumb, eager, and hopelessly in love. 🥲",
    "I know you can win any argument. But don’t win by walking away. 🛑",
    "Anger suits you. But love fits you better. 🧥💘",
    "You’re angry. I’m horny. Let’s meet halfway and just talk. 😅",
    "Even when I’m pissed off, you’re still the hottest girl in my life. 💋",
    "Babe, let’s be dramatic. Let’s cry. Let’s kiss. Let’s do it all. Just don’t ignore me. 🎭💔❤️",
    "Don’t make me beg, but also… here I am. Begging. Come back. 🧎‍♂️",
    "You think I don’t listen. But your words echo in my head all night. 🔁🧠",
    "I know I asked too much. I should’ve just held your hand and stayed quiet. 🫣🤝",
    "I’m not asking for your reply. I’m praying for it. 🙏📱",
    "Can we have that post-fight cuddle already? I’m emotionally naked right now. 🫂🩶"
]

def send_whatsapp_message_with_image(phone_number, messages, image_path, delay_between=5):
    for message in messages:
        pyperclip.copy(message)
        # print(f"Sending message: {message} to {phone_number}")
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
            # print("Attachment icon not found on the screen.")
            pass


    else:
        # print(f"Image not found: {image_path}")
        pass

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

        for _ in range(100):
            messages = [random.choice(love_messages)]

            image_path = os.path.join("project", "image", "Chat-GPT-Marketing.png")

            send_whatsapp_message_with_image(phone_number, messages, image_path, delay_between=4)
            print(f"{_}: Messages and image sent to {contacts['Name'][choice]} ({phone_number})")
            time.sleep(random.randint(2, 5))
        

if __name__ == "__main__":
    main()
