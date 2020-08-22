sentence = "Hi,... I am Abdul-Hameed Bathusha!.."

def avgwordlen(x):
    for i in ",.!-":
        x = x.replace(i,'')
    words = x.split()
    return round(sum(len(word) for word in words) / len(words), 2)

print(avgwordlen(sentence))
