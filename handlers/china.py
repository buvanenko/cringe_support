from vkbottle.bot import BotLabeler, Message
from rules.messages import FromMe

from tools.messages import edit

labeler = BotLabeler()

d = {'Й': '认', 'Ц': '凵', 'У': '丫', 'К': '长', 'Е': '乇', 
'Н': '卄', 'Г': '厂', 'Ш': '山', 'Щ': '屮', 'З': '了', 
'Х': '乂', 'Ъ': '乚', 'Ф': '中', 'Ы': '劜', 'В': '乃', 
'А': '卂', 'П': '冂', 'Р': '尸', 'О': '口', 'Л': '人', 
'Д': '丑', 'Ж': '米', 'Э': '刁', 'Я': '牙', 'Ч': '丩', 
'С': '匚', 'М': '从', 'И': '凵', 'Т': '丅', 'Ь': '乚', 
'Б': '万', 'Ю': '扣', 'Q': '彑', 'W': '山', 'E': '乇', 
'R': '尺', 'T': '丅', 'Y': '丫', 'U': '凵', 'I': '工', 
'O': '口', 'P': '尸', 'A': '卂', 'S': '丂', 'D': '刀', 
'F': '下', 'G': '厶', 'H': '卄', 'J': '丁', 'K': '长', 
'L': '乚', 'Z': '乙', 'X': '乂', 'C': '匚', 'V': ' リ', 
'B': '乃', 'N': '冂'}


@labeler.message(FromMe('.кит '))
async def info(message: Message):
    text = message.text[5:].upper()
    new_text = ''
    for i in text:
        if i in d:
            new_text += d[i]
        else:
            new_text += i
    await edit(message, new_text)