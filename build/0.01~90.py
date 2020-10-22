import numpy as np
n = 0
with open("session.txt","w") as f:

    while n <= 3.1417:
        f.write("1\n")
        f.write("0 %f\n" %(n))
        f.write("1 %f\n" %(n))
        f.write("2 0\n")
        f.write("-1\n")
        n += 0.0001
    f.write("-1")

