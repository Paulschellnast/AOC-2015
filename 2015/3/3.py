class position: 
    def __init__(self,x,y):
        self.x = x
        self.y = y
up = "^"
down = "v"
left = "<"
right = ">"
pos = position(0, 0)
poss = position(0, 0)
locations = [pos]
with open("2015/3/input.txt") as f:
    content = f.read()
    for i, direction in enumerate (content):

    for direction in content:
        if direction == up:
            pos = position(pos.x, pos.y-1)
        if direction == down:
            pos = position(pos.x, pos.y+1)
        if direction == left:
            pos = position(pos.x-1, pos.y)
        if direction == right:
            pos = position(pos.x+1, pos.y)
        if len([x for x in locations if x.x == pos.x and x.y == pos.y]) ==0:
            locations.append(pos)
print(len(locations))
    
