def compress(_str):
    a = ""
    finalLength = countCompression(_str)
    if(finalLength >= len(_str)):
        return _str
    
    compressed = [0] * finalLength
    countConsecutive = 0
    for i in range(len(_str)):
        countConsecutive +=1
        if( i+1 >= len(_str) or _str[i] != _str[i+1]):
            compressed.append(_str[i])
            compressed.append(countConsecutive)
            countConsecutive = 0
    a = " ".join(map(str, compressed))
    return a

def countCompression(_str):
    compressedLength = 0
    countConsecutive = 0

    for i in range(len(_str)):
        countConsecutive +=1

        if(i+1 >= len(_str) or _str[i] != _str[i+1]):
            compressedLength += 1+ len(countConsecutive)
            countConsecutive = 0
    return compressedLength

_str = "aabcccccaaa"
val = compress(_str)
print(val)