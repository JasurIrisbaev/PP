import re

text = "hello_world_example"

def snake_to_camel(match):
    return match.group(1).upper()

result = re.sub(r"_([a-z])", snake_to_camel, text)

print(result)