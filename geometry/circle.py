from typing import Tuple
import polar

def next_point(x: float, y: float, step: int = 5) -> Tuple[float, float]:
    """
    cartesian coordinates of next point on a circle
    """
    c1 = polar.CartesianPoint(x, y)
    p1 = polar.cartesian_to_polar(c1)
    p2 = polar.PolarPoint(p1.r, p1.t + step)
    c2 = polar.polar_to_cartesian(p2)
    return c2.x, c2.y

if __name__ == "__main__":
    x, y = 1, 0
    for _ in range(361):
        print(x, y)
        x, y = next_point(x, y, 1)


