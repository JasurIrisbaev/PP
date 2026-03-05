import re

text = "The rain in Spain"

pattern = r"^The.*Spain$"

if re.search(pattern, text):
    print("Matched!")
else:
    print("Not matched")