import re

text = "Hello world Test Python REGEX Example"

pattern = r"[A-Z][a-z]+"

print(re.findall(pattern, text))