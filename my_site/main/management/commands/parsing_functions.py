from ...models import *
from telethon.sync import TelegramClient, events

# Разбивает строку сообщения из поста на список, пригодный к использованию в базе данных
def split_str(post_str):
    import re
    import copy

    list = []
    result = [0, []]

    # Проверям, что в сообщении не менее 2 строк
    if not isinstance(post_str, str):  # Бывает, что попадает нестрока
        result[0] = -1
        return result
    if len(re.split('\n\n', str(post_str))) < 2:
        result[0] = -1
        return result

    # Название и тэг
    post_str1 = re.split('\n\n', post_str)[0]
    if len(re.split('\W*#', post_str1)) < 2:  # Игнорируем рекламу
        result[0] = -1
        return result
    else:
        # Название
        list.append(re.split('\W*#', post_str1)[0])
        # Тег
        list.append(re.split('\W*#', post_str1)[1])

    # Координаты
    post_str2 = re.split('\n\n', post_str)[1]
    if len(re.findall('\d+.\d+', post_str)) < 2:  # Если с координатами что-то не так
        result[0] = -1
        return result
    list.append(re.findall('\d+.\d+', post_str)[0])  # Список из элементов: точка, окруженная цифрами
    list.append(re.findall('\d+.\d+', post_str)[1])

    #	print(List)
    result[1] = copy.copy(list)
    return result


# Принимает сообщение и посылает его в базу
def message_to_base(message):

    if split_str(message.message)[0] != -1:  # Проверяем, имеет ли сообщение тот текст, который нам необходим.
        print('The message matches the info message criteria')
        post_str_list = split_str(message.message)[1]  # Разбиваем сообщение на список

        print("Sending text data to db...")
        content = post_str_list[1] + '. ' + post_str_list[2] + ', ' + post_str_list[3]
        AlbumElem.objects.create(title=post_str_list[0], content=content)
        print("Text data has been sent")

    else:  # Сюда входят случаи, когда сообщение рекламное либо когда оно состоит из прикрепленного изображения.
        print('The message does not match the info message criteria')
