#!/usr/bin/python3

import glob
import numpy as np
import matplotlib.pyplot as plt

for filename in glob.glob("lif_output_*.txt"):
    imageFilename = list(filename)
    imageFilename[-3:] = 'png'
    imageFilename = "".join(imageFilename)
    with open(filename) as f:
        lines = []
        for line in f:
            lines.append(float(line.strip()))
    plt.figure()
    plt.title(filename)
    plt.plot(lines)
    plt.savefig(imageFilename)
plt.show()

