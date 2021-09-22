with open("input.txt", "r") as f:
    
    numbers = f.readlines()
    numbers = [int(i.split("\n")[0]) for i in numbers]
    
    for g in numbers:
        for p in numbers:
            if (2020 - g - p) in numbers:
                print((2020 - g - p) * g * p)
                exit()