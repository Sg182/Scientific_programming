import numpy as np

class Quadratic:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def value(self,x):
        return (self.a*(x**2) + self.b*(x) +self.c)
    
    def table(self,L,R,n):

        '''Computes the value of the polynomial at all the points in the interval [L,R]'''

        x_values = np.linspace(L,R,n)
        print(f"{'x':>10} {'f(x)':>10}")
        print("-" * 20)

        for i in x_values:
            print(f"{i:10.5f} {self.value(i):10.5f}")

    def roots(self):
        '''Calculates the roots of the quadratic equation'''


        discriminant = self.b**2 - 4 * self.a * self.c
        if discriminant > 0:
            # Two real roots
            root1 = (-self.b + np.sqrt(discriminant)) / (2 * self.a)
            root2 = (-self.b - np.sqrt(discriminant)) / (2 * self.a)
            return root1, root2
        elif discriminant == 0:
            # One real root (double root)
            root = -self.b / (2 * self.a)
            return root, root
        else:
            # Complex roots
            real_part = -self.b / (2 * self.a)
            imaginary_part = np.sqrt(-discriminant) / (2 * self.a)
            root1 = real_part + 1j * imaginary_part
            root2 = real_part - 1j * imaginary_part
            return root1, root2

if __name__ == "__main__":        ## This statement is True if we directly run this script (i.e. if we run some other script)

    quad = Quadratic(1,-3,2)

    #input = int(input("Enter the value of x and the interval separated by a comma',': "))
    #x, n = input.split()
    print(quad.table(-2,2,5))
    print(quad.roots())
