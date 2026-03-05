import re

text = "Hello, world! Python is great."

result = re.split(r"\W+", text)

print(result)