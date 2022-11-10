# Path: handlers\__init__.py

import glob
import re

labelers = []
for f in [re.search(r".*handlers\\(.+?)\.py", h).group(1) for h in glob.glob("./handlers/*") if "__" not in h]:
    exec(f"from handlers.{f} import labeler\nlabelers.append(labeler)")

print(labelers)

__all__ = ["labelers"]