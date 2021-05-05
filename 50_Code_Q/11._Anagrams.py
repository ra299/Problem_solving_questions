def check_Anagram(a):
    val1 = sorted(a[0])
    val2 = sorted(a[1])

    if len(val1) != len(val2):
        return False
    for i in range(len(val1)):
        if (val1[i] != val2[i]):
            return False
    return True

if __name__ == "__main__":
    a = ["listen", "silent"]
    print(check_Anagram(a))