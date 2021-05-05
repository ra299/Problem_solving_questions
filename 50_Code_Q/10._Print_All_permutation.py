def toString(a):
    return "".join(a)

def permutation(a, l , r):
    if(l == r):
        print(toString(a))
    else:
        for i in range(l, r):
            a[l],a[i] = a[i],a[l]
            permutation(a, l+1, r)
            a[l], a[i] = a[i], a[l]

if __name__ == "__main__":
    string = "ABC"
    n = len(string)
    a = list(string)
    permutation(a, 0, n)