def isPermutationOfPalindrom(phrase): 
    table = []
    table = buildCharFrequencyTable(phrase)
    return checkMaxOneOdd(table)

# No more then one character has an odd count 

def checkMaxOneOdd(table):
    foundOdd = False
    for count in table:
        if(count % 2 == 1):
            if(foundOdd):
                return False
            foundOdd = True
    return True

# map each character to a number a-> 0, b-> 1, c-> 2, etc

def getCharNumber(c):
    a = ord("a")
    z = ord("z")
    val = ord(c)
    if(a <= val and val <=z):
        return (val-a)
    return -1

# count how many time each character will appears

def buildCharFrequencyTable(phrase):
    charVal = ord("z") - ord("a") +1
    table = [0] * charVal
    for c in phrase:
        x = getCharNumber(c)
        if(x != -1):
            table[x] +=1
    print(table)            
    return table


val = "tact123coa"
exp = isPermutationOfPalindrom(val)
print(exp)


# ----------- Another Approch ----------

# def isPermutationOfPalindrom(phrase):
#     countOdd = 0;
#     cal = ord("z") - ord("a") + 1
#     table = [0] * cal
#     for c in phrase:
#         x = getCharNumber(c)
#         if(x != -1):
#             table[x] +=1
#             if(table[x] % 2 == 1):
#                 countOdd +=1
#             else:
#                 countOdd -=1
#     return countOdd <=1

# def getCharNumber(c):
#     a = ord("a")
#     z = ord("z")
#     val = ord(c)
#     if(a <= val and val <=z):
#         return (val-a)
#     return -1

# val = "malayalam"
# exp = isPermutationOfPalindrom(val)
# print(exp)

