# Telegram Bot with Python

**Introduction**

This Python code creates a Telegram bot that offers various functionalities:

- **Number Guessing Game:** Play a classic guessing game with the bot.
- **Age Calculation:** Calculate your age based on your provided birthday in the Jalali (Shamsi) calendar format.
- **Text-to-Speech:** Convert your entered text into an audio file and send it to you. (Note: Language support is currently limited to English.)
- **Maximum Number:** Find the largest number among a comma-separated list of numbers you provide.
- **Index of Maximum:** Find the index of the largest number within a comma-separated list of numbers you provide.
- **QR Code Generation:** Generate a QR code from your entered text string.

**Requirements**

- Python 3
- Necessary libraries:
    - `telebot`: Install using `pip install pyTelegramBotAPI`
    - `qrcode`: Install using `pip install qrcode`
    - `gtts`: Install using `pip install gTTS`
    - `persiantools`: Install using `pip install persiantools` (for Jalali date calculations)

**Instructions**

1. **Obtain Telegram Bot Token:**
   - Create a Telegram bot using BotFather ([BotFather ON Telegram telegram.org]).
   - Follow the instructions to generate a unique token for your bot.

2. **Replace Placeholder Token:**
   - Open the Python script (`*.py`) in a text editor.
   - Replace `YOUR_BOT_TOKEN` with your actual bot token in the line:

   ```python
   bot = telebot.TeleBot("YOUR_BOT_TOKEN", parse_mode=None)
   ```

3. **(Optional) Using a VPN in Iran:**
   - If you're located in Iran, you may need a VPN to connect to Telegram's servers.

4. **Run the Script:**
   - Open a terminal or command prompt and navigate to the directory containing the script.
   - Execute the script using `python script_name.py`.

**Using the Bot**

Once the script is running, open Telegram and search for your bot's username. Send commands to the bot to initiate different functionalities:

- `/game`: Start the number guessing game.
- `/restart`: Restart the guessing game (within the game itself).
- `/age`: Enter your birthday in Jalali (Shamsi) date format (YYYY/MM/DD) to calculate your age.
- `/voice`: Enter text to convert to an audio file (currently supports English only).
- `/max`: Enter a comma-separated list of numbers to find the largest.
- `/argmax`: Enter a comma-separated list of numbers to find the index of the largest.
- `/qrcode`: Enter text to generate a QR code.
- `/help`: Display a list of available commands and brief descriptions.

**Additional Notes**

- For the `/age` command, ensure you enter your birthday in the correct Jalali (Shamsi) calendar format (e.g., 1399/06/14).
- The `/voice` command currently supports text-to-speech conversion for English only.
- The bot may take some time to respond to certain commands, depending on processing requirements.

**Disclaimer**

This code is provided for educational and demonstration purposes only. It is recommended to familiarize yourself with Telegram Bot API best practices and security considerations for production use cases.
