from vectorTasks import list_dot, list_add, list_scalar_mul
import sys

f = open('voting_record_dump109.txt')
mylist = list(f)
mylist = [listItem.split() for listItem in mylist]

democratsSet = {senatorData[0] for senatorData in mylist if senatorData[1] == 'D'}
republicanSet = {senatorData[0] for senatorData in mylist if senatorData[1] == 'R'}

# Task 2.12.1: 
# a procedure create voting dict(strlist) that, given a list of strings (voting records from the source file),
# returns a dictionary that maps the last name of a senator to a list of numbers representing that senator’s voting record
def create_voting_dict(strlist):
    return {senatorData[0]: [int(item) for item in senatorData[3 : ]] for senatorData in strlist}

voting_dict = create_voting_dict(mylist)

# Task 2.12.2: 
# a procedure policy compare(sen a, sen b, voting dict) that,
# given two names of senators and a dictionary mapping senator names to lists representing voting records,
# returns the dot-product representing the degree of similarity between two senators’ voting policies.
def policy_compare(sen_a, sen_b, voting_dict): 
    return list_dot(voting_dict[sen_a], voting_dict[sen_b])


# Task 2.12.3:
# a procedure most similar(sen, voting dict) that,
# given the name of a senator and a dictionary mapping senator names to lists representing voting records,
# returns the name of the senator whose political mindset is most like the input senator

def most_similar(sen, voting_dict):
    currentSimilarSenate = ''
    currentSimilarityValue = 0
    for senateName, senateVotes in voting_dict.items():
        if senateName == sen: continue
        dotProduct = list_dot(voting_dict[sen], voting_dict[senateName])
        if dotProduct > currentSimilarityValue:
            currentSimilarityValue = dotProduct
            currentSimilarSenate = senateName
    return currentSimilarSenate

# Task 2.12.4:
# a procedure least similar(sen, voting dict) that returns the name of the senator
# whose voting record agrees the least with the senator whose name is sen.

def least_similar(sen, voting_dict):
    currentSimilarSenate = ''
    currentSimilarityValue = sys.maxsize
    for senateName, senateVotes in voting_dict.items():
        if senateName == sen: continue
        dotProduct = list_dot(voting_dict[sen], voting_dict[senateName])
        if dotProduct < currentSimilarityValue:
            currentSimilarityValue = dotProduct
            currentSimilarSenate = senateName
    return currentSimilarSenate

# Task 2.12.7:
# a procedure find average similarity(sen, sen set, voting dict) that, given the name sen of a senator,
# compares that senator’s voting record to the voting records of all senators whose names are in sen set,
# computing a dot-product for each, and then returns the average dot-product.

def average_similarity(sen, sen_set, voting_dict):
    summedSenVector = [iter * 0 for iter in range(len(voting_dict[sen]))]
    for aSen in sen_set:
        summedSenVector = list_add(summedSenVector, voting_dict[aSen])
    return list_dot(voting_dict[sen], summedSenVector)/len(sen_set)

senSet = {'Sessions', 'Rockefeller', 'Sununu', 'Pryor'}
allAverages = {average_similarity(senName, senSet, voting_dict ): senName for senName in voting_dict.keys() }

# Task 2.12.8:
# Write a procedure find average record(sen set, voting dict) that, given a set of names of senators,
# finds the average voting record. That is, perform vector addition on the lists representing their voting records,
# and then divide the sum by the number of vectors.
        
def average_record(sen_set, voting_dict):
    n = len(voting_dict[list(senSet)[0]])
    summedSenVector = [iter * 0 for iter in range(n)]
    for aSen in sen_set:
        summedSenVector = list_add(summedSenVector, voting_dict[aSen])
    return list_scalar_mul((1/len(senSet)), summedSenVector)


