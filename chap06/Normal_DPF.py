# -*- coding: UTF8 -*-

from matplotlib import pyplot as plt
from chap06 import ProbabilityFunctions as pf

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [pf.normal_dpf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [pf.normal_dpf(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
plt.plot(xs, [pf.normal_dpf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
plt.plot(xs, [pf.normal_dpf(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')

plt.legend()
plt.title("Various Normal pdfs")
plt.show()