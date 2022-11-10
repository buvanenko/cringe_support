from vkbottle.user import User

import config
from handlers import labelers

user = User(config.TOKEN)

for labeler in labelers:
    user.labeler.load(labeler)

user.run_forever()