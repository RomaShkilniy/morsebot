import telebot
import config
import time

bot = telebot.TeleBot(config.token)

char_to_dots = {
	'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
	'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
	'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
	'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
	'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
	'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
	'6': '-....', '7': '--...', '8': '---..', '9': '----.',
	'&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
	':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
	'-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, 'Welcome {} 😘'.format(message.chat.first_name))
	bot.send_message(message.chat.id, 'I\'m a bot that converts text to Morse code.' )

@bot.message_handler(commands=['random'])
def random_dice(message):
  bot.send_dice(message.chat.id)

@bot.message_handler(content_types=['text'])
def send(message):
	m = message.text.upper()
	list_of_char = []
	result = ''
	for i in m:
		if i in char_to_dots:
			list_of_char.append(char_to_dots[i])
		else:
			result = 'Only English'

	if result != 'Only English':
			result = ' '.join(list_of_char)

	bot.send_message(message.chat.id, result )

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
  bot.send_sticker(message.chat.id, message.sticker.file_id)
  print(message.sticker.file_id)

@bot.message_handler(content_types=['dice'])
def dice_value(message):
  time.sleep(2.8)
  bot.send_message(message.chat.id, f'Your value is {message.dice.value}')

if __name__ == '__main__':
	bot.polling(none_stop = True, interval = 0)