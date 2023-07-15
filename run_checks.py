print("hello from python")
import os
from glob import glob
result = [y for x in os.walk(".") for y in glob(os.path.join(x[0], '*.md'))]

print(f"I found the following md files {result}")
