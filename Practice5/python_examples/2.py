import re

text = ["ab", "abb", "abbb", "abbbb"]

pattern = r"ab{2,3}"

for word in text:
    if re.fullmatch(pattern, word):
        print(word)