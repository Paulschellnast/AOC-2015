def doubleletter(input):
    for i, char in enumerate (input):
        if i + 1 <len (input) and char == input[i + 1]:
            return True
    return False

with open("2015/5/input.txt") as f:
    content = f.readlines()
    nice = 0


        
    
    
    
    for line in content:
        if line.count("a") + line.count("e") + line.count("i") + line.count("o") + line.count("u") >= 3:
            if doubleletter(line):
                if line.count("ab") == 0 and line.count("cd") == 0 and line.count("pq") == 0 and line.count("xy") == 0:
                    nice += 1 
    print(nice)               
                    

                
     
            



        
    
    
 