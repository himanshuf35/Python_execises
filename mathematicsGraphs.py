import matplotlib.pyplot as pyplot
import numpy as numpy

# Function which calculates the polynomial function 
# @args polynomial tuple consist values of x, degree of polynomial and the list of coefficients
def makePoylnomial(polynomialTuple):
    x, degree, constantList = polynomialTuple
    y = 0
    listLen = len(constantList)
    constantList = reversed(constantList)
    polyRepresentation = 'y = '
    for index,coefficient in enumerate(constantList):
        y = y + coefficient * (pow(x, index))
        polyRepresentation = str(polyRepresentation) + str(coefficient) + ' * x^' + str(index) 
        if index < (listLen - 1):
            polyRepresentation = polyRepresentation + ' + ' 
    return y, polyRepresentation

#Function which returns the tuple of a polynomial which is the derivative of passed polynomial Tuple
# @args polynomial tuple consist values of x, degree of polynomial and the list of coefficients
def diffPolynomial(polynomialTuple): 
    x, degree, constantList = polynomialTuple
    constantList = constantList[: len(constantList) - 1]
    for index, coefficient in enumerate(constantList):
        constantList[index] = (degree - index) * coefficient
    return x, degree - 1, constantList

#Function which plots the graph of given polynomial and it's derivative polynomial
def plotPolyAndDiffPoly(x, y , ydiff):
    pyplot.subplot(2,1,1)
    pyplot.plot(x, y)
    pyplot.subplot(2,1,2)
    pyplot.plot(x, ydiff)
    pyplot.show()

x = numpy.arange(-10, 10, 0.1)
polynomialTuple = (x, 1, [2, 1])
y, rep = makePoylnomial(polynomialTuple)
print(rep)
derivativePolynomial = diffPolynomial(polynomialTuple)
yDiff, diffRep = makePoylnomial(derivativePolynomial)
print(diffRep)
plotPolyAndDiffPoly(x, y, yDiff)



