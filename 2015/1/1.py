with open("2015/1/input.txt") as f:
    content = f.read()
    floors = 0
    for i, elem in enumerate (content):
        if elem == "(":
            floors += 1
        else: 
            floors -= 1
        if floors == -1:
            print (i + 1)
    print (floors)          

