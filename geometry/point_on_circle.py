# python3 alexgeometry.py
from typing import Tuple
import math

def next_point_on_a_circle(x, y, number_of_segments: int, radius: float) -> Tuple[int, int]:
    a = math.sin(180/number_of_segments)
    b = 2*radius
    beta0 = 180 * (number_of_segments - 2) / (2 * number_of_segments)
    arctan = math.atan(y/x) if x != 0 else 0
    beta = beta0 - 90 + arctan
    c = math.cos(beta)
    d = math.sin(beta)
    return [x + b*a*c, y + b*a*d]



if __name__ == "__main__":
    start_x, start_y = 0, 1
    n = 10
    r = 1
    x, y = start_x, start_y
    for _ in range(n):
        x, y = next_point_on_a_circle(x, y, n, r)
        print(x, y)
    print(x == start_x)
    print(y == start_y)

