import re

text = "My number is 12345"

result = re.findall(r"\d+", text)

print(result)