from typing import Tuple
import math

class Point:
    def __str__(self):
        return str(self.str)

class CartesianPoint(Point):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.str = (self.x, self.y)

class PolarPoint(Point):
    def __init__(self, r: float, t: float):
        self.r = r
        self.t = t
        self.str = (self.r, self.t)

def cartesian_to_polar(p: CartesianPoint) -> PolarPoint:
    r = math.sqrt(p.x*p.x + p.y*p.y)
    t = math.acos(p.x/r) if p.y >= 0 else -1 * acos(p.x/r)
    return PolarPoint(r, math.degrees(t))


def polar_to_cartesian(p: CartesianPoint) -> CartesianPoint:
    return CartesianPoint(
            p.r * math.cos(math.radians(p.t)), 
            p.r * math.sin(math.radians(p.t)))

if __name__ == "__main__":
    print(cartesian_to_polar(CartesianPoint(1, 1)))
    print(polar_to_cartesian(PolarPoint(1.4142135623730951, 45)))


