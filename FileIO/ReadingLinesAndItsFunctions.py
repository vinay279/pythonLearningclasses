with open('abc.txt','r') as f:
    lines = f.readlines()
    for line in lines:
             print(line, end='')
        char = f.read(2)
    print(char)