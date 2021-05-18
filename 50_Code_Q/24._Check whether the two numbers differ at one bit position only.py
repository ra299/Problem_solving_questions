def isPowerOfTwo(x):
    return x and ( not ( x & ( x - 1 )))
def differ(a,b):
    return isPowerOfTwo(a^b)
if __name__ == "__main__":
    a = 13
    b = 9
    if (differ(a,b)):
        print("Yes")
    else:
        print("No")