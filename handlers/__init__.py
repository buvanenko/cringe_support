# Path: handlers\__init__.py

import glob
import re

from sys import platform
if platform == "win32": reg = r".*handlers\\(.+?)\.py"
else: reg = r".*handlers/(.+?)\.py"

labelers = []
for f in [re.search(reg, h).group(1) for h in glob.glob("./handlers/*") if "__" not in h]:
    exec(f"from handlers.{f} import labeler\nlabelers.append(labeler)")

__all__ = ["labelers"]