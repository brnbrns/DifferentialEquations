###############
# Brian Burns
#  MATH 238
# x' = ax + by, y' = cx + dy
# system.py
###############

import sys
import math
import sympy as sy

def main():
    # make sure we have enough arguments
    if len(sys.argv) != 5:
        print("Usage: \"python system.py [a] [b] [c] [d]\"")
        sys.exit(0)

    # grab the arguments
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    d = float(sys.argv[4])

    # initialize sympy functions
    t = sy.symbols("t")
    x = sy.Function("x")(t)
    y = sy.Function("y")(t)

    # create x' = ax + by, y' = cx + dy
    e1 = sy.Eq(x.diff(t), a*x + b*y)
    e2 = sy.Eq(y.diff(t), c*x + d*y)
    eqs = (e1, e2)

    # solve the system
    sol = sy.dsolve(eqs)

    print("The solution to the system is:")
    sy.pprint(sy.simplify(sol[0]));
    sy.pprint(sy.simplify(sol[1]));

if __name__ == "__main__":
    main()
