def TwoLettersThatAppearsAtLeastTwiceInTheStringWithoutOverLapping(input):
    for i, char in enumerate(input):
        if i + 1 <len (input) and input.count(char + input[i + 1]) >= 2:
            return True
    return False
def ContainsAtLeastOneLetterWhichRepeatsWithExactlyOneLetterBetweenThem(input):
    for i, char in enumerate(input):
        if i + 2 <len (input) and input[i + 2] == char:
            return True
    return False
with open("2015/5/input.txt") as f:
    content = f.readlines()
    nice = 0


        
    
    
    
    for line in content:
        if TwoLettersThatAppearsAtLeastTwiceInTheStringWithoutOverLapping(line):
            if ContainsAtLeastOneLetterWhichRepeatsWithExactlyOneLetterBetweenThem(line):
                nice += 1 
    print(nice)               
                    

                
     
            



        
    
    
 