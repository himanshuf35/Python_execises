def dig_pow(n, p):
    result = -1
    numSum = getSum(n,p)
    if numSum % n == 0:
        return numSum // n
    return result

def getSum(n, p):
    numSum = 0
    numList = []
    while n >= 10 :
        numList.append(n % 10)
        n = n // 10 #"//" to perform division 
    numList.append(n)

    for digit in reversed(numList): 
        numSum = numSum + pow(digit, p) #function to calculate power i.e. pow(number, power)
        p = p + 1

    return numSum

print(dig_pow(695, 2))
    