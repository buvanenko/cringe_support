from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules import ABCRule

import config

chars = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N']

class TelegramSpam(ABCRule[Message]):
    def __init__(self):
        self.filters = ['t.me']

    async def check(self, event: Message) -> bool:
        if True in [(f in event.text) for f in self.filters]:
            sender = await config.user.api.users.get(user_ids=event.from_id)
            if True in [(c in sender[0].first_name.upper()) for c in chars]:
                return True

from tools.messages import edit

labeler = BotLabeler()

@labeler.message(TelegramSpam())
async def spam(message: Message):
    await config.user.api.messages.delete(message_ids=message.id, spam=True)