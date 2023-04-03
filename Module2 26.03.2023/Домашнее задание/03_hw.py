x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

color1 = "White"
if (x1 + y1) % 2 == 1:
    color1 = "Black"

color2 = "White"
if (x1 + y1) % 2 == 1:
    color2 = "Black"

if color1 == color2:
    print("Yes")
else:
    print("No")
