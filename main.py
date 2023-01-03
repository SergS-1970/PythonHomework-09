import telebot
import logger as log

bot = telebot.TeleBot("")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    log.info(message)
    if message.text == '/start':
        bot.reply_to(message, f'Привет, {message.from_user.first_name}.')
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        add_button = telebot.types.KeyboardButton("Add")
        substr_button = telebot.types.KeyboardButton("Substract")
        markup.add(add_button)
        markup.add(substr_button)
        bot.send_message(message.chat.id, "Выберите требуемое действие", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_action(message):
    log.info(message)
    msg = bot.send_message(message.chat.id, 'Введите первое число')
    if message.text == 'Add':                        
        bot.register_next_step_handler(msg, add_first_number, 'ADD') 
    if message.text == 'Substract':                        
        bot.register_next_step_handler(msg, add_first_number, 'SUB') 


def add_first_number(message, operation):
    mes_num = int(message.text)
    msg = bot.send_message(message.chat.id, 'Введите второе число')
    bot.register_next_step_handler(msg, add_second_number, operation, mes_num) 


def add_second_number(message, operation, first_number):
    sec_number = int(message.text)
    if operation == 'ADD':
        result = first_number + sec_number
    if operation == 'SUB':
        result = first_number - sec_number
    res_message = bot.send_message(message.chat.id, f'Результат: {result}')
    bot.register_next_step_handler(res_message, send_welcome) 
    


print('server started')              
bot.infinity_polling()    