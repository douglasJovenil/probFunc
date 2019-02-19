# Probabilistic Functional

This repository has the purpose of implement probabilistic and statistical functions using concepts of functional programming at python. The book used as support material is: *DOWNING, Douglas; CLARK, Jeffrey. Estatística aplicada. 3. ed. São Paulo: Saraiva, 2010*.

## Requeriments
![numpy](https://img.shields.io/badge/Numpy-1.12.0-brightgreen.svg)
![python-dateutil](https://img.shields.io/badge/python_dateutil-2.5.0-brightgreen.svg)
![six](https://img.shields.io/badge/six-1.5-brightgreen.svg)
![pytz](https://img.shields.io/badge/pytz-2011k-brightgreen.svg)

## Setup
`$ pip install -r requeriments.txt`

## Methods
The struct of this section is:

```bash
Some explanation / math definitions
# Params
methodSyntax()
# Return
```

### getData
```Python
# file_name: path of csv file you want to get data
# index: column to extract data
getData(file_name, index)
# Return a Tuple with all data of csv file and column passed as arguments 
```

### average
Value that shows where the values of collection are concentrates.

![average](https://latex.codecogs.com/gif.latex?average&space;=&space;\overline{x}&space;=&space;\frac{\sum_{i=1}^{n}x_i}{n})
```Python
# vector: data vector to extract the average
average(vector)
# Return a number that represents the average of a collection
```

### median
For a relation where the collections values are sorted, the median is the number
that has many values above as below of him.
```Python
# vector: data vector to extract the median
median(vector)
# Return a number that represents the median of a collection
```

### mode
Value that occurs more often at a collection.
```Python
# vector: data vector to extract the mode
mode(vector)
# Return a number that represents the mode of a collection
```

### amplitude
Represents the distance between the higher and lower value.

![amplitude](https://latex.codecogs.com/gif.latex?amplitude&space;=&space;max(x)&space;-&space;min(x))
```Python
# vector: data vector to extract the amplitude
mode(vector)
# Return a number that represents the amplitude of a collection
```

### absoluteMeanDeviation
Mean of distances between each value and the mean.

![absoluteMeanDeviation](https://latex.codecogs.com/gif.latex?absoluteMeanDeviation&space;=&space;\frac{\sum_{i=1}^{n}|x_i&space;-&space;\overline{x}|}{n})
```Python
# vector: data vector to extract the absoluteMeanDeviation
absoluteMeanDeviation(vector)
# Return a number that represents the absoluteMeanDeviation of a collection
```

### variance
Absolute Mean Deviation squared.

![variance](https://latex.codecogs.com/gif.latex?Variance&space;=&space;\sigma^2&space;=&space;\frac{\sum_{i=1}^{n}|x_i-&space;\overline{x}|^2}{n})
```Python
# vector: data vector to extract the variance
variance(vector)
# Return a number that represents the variance of a collection
```

### standardDeviation
Square root of Variance.

![standardDeviation](https://latex.codecogs.com/gif.latex?standardDeviation&space;=&space;\sigma&space;=&space;\sqrt{\frac{\sum_{i=1}^{n}|x_i-&space;\overline{x}|^2}{n}})
```Python
# vector: data vector to extract the standardDeviation
standardDeviation(vector)
# Return a number that represents the standardDeviation of a collection
```

### coefficientVariation
Measures the dispersion in relation to the mean.

![coefficientVariation](https://latex.codecogs.com/gif.latex?coefficientVartion&space;=&space;\frac{standardDeviation}{mean}&space;=&space;\frac{\sigma}{\overline{x}})
```Python
# vector: data vector to extract the coefficientVariation
coefficientVariation(vector)
# Return a number that represents the coefficientVariation of a collection
```