
import tic_tac_toe
import telebot
bot = telebot.TeleBot("5772216067:AAFuwNZ2c_giYo2zonx6lKLle4SN9HRGQUA", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = f"{message.from_user.first_name}"
    if(f"{message.from_user.last_name}" != "None"):
        name += f" {message.from_user.last_name}"
    mess = f"Доброе утро, {name} ))"
    bot.send_message(message.chat.id, mess + str(message.chat.id), parse_mode=None)

@bot.message_handler(commands=['game'])
def game(message):
    tic_tac_toe.field = [[tic_tac_toe.EMPTY_CHAR for x in range(3)] for y in range(3)]
    bot.send_message(message.chat.id, tic_tac_toe.show_field(tic_tac_toe.field) , parse_mode=None)

comb = [str(k+i) for i in ("1", "2", "3") for k in ("a", "b", "c")]

def resetField():
    tic_tac_toe.field = [[tic_tac_toe.EMPTY_CHAR for x in range(3)] for y in range(3)]

resetField()

@bot.message_handler()
def default(message):    
    if message.text in comb:        
        result = tic_tac_toe.set_user_position(message.text)
        if result[0] != 0:
            bot.send_message(message.chat.id, result[1] , parse_mode=None)
            bot.send_message(message.chat.id, tic_tac_toe.show_field(tic_tac_toe.field) , parse_mode=None)
            return
        bot.send_message(message.chat.id, tic_tac_toe.show_field(tic_tac_toe.field) , parse_mode=None)
        if tic_tac_toe.is_win(tic_tac_toe.user_char, tic_tac_toe.field):
            bot.send_message(message.chat.id,'you win', parse_mode=None)
            resetField()
            return
        if tic_tac_toe.is_draw(tic_tac_toe.field):
            bot.send_message(message.chat.id,'is draw', parse_mode=None)
            resetField()
            return
        move = tic_tac_toe.get_computer_position(tic_tac_toe.field)
        if move is not None:
            x, y = move
            tic_tac_toe.field[y][x] = tic_tac_toe.computer_char
            bot.send_message(message.chat.id, tic_tac_toe.show_field(tic_tac_toe.field) , parse_mode=None)
            if tic_tac_toe.is_win(tic_tac_toe.computer_char, tic_tac_toe.field):
                bot.send_message(message.chat.id, 'you lose', parse_mode=None)
            else:
                bot.send_message(message.chat.id, "choose your field!" , parse_mode=None)
    else:
        bot.send_message(message.chat.id, "Invalid input" , parse_mode=None)

bot.polling(none_stop=True)



