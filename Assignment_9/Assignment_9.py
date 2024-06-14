import random as rand
import datetime
import telebot
import qrcode as q
import gtts
from persiantools.jdatetime import JalaliDate

def msg(message ,m):
    return bot.send_message(message.chat.id, m)
     

bot = telebot.TeleBot("Your bot token", parse_mode=None)

k1 = telebot.types.KeyboardButton("/game")
k2 = telebot.types.KeyboardButton("/age")
k3 = telebot.types.KeyboardButton("/max")
k4 = telebot.types.KeyboardButton("/voice")
k5 = telebot.types.KeyboardButton("/argmax")
k6 = telebot.types.KeyboardButton("/qrcode")
k7 = telebot.types.KeyboardButton("/help")

markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
markup.add(k1, k2, k3, k4, k5, k6, k7)
game_markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
restart_key = telebot.types.KeyboardButton("/restart")
game_markup.add(restart_key)

rand_n = {}

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, f'Hi  {message.from_user.first_name}\n', reply_markup=markup)     	

@bot.message_handler(commands=['game'])
def game_command(message):
	
    username = message.from_user.username
    rand_n[username] = rand.randint(0, 100)

    msg(message, "Guess number game!")
    m = bot.send_message(message.chat.id, "Enter your guess: ", reply_markup=game_markup)
    bot.register_next_step_handler(m, game)

@bot.message_handler(commands=["restart"])
def restart_game(message):
    username = message.from_user.username
    rand_n[username] = rand.randint(0, 100)

    msg(message, "Game is restarted....")
    msg(message, "Guess number game!")
    m = bot.send_message(message.chat.id, "Enter your guess: ", reply_markup=game_markup)
    bot.register_next_step_handler(m, game)
     

@bot.message_handler(commands=['age'])
def age_command(message):
    m = bot.send_message(message.chat.id, "Enter your birthday date like 1111/11/13 (in shamsi date)")
    bot.register_next_step_handler(m, age)




@bot.message_handler(commands=['voice'])
def voice_command(message):
    m = bot.send_message(message.chat.id, "Enter your text(in English)")
    bot.register_next_step_handler(m, voice)
    

@bot.message_handler(commands=['max'])
def max_command(message):
    m = bot.send_message(message.chat.id, "Enter your numbers such as 1,2,3,4.. to determine which one is bigger")
    bot.register_next_step_handler(m, max_number)


@bot.message_handler(commands=['argmax'])
def max_index_command(message):
    m = bot.send_message(message.chat.id, "Enter your numbers such as 1, 2, 3, 4... to determine which index is the largest number")
    bot.register_next_step_handler(m, max_index)


@bot.message_handler(commands=['qrcode'])
def qrcode_command(message):
    m = bot.send_message(message.chat.id, "Enter a sequence to convert to qrcode")
    bot.register_next_step_handler(m, qrcode_maker)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id ,"/game :\t For play number game\n/restart :\t to restart the game\n/age :\t Calculate your age\n/voice :\t Convert your text to voice\n/max :\t show the biggest number\n/argmax :\t show the index of biggest number\n/qrcode :\t Make a QRcode with your text\n/help :\t Show help", reply_markup=markup)
            

@bot.message_handler(func=lambda m: True)
def menu(message):
    help(message)

def game(message):
    try:
        username = message.from_user.username
        guess = int(message.text)

        if guess == rand_n[username]:
            #Win
            bot.send_message(message.chat.id, "That's Right!🕺🏻", reply_markup=markup)
            # bot.register_next_step_handler(m, game)
        elif guess > rand_n[username]:
            m = bot.send_message(message.chat.id, "Go Down 👇🏻", reply_markup=game_markup)
            bot.register_next_step_handler(m, game)

        elif guess < rand_n[username]:
            m = bot.send_message(message.chat.id, "Go Up 👆🏻", reply_markup=game_markup)
            bot.register_next_step_handler(m, game)

        user_input = int(message.text)
    except:
        if message.text == '/restart':
            restart_game(message)
        else:
            bot.send_message(message.chat.id, "Enter the number correctly\nGame is closed", reply_markup=markup)


def age(message):

    try:
        y, m, d = str(message.text).split('/')
        y, m, d = int(y), int(m), int(d)
        AD = JalaliDate(y, m, d).to_gregorian()
        AD = datetime.date.today() - AD
        age = AD.days // 365
        bot.send_message(message.chat.id, f'Your age is {age}', reply_markup=markup)

    except:
        bot.send_message(message.chat.id, 'Your date is not correctly entered', reply_markup=markup)


def voice(message):
    try: 
        voice = message.text
        voice = gtts.gTTS(voice, lang='en', slow=True)
        voice.save("Assignment_9/Voice.mp3")

        with open("Assignment_9/Voice.mp3", "rb") as file:
            bot.send_voice(message.chat.id, file)
    except: 
        bot.send_message(message.chat.id, "Error...\ntry again", reply_markup=markup)


def max_number(message):
    try:
        print(message.text)
        sp = message.text.split(',')
        sp = list(map(lambda text: int(text.strip()), sp))
        print(max(sp))
        bot.send_message(message.chat.id, f"The biggest number is: {max(sp)}")
    except:
        bot.send_message(message.chat.id, "Enter the numbers correctly", reply_markup=markup)


def max_index(message):
    try:
        print(message.text)
        sp = message.text.split(',')
        sp = list(map(lambda text: int(text.strip()), sp))
        print(max(sp))
        bot.send_message(message.chat.id, f"The index of biggest number is: {sp.index(max(sp))}")
    except:
        bot.send_message(message.chat.id, "Enter the numbers correctly", reply_markup=markup)


def qrcode_maker(message):
    res = q.make(message.text)
    res.save("QRcode1.png")
    with open("QRcode1.png", "rb") as photo:
        bot.send_photo(message.chat.id, photo)



bot.infinity_polling()