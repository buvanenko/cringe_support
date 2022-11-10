from typing import Union
from vkbottle.bot import Message
from vkbottle.dispatch.rules import ABCRule

import config

class FromMe(ABCRule[Message]):
    def __init__(self, text: Union[str, list]):
        self.text = text

    async def check(self, event: Message) -> bool:
        if type(self.text) == str:
            return event.from_id == config.USER_ID and event.text.startswith(self.text)
        elif type(self.text) == list:
            for t in self.text:
                if event.from_id == config.USER_ID and event.text.startswith(t):
                    return True
            return False