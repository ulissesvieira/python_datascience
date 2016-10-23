# -*- coding: UTF8 -*-

import math

def vector_add(v, w):
  """ adds corresponding elements """
  return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
  """ subtracts corresponding elements """
  return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum1(vectors):
  """ sum all corresponding elements """
  result = vectors[0] # start with the first vector
  for vector in vectors[1:]: # then loop over the others
    result = vector_add(result, vector) # and add them to the result
  return

def vector_sum(vectors):
  return reduce(vector_add, vectors)

def scalar_multiply(c, v):
  """ c is a number, v is a vector """
  return [c * v_i for v_i in v]

def vector_mean(vectors):
  """ compute the vector whose ith element is the mean of the ith elements of the input vectors """
  n = len(vectors)
  return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
  """ v_1 * w_1 + ... + v_n * w_n """
  return sum(v_1 * w_1 for v_1, w_1 in zip(v, w))

def sum_of_squares(v):
  """ v_1 * v_1 + ... + v_n * v_n """
  return dot(v, v)

def magnitude(v):
  return math.sqrt(sum_of_squares(v)) # math.sqrt is square root function

def squared_distance(v, w):
  """ (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2 """
  return sum_of_squares(vector_subtract(v, w))

def distance1(v, w):
  return math.sqrt(squared_distance(v, w))

def distance(v, w):
  return magnitude(vector_subtract(v, w))