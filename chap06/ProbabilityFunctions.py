# -*- coding: UTF8 -*-

from __future__ import division
import math, random

def uniform_dpf(x):
    return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
    """ return the probability that a uniform random variable is <= x """
    if x < 0: return 0 # uniform random os never less than 0
    elif x < 1: return x # e.g. P(X < 0.4) = 0.4
    else: return 1 # uniform random is always less than 1

def normal_dpf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma **2) / (sqrt_two_pi * sigma))

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """ find approximate inverse using binary serach """
    # if not standart, compute and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * (inverse_normal_cdf(p, tolerance=tolerance))

    low_z, low_p = -10.0, 0 # normal_cdf(-10) is (very close to) 0
    hi_z, hi_p = 10.0, 1  # normal_cdf(10) is (very close to) 1

    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2 # consider the midpoint
        mid_p = normal_cdf(mid_z) # and the cdf's value there

        if mid_p < p: # midpoint is still too low, search above
            low_z, low_p = mid_z, mid_p
        elif mid_p > p: # midpoint is still too high, search below
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))