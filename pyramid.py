import fileinput

level = []

for line in fileinput.input():
    n = int(line)
    
    for i in range(1,n+1):
        if i > 1:
            level = list(range(1,i)) + list(reversed(list(range(1,i+1))))
            #level = list(reversed(list(range(1,i+1))))
        else:
            level =[1]
        print(''.join(list(map(str,level))))

    for i in list(reversed(list(range(1,n)))):
        if i>1:
            level = list(range(1,i))+ list(reversed(list(range(1,i+1))))
        else:
            level = [1]
        print(''.join(list(map(str,level))))