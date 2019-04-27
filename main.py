def printSimplePath(start : int, end : int, current_path : list, arcs : list):
    current_path.append(start)

    for arc in arcs:
        if arc[0] != current_path[-1]:
            continue

        if arc[1] in current_path:
            continue

        if arc[1] == end:
            print(current_path + [end])
            continue

        printSimplePath(arc[1], end, current_path, arcs)
    
    current_path.pop()

gStart, gEnd = [int(i) for i in input().split()]
gPath = list()
listArcs = [(1, 2),
            (1, 7),
            (2, 1),
            (2, 3),
            (2, 6),
            (3, 4),
            (3, 5),
            (3, 7),
            (4, 5),
            (4, 6),
            (4, 7),
            (7, 6)]

printSimplePath(gStart, gEnd, gPath, listArcs)
