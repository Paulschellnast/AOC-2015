with open("input.txt", "r") as f:
    numbers = f.read().split()
    list = list(map(int, numbers))
    target = 2020
    
    for i, number in enumerate(list[:-1]): 
        complementary = target - number
        if complementary in list[i+1:]:
            print("Found: {} and {}".format(number, complementary))
            
            second = number * complementary #multiplies the found numbers.
            print(second)        