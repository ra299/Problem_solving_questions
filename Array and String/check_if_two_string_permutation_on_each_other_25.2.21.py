def check(str1, str2):

    no_of_byte = 256
    count1 = [0] * no_of_byte
    count2 = [0] * no_of_byte

    for i in str1:
        count1[ord(i)]+=1
    # print(count1)
    # print(len(count1))

    for i in str2:
        count2[ord(i)]+=1
    # print(count2)
    # print(len(count2))

    if(len(count1) != len(count2)):
        return False

    for i in range(no_of_byte):
        if(count1[i] != count2[i]):
            return False

    return True

str1 = "aac"
str2 = "aca"

if(check(str1, str2)):
    print("It possible")
else:
    print("Not It possible")