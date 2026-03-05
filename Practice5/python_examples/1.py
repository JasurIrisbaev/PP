import re

text = ["a", "ab", "abb", "ac", "b"]

pattern = r"ab*"

for word in text:
    if re.fullmatch(pattern, word):
        print(word)