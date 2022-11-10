import random

from vkbottle.bot import BotLabeler, Message
from rules.messages import FromMe

import config
from tools.messages import edit

labeler = BotLabeler()

@labeler.message(FromMe(['.хохлы', '.хохол']))
async def info(message: Message):
    videos = await config.user.api.video.get(owner_id=-208926469, album_id=2)
    video = random.choice(videos.items)
    await edit(message, "", f"video{video.owner_id}_{video.id}")