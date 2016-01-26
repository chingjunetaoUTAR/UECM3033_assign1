import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( (sy.sin(x)*sy.cos(x))/(sy.sin(x)+1), (x,0,sy.pi ))
    return ans
    
def my_solution():
    A = np.array( [[1,1,1,1,1,1,1,1,1,1],[5,2,1,1,1,1,1,1,1,1], [1,3,1,4,1,1,2,1,1,2],[1,1,1,5,1,8,1,6,1,3],[1,7,1,7,1,4,1,1,2,1],[1,6,1,6,1,2,1,3,1,5],[1,4,1,5,1,9,1,2,1,6],[5,1,3,1,6,1,1,1,4,1],[1,2,1,2,1,4,1,6,1,2],[1,2,1,5,1,2,1,7,1,9]] )
    b = np.array([55,61,88,173,118,147,183,117,129,207])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1202462
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
