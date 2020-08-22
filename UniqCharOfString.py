def uniqchar(s):
    freq = ""
    for i in s:
        if i.lower() not in freq.lower() and i != " ":
            freq = freq + i
        else:
            freq = freq
    return freq

print(uniqchar("Abdul Hameed Bathusha Mohamed Yousuf"))
print(uniqchar("Fathima Irfana Motheyar Ismail Arif"))
print(uniqchar("Shafana Abdul Hameed Bathusha"))
print(uniqchar("Ibrahim Abdul Hameed Bathusha"))