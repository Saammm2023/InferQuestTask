import matplotlib.pyplot as plt
import numpy as np
import random


heads=[0,0]


heads_tails = [0, 0]

for _ in range(100):
    heads_tails[random.randint(0, 1)] += 1
    plt.bar(["Heads", "Tails"], heads_tails, color=["red", "blue"])
    plt.pause(0.001)#this is the key to create that animated effect

plt.show()
