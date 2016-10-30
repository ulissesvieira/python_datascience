# -*- coding: UTF8 -*-

from chap05 import num_friends, daily_minutes
from chap05 import BasicsStatisticsFunctions as bsf

print(len(num_friends))
print(bsf.mean(num_friends))
print(bsf.median(num_friends))
print(bsf.quantile(num_friends, 0.10))
print(bsf.quantile(num_friends, 0.25))
print(bsf.quantile(num_friends, 0.50))
print(bsf.quantile(num_friends, 0.75))
print(bsf.quantile(num_friends, 0.90))
print(bsf.mode(num_friends))
print(bsf.data_range(num_friends))
print(bsf.variance(num_friends))
print(bsf.standart_deviation(num_friends))
print(bsf.interquartile_range(num_friends))
print(bsf.covariance(num_friends, daily_minutes))
print(bsf.correlation(num_friends, daily_minutes))