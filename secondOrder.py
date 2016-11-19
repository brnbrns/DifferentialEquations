###############
# Brian Burns
#  MATH 238
# ay'' + by' + cy = 0
# secondOrder.py
###############

import sys
import math

def main():
    # make sure we have enough arguments
    if len(sys.argv) != 4:
        print("Usage: \"python secondOrder.py [a] [b] [c]\"")
        sys.exit(0)

    # grab the arguments
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    print("The solution to the equation is:\n")

    # get the auxiliary roots
    root = pow(b, 2) - (4*a*c)

    # y = c_1e^(r_1t) + c_2e^(r_2t)
    if root > 0:
        r1 = (-1*b + math.sqrt(root)) / 2*a
        r2 = (-1*b - math.sqrt(root)) / 2*a
        print("y = c_1e^("+str(r1)+"t) + c_2e^("+str(r2)+"t)")

    # y = c_1e^(rt) + c_2te^(rt)
    elif root == 0:
        r = (-1*b) / (2*a)
        print("y = c_1e^("+str(r)+"t) + c_2te^("+str(r)+"t)")

    else:
        alpha = (-1*b) / (2*a)
        beta = math.sqrt((-1*root)) / (2*a)
        # y = c_1cos(Bt) + c_2sin(Bt)
        if alpha == 0.0:
            print("y = c_1cos("+str(beta)+"t) + c_2sin("+str(beta)+"t)")
        # y = c_1e^(at)cos(Bt) + c_2e^(at)sin(Bt)
        else:
            print("y = c_1e^("+str(alpha)+"t)cos("+str(beta)+"t) + c_2e^("+str(alpha)+"t)sin("+str(beta)+"t)")


if __name__ == "__main__":
    main()
