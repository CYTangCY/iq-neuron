import numpy as np
with open("8exch400.txt","a") as k:
    with open("lif_ICoutput_0.txt","r") as f:
        lines = []
        for line in f:
            lines.append(float(line.strip()))
        if lines[3600] > 18:
            k.write("1\n")
        if lines[3600] < 5:
            k.write("0\n")

            


