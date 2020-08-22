import collections

def solution(s):
    # build hash map : character and how often it appears
    count = collections.Counter(s) # <-- gives back a dictionary with words occurrence count
                                         #Counter({'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1})
    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1

    '''
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1
'''
#print(solution('akphabet'))
print(solution('aaaabbbccd'))
#print(solution('aaaabbbcc'))