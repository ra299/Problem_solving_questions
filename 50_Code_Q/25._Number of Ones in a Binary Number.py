def decToBinary(num):
    arr = []
    if num >= 1:
        decToBinary(num//2)
    print(num % 2, end = "")
    temp = num % 2
    arr.append(temp)
    return arr

def toCountOne(num):
    if (num == 0):
        return 0
    return 1 + toCountOne(num & (num -1))

if __name__ == "__main__":
    value = 8
    print(toCountOne(value))
    catch = decToBinary(value)
    print(catch)
