from math import sqrt


x_start = -10
x_end = 8
dx = 0.5
x = x_start

print('x|y')

while x <= x_end:
    if -10 <= x <= 0:
        print(x, -0.5 * x - 3)
    elif 0 < x <= 3:
        print(x, -sqrt(9 - x**2))
    elif 3 < x <= 6:
        print(x, sqrt(9 - (x - 6)**2))
    else:
        print(x, 0)
    x = x + dx

