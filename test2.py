def disemvowel(string):
    tempString = ''
    if len(string) == 0:
        return string
    for charIndex in range(0, len(string)):
        print(charIndex)
        if not checkVowel(string[charIndex]):
            # string = string[: charIndex] + string[charIndex+1 :] #slicing of list [start end] i.e. List[: 5] colon means start for first and end for second param
            tempString = tempString + string[charIndex]
    return tempString
    
def checkVowel(char):
    isVowel = False
    vowelList = ['a','e','i','o', 'u']
    for vowel in vowelList:
        if char.lower() == vowel:
                isVowel = True
                break
    return isVowel

print(disemvowel("This website is for losers LOL!"))