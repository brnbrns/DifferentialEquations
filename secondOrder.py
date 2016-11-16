###############
# Brian Burns
# ay'' + by' + cy = 0
# secondOrder.py
###############

import sys
import math

def main():
    if len(sys.argv) != 4:
        print("Usage: \"python3 secondOrder.py [a] [b] [c]\"")
        sys.exit(0)

    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    root = pow(b, 2) - (4*a*c)

    # if a == 0:
    #     if b == 0:
    #         print("y = 0")
    #     else:
    #         r = (-1*c) / b
    #         print("y = c1e^("+str(r)+"t) + c2te^("+str(r)+"t)")

    if root > 0:
        r1 = (-1*b + math.sqrt(root)) / 2*a
        r2 = (-1*b - math.sqrt(root)) / 2*a
        print("y = c_1e^("+str(r1)+"t) + c_2e^("+str(r2)+"t)")

    elif root == 0:
        r = (-1*b) / (2*a)
        print("y = c_1e^("+str(r)+"t) + c_2te^("+str(r)+"t)")

    else:
        alpha = (-1*b) / (2*a)
        beta = math.sqrt((-1*root)) / (2*a)
        if alpha == 0.0:
            print("y = c_1cos("+str(beta)+"t) + c_2sin("+str(beta)+"t)")
        else:
            print("y = c_1e^("+str(alpha)+"t)cos("+str(beta)+"t) + c_2e^("+str(alpha)+"t)sin("+str(beta)+"t)")


if __name__ == "__main__":
    main()
