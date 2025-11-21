def evaluate_linear(m, b, x):
    return m * x + b

print(evaluate_linear(2,3,5))

x_values = [-2, -1, 0, 1, 2, 3]
m = 3
b = -1

for x in x_values:
    print(f"f({x}) = {evaluate_linear(m,b,x)}")
