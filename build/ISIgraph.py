#!/usr/bin/python3

import glob
import numpy as np
import matplotlib.pyplot as plt
import math

n = 0.00
for filename in glob.glob("lif_FRoutput_*.txt"):
    imageFilename = list(filename)
    imageFilename[-3:] = 'png'
    imageFilename = "".join(imageFilename)
    with open(filename) as f:
        lines = []
        nlist = []
        threelist = []
        for line in f:
            three = n**3
            lines.append(float(line.strip()))
            nlist.append(float(n))
            threelist.append(float(three))
            n += 0.0001
    n = 0
    plt.figure()
    plt.title(filename)
    plt.xlabel("theta")
    plt.ylabel("sinetheta")
    plt.plot(nlist, lines, label = "ISI")
    #plt.plot(nlist, threelist, label = "x^3")
    plt.legend()
    plt.grid(True)
    plt.savefig(imageFilename)
plt.show()


