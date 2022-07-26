from typing import Tuple
import random
import polar

def next_point(x: float, y: float, tstep: int = 5, rstep: int = 0) -> Tuple[float, float]:
    """
    cartesian coordinates of next point on a spiral

    tstep = 5
    rstep = 0
    is a circle

    for 600 frames
    tstep = 3
    rstep = 0.01
    is a nice spiral
    """
    c1 = polar.CartesianPoint(x, y)
    p1 = polar.cartesian_to_polar(c1)
    p2 = polar.PolarPoint(
            p1.r + rstep, 
            p1.t + tstep
            )
    c2 = polar.polar_to_cartesian(p2)
    return c2.x, c2.y

if __name__ == "__main__":
    x, y = 1, 0
    for _ in range(361):
        print(x, y)
        x, y = next_point(x, y, 1)


