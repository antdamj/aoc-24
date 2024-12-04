import re
sum = 0

def evaluate_multiplication(mul: list) -> int:
    num1, num2 = map(int, mul[4:-1].split(','))
    return num1 * num2

regex_task1 = r'mul\(\d{1,3},\d{1,3}\)'
regex_task2 = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'

with open('data/03-kat', 'r') as file:
    valid_multiplication = True
    while line := file.readline():
        exprs = re.findall(regex_task2, line)
        for expr in exprs:
            if expr == 'do()': valid_multiplication = True
            elif expr == 'don\'t()': valid_multiplication = False
            elif valid_multiplication:
                sum += evaluate_multiplication(expr)

print(sum)