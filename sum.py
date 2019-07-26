import fileinput

num = 0


for line in fileinput.input():
    try:
        num += int(line)
    except:
        pass
print(num)
