import numpy as np
import time 
import matplotlib.pyplot as plt
import statistics
import simpy
import random

n_samples = 10
n_structure = 50 + 50 * np.random.rand(n_samples, 2), None
X, y = n_structure

# Creating data points in a scatter plot makes it hard to move the points randomly like a simulation