import re

text = "HelloWorldPythonExample"

result = re.split(r"(?=[A-Z])", text)

print(result)