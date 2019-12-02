

def to():
    with open("1.txt", "r") as f:
        l = f.read().split(",")
        l = [int(i) for i in l] 
        for i in range(0, len(l), 4):
            if l[i] == 99:
                return l
            if l[i] == 1:
                l[l[i+3]] = l[l[i+1]] + l[l[i+2]]
            elif l[i] == 2:
                l[l[i+3]] = l[l[i+1]] * l[l[i+2]]
            else:
                continue


def toto():
    for x in range(0,100):
        for y in range(0,100):
            if insert(x,y):
                return 100 * x + y
    
            
def insert (x, y):
    with open("1.txt", "r") as f:
        l = f.read().split(",")
        l = [int(i) for i in l]
        l[1] = x
        l[2] = y
        for i in range(0, len(l), 4):
            if l[i] == 99:
                if l[0] == 19690720:
                    return True
                return False
            if l[i] == 1:
                l[l[i+3]] = l[l[i+1]] + l[l[i+2]]
            elif l[i] == 2:
                l[l[i+3]] = l[l[i+1]] * l[l[i+2]]
    
