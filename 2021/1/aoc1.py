def func():
    y = None
    x = 0
    with open('input.txt') as f:
        data = f.read().splitlines()

    data = list(map(int, data))
    
    for i in data:
        if y != None:
            if i > y:
                x += 1
        y = i   
    print(x)    

func()





