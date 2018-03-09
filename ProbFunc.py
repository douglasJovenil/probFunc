import matplotlib.pyplot as pyplot
from functools import reduce
from pandas import read_csv
import numpy

def getData(index):
   return tuple(read_csv("Janeiro.csv", sep=";").iloc[:, index])

def media(vetor):
   return reduce(lambda x, y: x + y, vetor) / len(vetor)

def mediana(vetor, i=0):
   if i == int(len(vetor) / 2): 
      if i % 2 == 0: return vetor[i]
      else: return media((vetor[i]), vetor[i + 1])
   return mediana(tuple(sorted(vetor)), i + 1)

def histograma(vetor):
   pyplot.hist(numpy.array([vetor]))
   
