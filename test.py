# print(ord('A'))
# #lowercase
# print(ord('a')) function for getting ascii value of a char ord(char)
tempStr = [1,2,2,3,3]
tempList = [tempStr[0]]
currentChar = tempStr[0]
print(len(tempStr)) #function to check length of iterable len()
for charIndex in range(1, len(tempStr)): #function for getting range is range(start, stop, step)
    iterChar = tempStr[charIndex]
    if iterChar != currentChar:
        tempList.append(iterChar)
        currentChar = iterChar

print(tempList)

