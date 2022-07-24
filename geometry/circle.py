from typing import Tuple
import polar

def next(x: float, y: float) -> Tuple(float, float):
    # cartesian coordinates of next point on a circle
    d = 1
    start = polar.cartesian_to_polar(x, y)


