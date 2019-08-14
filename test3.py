def dig_pow(n, p):
    

def getSum(n, p):
    numSum = 0
    numList = []
    while tempNum > 10 :
        numList.append(tempNum % 10)
        tempNum = tempNum // 10
    numList.append(tempNum)

    for digit in reversed(numList): 
        numSum = numSum + pow(digit, p)
        p = p + 1

    return numSum

print(dig_pow(89, 1))
    