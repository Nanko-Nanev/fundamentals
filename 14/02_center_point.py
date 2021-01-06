def center_point(x, y):
    x = [abs(el) for el in x]
    y = [abs(el) for el in y]
    x_max = max(x)
    x_min = min(x)
    y_max = max(y)
    y_min = min(y)
    if x_max == y_max:
        if x_min >= y_min:
            return 1
    elif x_max <= y_max:
        return 1


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
xy1 = [x1, y1]
xy2 = [x2, y2]

if center_point(xy1, xy2) == 1:
    print(f"({int(x1)}, {int(y1)})")
else:
    print(f"({int(x2)}, {int(y2)})")