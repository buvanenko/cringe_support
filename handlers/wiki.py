import wikipediaapi
from vkbottle.bot import BotLabeler, Message

from rules.messages import FromMe
from tools.messages import edit

labeler = BotLabeler()
wiki_wiki = wikipediaapi.Wikipedia('ru')

@labeler.message(FromMe('.в '))
async def info(message: Message):
    page_py = wiki_wiki.page(message.text[3:])
    try:
        link = page_py.fullurl
        text = page_py.text.split('\n')[0]
        text = f"{text}\n\n{link}"
    except KeyError:
        text = "Статья не найдена"
    await edit(message, text)