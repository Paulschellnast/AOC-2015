import sys 
import hashlib 
with open("2015/4/input.txt") as f:
    content = f.read()
    i = 1
    while True:
        m = hashlib.md5((content +str(i)).encode()).hexdigest()
        if m[0] == "0" and m[1] == "0" and m[2] == "0" and m[3] == "0" and m[4] == "0":
            print(i)
            sys.exit()

            


        
        
        
        i += 1 