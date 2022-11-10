from vkbottle.bot import BotLabeler, Message
from rules.messages import FromMe

labeler = BotLabeler()

@labeler.message(FromMe('..i'))
async def info(message: Message):
    await message.answer("Привет!")