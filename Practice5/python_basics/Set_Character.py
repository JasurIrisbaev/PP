import re

text = "apple banana cherry"

pattern = r"[ae]"

result = re.findall(pattern, text)

print(result)