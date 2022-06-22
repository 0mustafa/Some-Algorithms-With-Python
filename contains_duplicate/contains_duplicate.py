
#Is a number used twice in the list?

firstList = [1,2,5,3,4,5]
secondList = []

def duplicate():
    #iterate in firstList
    for num in firstList:
        if num in secondList:
            #returns True and stop the algorithm
            return True
        #append to the secondList when is secondList has no firstList element
        secondList.append(num)
    #returns False and stop the algorithm
    return False


print(duplicate())
