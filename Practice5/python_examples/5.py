import re

text = ["ab", "acb", "a123b", "abbbb", "aXb"]

pattern = r"a.*b"

for word in text:
    if re.fullmatch(pattern, word):
        print(word)