from plotting import plot
from image import file2image
import math

#Task 1.4.10
data = file2image('img01.png')
data = reversed(data)
dataList = {x+(y*1j) for y,item in enumerate(data) for x,yItem in enumerate(item) if list(yItem)[0] <= 120}
plot(dataList, 255, 1)

#Task 1.4.12
plot({ (1/2 * z) * 1j for z in dataList}, 255, 1)

#Task 1.4.17
eulerList = [pow(math.e, (2 * math.pi * 1j) / n) for n in range(1,20)]
plot(eulerList)

#Task 1.4.18
S = {2 + 2j,3 + 2j,1.75 + 1j,2 + 1j,2.25 + 1j,2.5+1j,2.75+1j,3+1j,3.25+1j}
plot({ z * (pow(math.e, ( (math.pi/4) * 1j))) for z in S})

#Task 1.4.20
def recenterOrigin(z): return (z.real - 83) + ((z.imag - 95) * 1j)
plot({(recenterOrigin(z) * (pow(math.e, ( (math.pi/4) * 1j)))) * 0.5 for z in dataList}, 190, 1)