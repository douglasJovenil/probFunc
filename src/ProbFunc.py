from functools import reduce
from pandas import read_csv
from math import ceil, sqrt

def getData(file_name, index):
   return tuple(read_csv(file_name, sep=";").iloc[:, index])

def average(vector):
   return reduce(lambda x, y: x + y, vector) / len(vector)

def median(vector, i=0):
   if (i == ceil(len(vector) / 2)): 
      if (i % 2 == 1): return vector[i-1]
      else: return average((vector[i], vector[i - 1]))
   return median(tuple(sorted(vector)), i + 1)
   
def mode(vector, quantidade=0, retorno=0, i=0):
   if (i == (len(vector) - 1)): return retorno
   elif (vector.count(vector[i]) > quantidade): 
      return mode(vector, vector.count(vector[i]), vector[i], i + 1)
   else: return mode(vector, quantidade, retorno, i + 1)

def amplitude (vector):
   return max(vector) - min(vector)

def absoluteMeanDeviation(vector):
   return sum(map(lambda x: abs(x - average(vector)), vector)) / (len(vector))

def variance(vector):
   return sum(map(lambda x: pow((x - average(vector)), 2), vector)) / (len(vector))

def standardDeviation(vector):
   return sqrt(variance(vector))

def coefficientVariation(vector):
   return standardDeviation(vector) / average(vector)