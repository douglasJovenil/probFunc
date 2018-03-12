from ProbFunc import *

TUPLE_DAYS = getData(4)

print("Média: {:.2f}".format(media(TUPLE_DAYS)))
print("Mediana: {}".format(mediana(TUPLE_DAYS)))
print("Moda: {}".format(moda(TUPLE_DAYS)))
print("Amplitude: {}".format(amplitude(TUPLE_DAYS)))
print("Desvio Médio Absoluto: {:.2f}".format(desvioMedioAbsoluto(TUPLE_DAYS)))