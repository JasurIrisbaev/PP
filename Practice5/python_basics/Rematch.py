import re

text = "Hello"

result = re.match(r"Hello", text)

if result:
    print("Matched:", result.group())
else:
    print("No match")