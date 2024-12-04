safe = 0

# calculate the difference vector
def difference(line: list) -> list:
    return [b - a for a, b in zip(line[:-1], line[1:])]

# check if difference vector is fit
def difness(difs: list) -> bool:
    difs = set(difs)
    if difs.issubset({1, 2, 3}) or difs.issubset({-1, -2, -3}):
        return True
    return False

# evaluate each version of data line
def evaluate(line: list) -> bool:
    difs = difference(line)
    if difness(difs): return True
    else:
        for i in range(len(line)):
            line_min = line[:i] + line[i+1:]
            if difness(difference(line_min)):
                return True
    return False

with open('data/02', 'r') as f:
    while line := f.readline():
        line = list(map(int, line.split()))
        if evaluate(line): safe += 1
        else: print(line)

print(f"Number of safe readings: {safe}")
