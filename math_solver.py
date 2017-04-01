from sympy import *

# Domain                                #  not done yet
# Intercepts
# Symmetry
# Assymptotes
# Increasing/Decreasing   # \ f''(x)
# Concavity               # /  test

def print_all(eq, d1, d2):
    print("\nOriginal Function:", eq)
    pprint(eq)

    print("\nFirst Derivative:", d1)
    pprint(d1)

    print("\nSecond Derivative:", d2)
    pprint(d2)

def calc_domain(f):
    #  either the real domains
    #  or the important points + margins
    #  as of now, iz fixed
    return -2, 2

if __name__ == "__main__":
    x = Symbol('x')
    
    eq = sympify(input(), evaluate = False)
    d1 = simplify(diff(eq, x))
    d2 = simplify(diff(d1, x))
    
    print_all(eq, d1, d2)
    
    D = calc_domain(eq)
    extrema = simplify(solve(d1, x))
    IPs = simplify(solve(d2, x))
    
    print("\n\n")
    print("Relative Extrema:  ", ', '.join(map(str, extrema)))
    print("Inflection Points: ", ', '.join(map(str, IPs)))
    
    
    plot(eq, (x, D[0], D[1]))
    #plot(eq, Symbol('x'))
    
    input()
