# Translator

This Python script provides a simple command-line translator between English and Persian, with the ability to add new words to the translation database. It utilizes the pyfiglet library for a visually appealing welcome message and the gtts library for text-to-speech functionality.

## Features:

### Translation: Translate sentences between English and Persian using a pre-defined word bank.
### Word Bank Management:
- Add new word pairs (English-Persian) to the translation database.
- The word bank is stored in a text file .
- Text-to-Speech: generates an audio file  of the translated sentence (slow pronunciation for clarity).

## Requirements:

- Python 3 (tested with 3.x)
- A database whose name is **Translate.txt**
- pyfiglet library
- gtts library
- internet for generating Text_To_Speech

## How to Use
1. Clone project in your device with this code : ``` git clone https://github.com/Mahdiyar-Tagharobi/PythonCourse/tree/main/Assignment_8 ```
2. Install requirments with these codes : ``` pip install pyfiglet ``` and ``` pip install gtts ```
3. Run main file with pip ``` python Assignment_8.py code ```
4. Follow the interactive menu:
  1- **English to persian:** Translate a sentence from English to Persian.
  2- **Persian to English:** Translate a sentence from Persian to English.
  3- **Add new word to database:** Add a new word pair (English-Persian) to the translation database.
  4- **Exit:** Exit the program.

## Notes:

The script uses a text file (`Translate.txt`) to persist data. Ensure that this file is present in the `Assignment_8` directory relative to the script.
The translation accuracy depends on the quality and completeness of the initial word bank.
Text-to-speech is currently limited to English and Urdu languages provided by gtts.