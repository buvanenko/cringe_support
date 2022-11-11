from vkbottle.bot import BotLabeler, Message
from rules.messages import FromMe

from tools.messages import edit

labeler = BotLabeler()

@labeler.message(FromMe('.сосиска'))
async def info(message: Message):
    await edit(message, "", f"photo434356505_457288263")