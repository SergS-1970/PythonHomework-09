
def info(message):
    data = open('info_log.txt', 'a+', encoding='utf-8')
    data.writelines(f'user_id: {message.from_user.id} текст: {message.text}\n')
    data.close() 

def error(message):
    data = open('error_log.txt', 'a+', encoding='utf-8')
    data.writelines(f'user_id: {message.from_user.id} текст: {message.text}\n')
    data.close() 
