from vkbottle.bot import BotLabeler, Message
from rules.messages import FromMe

import config
from tools.messages import edit

labeler = BotLabeler()

@labeler.message(FromMe('.стата'))
async def stats(message: Message):
    history = await config.user.api.messages.get_history(peer_id=message.peer_id, count=1)

    text = f'''ℹ️ Статистика беседы {message.peer_id}

✉️ Сообщений в беседе: {history.count}'''

    await edit(message, text)