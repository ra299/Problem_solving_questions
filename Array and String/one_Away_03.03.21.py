def oneEditAway(firstStr, secondStr):
    if(len(firstStr) == len(secondStr)):
        return oneEditReplace(firstStr, secondStr)
    elif(len(firstStr)+1 == len(secondStr)):
        return oneEditInsert(firstStr, secondStr)
    elif(len(firstStr)-1 == len(secondStr)):
        return oneEditInsert(secondStr, firstStr)

def oneEditReplace(firstStr,secondStr):
    foundDiffrence = False
    for i in range(len(firstStr)):
        if(firstStr[i] != secondStr[i]):
            if(foundDiffrence):
                return False
            foundDiffrence = True
    return True

def oneEditInsert(str1, str2):
    index1 = 0
    index2 = 0
    while(index1 < len(str1) and index2 < len(str2)):
        if(str1[index1] != str2[index2]):
            if(index1 != index2):
                return False
            index2 +=1
        else:
            index1 +=1
            index2 +=1
    return True

# firstStr = "pale"
# secondStr = "ple"

# firstStr = "pales"
# secondStr = "pale"

# firstStr = "pale"
# secondStr = "bale"

firstStr = "pale"
secondStr = "bae"
print(oneEditAway(firstStr, secondStr))