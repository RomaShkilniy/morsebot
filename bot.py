import telebot
import config

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


if __name__ == '__main__':
	bot.polling(none_stop = True, interval = 0)