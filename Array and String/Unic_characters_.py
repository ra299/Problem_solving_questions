def find(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if(a[i] == a[j]):
                return True
    return False
                

val = input()
if(find(val)):
    print("Yes, this string have repeted charecters")
else:
    print("No, this string havent any repetition")

