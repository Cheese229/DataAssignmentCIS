"""
    Figuring out how to animate a scatter plot
    At the end, to create moving points in a scatter is harder than making everything change in terms of 'i'
    The animation can be found in the folder "chartAnim"
    The gif was created using 'ImageMagick'
"""

import matplotlib.pyplot as plt 
import seaborn as sns 

my_dpi=96

for i in range(0,10):
    fig = plt.figure(figsize=(480/my_dpi, 480/my_dpi), dpi=my_dpi)
    plt.scatter(i, i*i, s=40+i*600, alpha=0.5, edgecolors="grey", linewidth=2)
    plt.xlim(0,10)
    plt.ylim(0,100)
    filename='step'+str(i)+'.png'
    plt.savefig(filename, dpi=96)
    plt.gca()