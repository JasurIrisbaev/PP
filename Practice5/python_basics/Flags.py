import re

text = "hello World"

result = re.search(r"world", text, re.IGNORECASE)

if result:
    print("Found:", result.group())