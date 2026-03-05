import re

text = "abb abbb abbbb a"

pattern = r"ab{2,3}"

matches = re.findall(pattern, text)

print(matches)