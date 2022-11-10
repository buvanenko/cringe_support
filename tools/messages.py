from vkbottle.bot import Message
from vkbottle.user import User

import config

user = User(config.TOKEN)

async def edit(message: Message, text: str):
    a = await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=message.id,
        message=text,
    )
    print(a)