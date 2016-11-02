# -*- coding: UTF8 -*-

from __future__ import division
import math

from matplotlib import pyplot as plt
from chap06 import ProbabilityFunctions as pf
from collections import Counter

def make_hist(p, n, num_points):
    data = [pf.binomial(n, p) for _ in range(num_points)]

    # use a bar chart to show the actual binomial samples
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()], [v / num_points for v in histogram.values()], 0.8, color='0.75')

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # user a line chart to show the normal aproximation
    xs = range(min(data), max(data) + 1)
    ys = [pf.normal_cdf(i + 0.5, mu, sigma) - pf.normal_cdf(i - 0.5, mu, sigma) for i in xs]

    plt.plot(xs, ys)
    plt.title("Binomial Distribuition vs. Nomal Aproximation")

    plt.show()