with open("input.txt", "r") as f:
    
    numbers = f.readlines()
    numbers = [int(i.split("\n")[0]) for i in numbers]
    
    for g in numbers:
        for p in numbers:
            if (2020 - g - p) in numbers:
                print(2020 - g - p, g, p, file=open("solution.txt", "a"))

with open("solution.txt", "r") as r:
                    test = r.read().split()
                    test = [(i.split("\n")[0]) for i in test]
                    liste = list(map(int, test))
                    nodublica = list(dict.fromkeys(liste))
                    def finalcalc(nodublica):
                        result = 1
                        for x in nodublica:
                            result = result * x
                        return result
                    
                    print(finalcalc(nodublica))
                    
                   
                    
                
                
                