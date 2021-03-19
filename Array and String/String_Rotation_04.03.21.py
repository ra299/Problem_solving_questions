def isRotation(s1, s2):
    _len = len(s1)
    if(_len == len(s2) and _len > 0):
        S1s1 = s1 + s1
        return isSubString(S1s1, s2)
    return False

s1 = "waterbottle"
s2 = "erbottlewat"
a =  isRotation(s1, s2)
print(a)
