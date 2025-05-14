
'''A right regular pyramid with height h and a base consisting of a regular nsided polygon of side length s
 has a volume V = 1/3 Ah and total surface area S = A + 1/2nsl where A is the base area and l the slant height, 
 which may be calculated from the apothem of the base polygon,
a = 1/2s cot (pi/n) as A = 12 nsa and l = sqrt(h^2 + a^2). 
Use these formulas to define a function, pyramid_AV, returning V and S when passed values for n, s and h.'''

from math import *

def pyramid_AV(n, s, h):
    """
    Compute volume V and total surface area S of a right regular n‐sided pyramid.

    Parameters:
      n (int): number of sides of the regular polygonal base
      s (float): side length of the base polygon
      h (float): vertical height of the pyramid

    Returns:
      (V, S) tuple of floats:
        V = volume
        S = total surface area
    """
    # apothem of the base polygon
    a = 0.5 * s * (1 /tan(pi / n))
    # base area
    A = 0.5 * n * s * a
    # slant height
    l =sqrt(h**2 + a**2)
    # volume
    V = (1/3) * A * h
    # total surface area
    S = A + 0.5 * n * s * l
    return V, S

# Example usage:
if __name__ == "__main__":
    V, S = pyramid_AV(n=5, s=2.0, h=3.0)
    print(f"Volume = {V:.4f}, Surface Area = {S:.4f}")

