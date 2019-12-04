
with open("1.txt", "r") as f:
    routes = f.read().split("\n")
    l = routes[0].split(",")
    r = routes[1].split(",")

    f_route_pos = set()
    s_route_pos = set()

    x = 0
    y = 0

    ans = {}
    length = 0

    for i in l:
        d = i[0]
        n = i[1:]
        for _ in range(int(n)):
            length += 1
            if d == 'R':
                x += 1
                if (x,y) not in ans:
                    ans[(x,y)] = length
                f_route_pos.add((x, y))
            if d == 'U':
                y += 1
                if (x,y) not in ans:
                    ans[(x,y)] = length
                f_route_pos.add((x, y))
            if d == 'D':
                y -= 1
                if (x,y) not in ans:
                    ans[(x,y)] = length
                f_route_pos.add((x, y))
            if d == 'L':
                x -= 1
                if (x,y) not in ans:
                    ans[(x,y)] = length
                f_route_pos.add((x, y))


    x = 0
    y = 0
    length = 0
    ans2 = {}
    
    for i in r:
        d = i[0]
        n = i[1:]
        for _ in range(int(n)):
            length += 1
            if d == "R":
                x += 1
                if (x,y) not in ans2:
                    ans2[(x,y)] = length
                s_route_pos.add((x, y))
            if d == "U":
                y += 1
                if (x,y) not in ans2:
                    ans2[(x,y)] = length
                s_route_pos.add((x, y))
            if d == "D":
                y -= 1
                if (x,y) not in ans2:
                    ans2[(x,y)] = length
                s_route_pos.add((x, y))
            if d == 'L':
                x -= 1
                if (x,y) not in ans2:
                    ans2[(x,y)] = length
                s_route_pos.add((x, y))
    

    both = s_route_pos&f_route_pos

    p1 = min([abs(x)+abs(y) for (x,y) in both])
    p2 = 999999999

    for p in both:
        p2 = min(ans[p]+ans2[p], p2)
        

    print(p1,p2)    


    
