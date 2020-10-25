import numpy as np
with open("0exch1000re42no1.txt","a") as k:
    with open("lif_ICoutput_0.txt","r") as f:
        lines = []
        for line in f:
            p = float(line.strip())
            if p < 4.0:
            	k.write("0\n")
            	break

            	

            


