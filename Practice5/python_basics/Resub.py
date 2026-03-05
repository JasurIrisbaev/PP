import re

text = "I like cats"

result = re.sub(r"cats", "dogs", text)

print(result)