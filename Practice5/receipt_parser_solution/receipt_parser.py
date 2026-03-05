import re

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# product names
products = re.findall(r"\d+\.\n(.+)", text)

# prices (стоимость товара)
prices = re.findall(r"\n(\d+\s?\d*,\d{2})\nСтоимость", text)

# date and time
datetime = re.search(r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}", text)

# total
total = re.search(r"ИТОГО:\n([\d\s,]+)", text)

print("PRODUCTS:")
for p in products:
    print("-", p)

print("\nPRICES:")
for price in prices:
    print("-", price)

if datetime:
    print("\nDATE:", datetime.group())

if total:
    print("TOTAL:", total.group(1))