with open("2015/2/input.txt") as f:
    content = f.readlines()
    ribbon = 0
    for line in content:
        sline = line.split("x")
        l = int(sline [0])
        w = int(sline [1])
        h = int(sline [2])
        sorteds = sorted ([l, w, h]) 
        ribbon += sorteds[0] * 2 + sorteds[1] * 2
        ribbon += l * w * h
    print (ribbon)
    



