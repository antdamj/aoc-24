x_count, x_visited = 0, []
a_count, a_visited = 0, []

with open('data/04', 'r') as f:
    lines = [[*l.strip()] for l in f.readlines()]
    # add dummy char to right and bottom to prevent false positives
    lines.append(['0' for _ in range(len(lines[0]))])
    for line in lines: line.append('0')

    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            # first task
            if (i,j) not in x_visited and letter == 'X':
                directions = zip([x for x in range(-1, 2) for _ in range(3)], [x for _ in range(3) for x in range(-1, 2)])
                x_validity = 0
                for a, b in directions:
                    try:
                        if lines[i+a][j+b] == 'M' and \
                            lines[i+2*a][j+2*b] == 'A' and \
                            lines[i+3*a][j+3*b] == 'S':
                            x_validity += 1
                    except IndexError: pass
                if x_validity > 0:
                    x_visited.append((i, j))
                    x_count += x_validity
            
            # second task
            if (i,j) not in a_visited and letter == 'A':
                directions = zip([x for x in (-1, 1) for _ in range(2)], [x for _ in range(2) for x in (-1, 1)])
                for a, b in directions:
                    try:
                        if lines[i+a][j+b] == 'M' and lines[i-a][j-b] == 'S' and \
                            (lines[i-a][j+b], lines[i+a][j-b]) in [('M', 'S'), ('S', 'M')]:
                            a_visited.append((i, j))
                            a_count += 1
                            break
                    except IndexError: pass

print(f"XMAS count: {x_count}")
print(f"X-MAS count: {a_count}")