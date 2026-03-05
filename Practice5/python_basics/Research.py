import re

text = "I love Python programming"

result = re.search(r"Python", text)

print("First occurrence:", result.group())