from ProbFunc import *

def main():
   TUPLE_DAYS = getData(4)
   
   print("Média: {:.2f}".format(media(TUPLE_DAYS)))
   print("Mediana: {}".format(mediana(TUPLE_DAYS)))
   print("Moda: {}".format(moda(TUPLE_DAYS)))
   print("Amplitude: {}".format(amplitude(TUPLE_DAYS)))
   print("Desvio Médio Absoluto: {:.2f}".format(desvioMedioAbsoluto(TUPLE_DAYS)))
   print("Variância: {:.2f}".format(variancia(TUPLE_DAYS)))
   print("Desvio Padrão: {:.2f}".format(desvioPadrao(TUPLE_DAYS)))
   print("Coeficiente de Variação: {:.2f}".format(coeficienteVariacao(TUPLE_DAYS)))

if __name__ == "__main__":
   main()
   
def setup():
    size(400, 400)
    background(255)

def draw():
    background(123)
    fill(0)
    rect(50, 50, 50, 50)