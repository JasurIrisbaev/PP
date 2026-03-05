import re

text = "HelloWorldPythonExample"

result = re.sub(r"([A-Z])", r" \1", text)

print(result.strip())