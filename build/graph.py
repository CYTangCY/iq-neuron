#!/usr/bin/python3

import glob
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

times = 0
fired = False
GATE = 40
GROUND = 16
spike_list= [0,0,0]
potential_list = []
a_list = []
time_list = [0,0,0]
time_count = 0
EMAfrlist = [0]
for filename in glob.glob("lif_output_*.txt"):
    imageFilename = list(filename)
    imageFilename[-3:] = 'png'
    imageFilename = "".join(imageFilename)
    with open(filename) as f:
        for line in f:
            potential_list.append(float(line))

            for i in range (int(len(potential_list)/100)):
                a_list = potential_list[100*i+1:100*(i+1)]
                #print(a_list)
                spike_count = 0
                #print(potential_list)
                potential_list = []
                
                for j in a_list :
                    if j > GATE and fired==False:
                        spike_count += 1
                        fired = True
                    if j == GROUND and fired == True:
                        fired = False
                time_count += (1/15)
                time_list.append(time_count)
                spike_list.append(spike_count*15)
                #print("sp",spike_list)
                #print("ti",time_list)

    
    #with open('EMAfralpha = 0.1.txt','r') as f1:
        #for line in f1:
            #EMAfrlist.append(float(line))
    MAfr = pd.DataFrame({'x':spike_list})
    MAfr['y'] = MAfr['x'].rolling(2).mean()
    #EMAfr = pd.DataFrame({'i':EMAfrlist})
    #EMAfr['j'] = EMAfr['i'].rolling(2).mean()
    #print(MAfr['y'])
    #with open('input2.2_1.0_28.txt','w') as f2:
        #f2.write(str(MAfr['y']))
        
    fig1 = plt.figure(figsize = (15,10))
    plt.title("fr_%s"%(filename))
    plt.plot(time_list,MAfr['y'], label = 'oriFR')
    #plt.plot(EMAfrlist, label = 'EMAFR')
    plt.legend()
    plt.grid(True)
    #plt.plot(time_list,spike_list)
    plt.xlabel("time")
    plt.ylabel("firingrate(spike/s)")
    spike_list = []
    a_list = []
    time_list = []
plt.show()
