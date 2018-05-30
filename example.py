#!/usr/bin/env python

from eggcellent import egg
import matplotlib.pyplot as plt

plt.scatter([0, 1], [0, 1], marker=None, verts=egg, s=200)
plt.savefig('eggs.png')
