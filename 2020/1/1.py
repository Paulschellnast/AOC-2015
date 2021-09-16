with open("input.txt", "r") as f:
    numbers = f.read().split()
    expenses = list(map(int, numbers))
    target = 2020
    
    for i, number in enumerate(expenses[:-1]): 
        complementary = target - number
        if complementary in expenses[i+1:]:
            print("Found: {} and {}".format(number, complementary))
            
            second = number * complementary #multiplies the found numbers.
            print(second)        