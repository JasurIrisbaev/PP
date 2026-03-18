import re

text = "Hello 123"

result = re.match(r"Hello", text)

if result:
    print("Matched:", result.group())
else:
    print("No match")