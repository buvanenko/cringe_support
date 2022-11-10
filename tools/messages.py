from vkbottle.bot import Message
from vkbottle.user import User

import config

async def edit(message: Message, text: str, attachment: str = ''):
    a = await config.user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=message.id,
        message=text,
        attachment=attachment
    )
    print(a)