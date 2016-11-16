###############
# Brian Burns
# x' = ax + by, y' = cx + dy
# system.py
###############

import sys
import math

def main():
    if len(sys.argv) != 5:
        print("Usage: \"python3 system.py [a] [b] [c] [d]\"")
        sys.exit(0)

    a = -float(sys.argv[1])
    b = -float(sys.argv[2])
    c = -float(sys.argv[3])
    d = -float(sys.argv[4])

    if c > 0:
        diffy = [a, -d]
        coeffy = (a*d) - (b*c)
        print(a+d)
        print(coeffy)
        y = second(1, a+d, coeffy)
        # y = c_1e^(r1t) + c_2e^(r2t)
        if y[0] == 0:
            coeffx1 = -(((1/c)*y[2]) + (d/c))
            coeffx2 = -(((1/c)*y[3]) + (d/c))
            x = str(coeffx1) + "c_1e^("+str(y[2])+"t) + " + str(coeffx2) + "c_2e^("+str(y[3])+"t)"
        # y = c_1e^(rt) + c_2te^(rt)
        if y[0] == 1:
            coeffx1 = -(((1/c)*y[2]) + (d/c))
            coeffx2 = -(((1/c)*y[2]) + (d/c))
            coeffx3 = (-1/c)
            x = str(coeffx1) + "c_1e^("+str(y[2])+"t) + " + str(coeffx2) + "c_2te^("+str(y[2])+"t) + " + str(coeffx3) + "c_2e^("+str(y[2])+"t)"
        # y = c_1cos(bt) + c_2sin(bt)
        if y[0] == 2:
            coeffx1 = y[2] / c
            coeffx2 = -y[2] / c
            coeffx3 = d / c
            x = str(coeffx1) + "c_1sin("+str(y[2])+"t) + " + str(coeffx2) + "c_2cos("+str(y[2])+"t) + " + str(coeffx3) + "c_1cos("+str(y[2])+"t) + " + str(coeffx3) + "c_2sin("+str(y[2])+"t)"
        # y = c_1e^(at)cos(bt) + c_2e^(at)sin(bt)
        if y[0] == 3:
            coeffx1 = (-y[2]/c) + (d/c)
            coeffx2 = y[3] / c
            coeffx3 = -y[3] / c
            x = str(coeffx1) + "c_1e^("+str(y[2])+"t)cos("+str(y[3])+"t) + " + str(coeffx1) + "c_2e^("+str(y[2])+"t)sin("+str(y[3])+"t) + " + str(coeffx2) + "c_1e^("+str(y[2])+"t)sin("+str(y[3])+"t) + " + str(coeffx3) + "c_2e^("+str(y[2])+"t)cos("+str(y[3])+"t)"
    if c < 0:
        diffy = [a, d]
        coeffy = (a*d) + (b*(-1*c))
        print(a+d)
        print(coeffy)
        y = second(1, a+d, coeffy)
        # y = c_1e^(r1t) + c_2e^(r2t)
        if y[0] == 0:
            coeffx1 = -(((1/c)*y[2]) + (d/c))
            coeffx2 = -(((1/c)*y[3]) + (d/c))
            x = str(coeffx1) + "c_1e^("+str(y[2])+"t) + " + str(coeffx2) + "c_2e^("+str(y[3])+"t)"
        # y = c_1e^(rt) + c_2te^(rt)
        if y[0] == 1:
            coeffx1 = ((1/c)*y[2]) - (d/c)
            coeffx2 = ((1/c)*y[2]) - (d/c)
            coeffx3 = (1/c)
            x = str(coeffx1) + "c_1e^("+str(y[2])+"t) + " + str(coeffx2) + "c_2te^("+str(y[2])+"t) + " + str(coeffx3) + "c_2e^("+str(y[2])+"t)"
        # y = c_1cos(bt) + c_2sin(bt)
        if y[0] == 2:
            coeffx1 = -y[2] / c
            coeffx2 = y[2] / c
            coeffx3 = -d / c
            x = str(coeffx1) + "c_1sin("+str(y[2])+"t) + " + str(coeffx2) + "c_2cos("+str(y[2])+"t) + " + str(coeffx3) + "c_1cos("+str(y[2])+"t) + " + str(coeffx3) + "c_2sin("+str(y[2])+"t)"
        # y = c_1e^(at)cos(bt) + c_2e^(at)sin(bt)
        if y[0] == 3:
            coeffx1 = (y[2]/c) - (d/c)
            coeffx2 = -y[3] / c
            coeffx3 = y[3] / c
            x = str(coeffx1) + "c_1e^("+str(y[2])+"t)cos("+str(y[3])+"t) + " + str(coeffx1) + "c_2e^("+str(y[2])+"t)sin("+str(y[3])+"t) + " + str(coeffx2) + "c_1e^("+str(y[2])+"t)sin("+str(y[3])+"t) + " + str(coeffx3) + "c_2e^("+str(y[2])+"t)cos("+str(y[3])+"t)"

    print("x = " + x + "\n" + y[1])

    # cx = y' - dy
    # x = (1/c)Dy - (d/c)y

    # y = c_1e^(r_1t) + c_2e^(r_2t)
    # dy = r_1c_1e^(r_1t) + r_2c_2e^(r_2t)
    # x = (1/c)(r_1)c_1e^(r_1t) + (1/c)r_2c_2e^(r_2t) - (d/c)c_1e^(r_1t) - (d/c)c_2e^(r_2t)
    # x = ((1/c)(r_1) - (d/c))c_1e^(r_1t) + ((1/c)(r_2) - (d/c))c_2e^(r_2t)

    # y = c_1e^(rt) + c_2te^(rt)
    # dy = rc_1e^(rt) + c_2e^(rt) + rc_2te^(rt)
    # x = (1/c)rc_1e^(rt) + (1/c)c_2e^(rt) + (1/c)rc_2te^(rt) - (d/c)c_1e^(rt) - (d/c)c_2te^(rt)
    # x = ((1/c)r - (d/c))c_1e^(rt) + ((1/c)r - (d/c))c_2te^(rt) + (1/c)c_2e^(rt)


def second(a, b, c):
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
        return([0, "y = c_1e^("+str(r1)+"t) + c_2e^("+str(r2)+"t)", r1, r2])

    elif root == 0:
        r = (-1*b) / (2*a)
        return([1, "y = c_1e^("+str(r)+"t) + c_2te^("+str(r)+"t)", r])

    else:
        alpha = (-1*b) / (2*a)
        beta = math.sqrt((-1*root)) / (2*a)
        if alpha == 0.0:
            return([2, "y = c_1cos("+str(beta)+"t) + c_2sin("+str(beta)+"t)", beta])
        else:
            return([3, "y = c_1e^("+str(alpha)+"t)cos("+str(beta)+"t) + c_2e^("+str(alpha)+"t)sin("+str(beta)+"t)", alpha, beta])

if __name__ == "__main__":
    main()
