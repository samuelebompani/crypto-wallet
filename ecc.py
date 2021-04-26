def inverse(n, q):
    return extEuclide(q, n)

def extEuclide(n, m):
    r, x0, y0, x1, y1 = n, 1, 0, 0, 1
    while (r > 0):
        q, r = divmod(n, m)
        x0, y0, x1, y1 = x1, y1, x0 - (q*x1), y0 - (q*y1)
        n, m = m, r
    return y0

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class EC(object):
    def __init__(self, a, b, q):
        self.a = a
        self.b = b
        self.q = q
    
    def add(self, p1, p2):
        if (p1.x == 0 and p1.y == 0):
            return (p2.x, p2.y)
        if p1.x == p2.x and (p1.y != p2.y or p1.y == 0):
            return (0,0)
        if p1.x == p2.x:
            # p1 + p1: use tangent line of p1 as (p1,p1) line
            l = (3 * p1.x * p1.x + self.a) * inverse(2 * p1.y, self.q) % self.q
        else:
            l = (p2.y - p1.y) * inverse(p2.x - p1.x, self.q) % self.q
        x = (l * l - p1.x - p2.x) % self.q
        y = (l * (p1.x - x) - p1.y) % self.q
        return Point(x,y)
    
    def mul(self, p, n):
        r = p
        for _ in range(1, n):
            r = self.add(p, r)
        return r