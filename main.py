import config
from handlers import labelers

user = config.user

for labeler in labelers:
    user.labeler.load(labeler)

user.run_forever()