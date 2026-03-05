import re

text = "Hello Python"

pattern = "Python"

result = re.search(pattern, text)

if result:
    print("Match found:", result.group())
else:
    print("No match")