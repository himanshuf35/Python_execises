import math
def find_nb(m):
    result = -1
    m = math.sqrt(m) 
    if m - math.floor(m) != 0 :
        return -1
    
    print(math.floor(m))
    for number in range(1,math.floor(m)) :
        if (2 * m) // (number * (number + 1)) == 1:
            print(number)
            result = number
            break
    return result
print(find_nb(4183059834009))
# print(find_nb(4183059834009))