import re

# File to read equations from
filename = 'equations_Algebraic.txt'

def parse_equation(eq):
    monomials = re.findall(r'\((.*?)\)', eq)
    degrees = []
    variables = set()
    
    for mono in monomials:
        vars_in_mono = [v.strip() for v in mono.split('&')]  # clean whitespace
        degrees.append(len(vars_in_mono))
        variables.update(vars_in_mono)
    
    return degrees, variables

max_degree = 0
all_variables = set()

equations = []

# Read file manually
with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        if line in ['[', ']'] or not line:
            continue
        if line.endswith(','):
            line = line[:-1]
        equations.append(line)

# Now process each equation
for eq in equations:
    degrees, vars_in_eq = parse_equation(eq)
    max_degree = max(max_degree, max(degrees))
    all_variables.update(vars_in_eq)

print(f"Maximum algebraic degree across all equations = {max_degree}")
print(f"Total number of unknown variables = {len(all_variables)}")
