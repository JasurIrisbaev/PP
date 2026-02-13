i = int(input())
count = 0
for x in len(i):
    if x % 2 == 0:
        count+=1

if count == s.length():
    print("Valid")
else:
    print("Not valid")