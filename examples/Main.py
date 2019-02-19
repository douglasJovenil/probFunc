from os import getcwd
from sys import path
path.append(getcwd().replace('examples', 'src')) # Add the lib folder to the import PATH

from ProbFunc import *

def main():
    TUPLE_DAYS = getData("days.csv", 0) # Save the data of column 0 of the file days.csv
    print("Days:", end=' ')
    for value in TUPLE_DAYS: print(value, end=' ') # Print the values of TUPLE_DAYS
    print("\nAverage: {:.2f}".format(average(TUPLE_DAYS)))
    print("Median: {}".format(median(TUPLE_DAYS)))
    print("Mode: {}".format(mode(TUPLE_DAYS)))
    print("Amplitude: {}".format(amplitude(TUPLE_DAYS)))
    print("Absolute Mean Deviation: {:.2f}".format(absoluteMeanDeviation(TUPLE_DAYS)))
    print("Variance : {:.2f}".format(variance(TUPLE_DAYS)))
    print("Standard Deviation: {:.2f}".format(standardDeviation(TUPLE_DAYS)))
    print("Coefficient of Variation: {:.2f}".format(coefficientVariation(TUPLE_DAYS)))


if __name__ == "__main__":
   main()