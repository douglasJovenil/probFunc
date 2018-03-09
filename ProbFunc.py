from functools import reduce
from pandas import read_csv

def getData(index):
   return tuple(read_csv("Janeiro.csv", sep=";").iloc[:, index])

def media(vetor):
   return reduce(lambda x, y: x + y, vetor) / len(vetor)

def mediana(vetor, i=0):
   if i == int(len(vetor) / 2): 
      if i % 2 == 0: return vetor[i]
      else: return media((int(vetor[i]), vetor[i+1]))

   return mediana(vetor, i + 1)