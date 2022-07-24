import math

def cartesian_to_polar(x, y):
    # returns r, t in degrees
    r = math.sqrt(x*x + y*y)
    t = math.acos(x/r) if y >= 0 else -1 * acos(x/r)
    return (r, math.degrees(t))

def polar_to_cartesian(r, t):
    # returns x, y
    return (r * math.cos(math.radians(t)), r * math.sin(math.radians(t)))

if __name__ == "__main__":
    print(cartesian_to_polar(1, 1))
    print(polar_to_cartesian(1.4142135623730951, 45))


