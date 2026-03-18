f = open("test.txt", "a")
f.write("\nNew line")
f.close()

f = open("test.txt", "r")
print(f.read())
f.close()