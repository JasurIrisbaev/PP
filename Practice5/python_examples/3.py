import re

text = "hello_world test_string Hello_World another_example"

pattern = r"[a-z]+_[a-z]+"

print(re.findall(pattern, text))