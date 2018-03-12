from functools import reduce
from pandas import read_csv
from math import ceil

def getData(index):
   return tuple(read_csv("Janeiro.csv", sep=";").iloc[:, index])

def media(vetor):
   return reduce(lambda x, y: x + y, vetor) / len(vetor)

def mediana(vetor, i=0):
   if (i == ceil(len(vetor) / 2)): 
      if (i % 2 == 1): return vetor[i-1]
      else: return media((vetor[i], vetor[i - 1]))
   return mediana(tuple(sorted(vetor)), i + 1)
   
def moda(vetor, quantidade=0, retorno=0, i=0):
   if (i == (len(vetor) - 1)): return retorno
   elif (vetor.count(vetor[i]) > quantidade): 
      return moda(vetor, vetor.count(vetor[i]), vetor[i], i + 1)
   else: return moda(vetor, quantidade, retorno, i + 1)
   
def amplitude(vetor):
   return max(vetor) - min(vetor)

def desvioMedioAbsoluto(vetor):
   return sum(map(lambda x: abs(x - media(vetor)), vetor)) / (len(vetor))