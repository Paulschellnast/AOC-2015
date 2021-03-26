with open("2015/2/input.txt") as f:
    content = f.readlines()
    papyrus = 0
    for line in content:
        sline = line.split("x")
        l = int(sline [0])
        w = int(sline [1])
        h = int(sline [2])
        papyrus += 2*l*w + 2*w*h + 2*h*l 
        papyrus += min (l*w, w*h, h*l) 
    print (papyrus)
    



