import re

text = "Apple banana cherry"

pattern = r"[A-Z]"

result = re.findall(pattern, text)

print(result)