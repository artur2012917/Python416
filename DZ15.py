from math import pi

area = {
    'circle': lambda x: pi * x * x,
    'rectangle': lambda x, y: x * y,
    'trapezoid': lambda a, b, h: (a + b) * h / 2
}

print(area['circle'](2))
print(area['rectangle'](10,13))
print(area['trapezoid'](7,5,3))
