# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def solution(x):

    if isinstance(x,float):
        sf = repr(x)
        p, q = sf.split('.')
        if p[0] == '-':
            return float('-' + p[:0:-1] + '.' +q[::-1])
        else:
            return float(p[::-1] + '.' +q[::-1])

    if isinstance(x,int):
        si = str(x)
        if si[0] == '-':
            return int('-' + si[:0:-1])
        else:
            return int(si[::-1])

    else:
        return "Enter Valid Number"

print(solution(-321))
print(solution("abdul"))
print(solution("12abdul12"))
print(solution(345))
print(solution(345.67))
print(solution(-345.67))
print(solution("-123.45"))
print(solution(0))
print(solution(-0))
print(solution(0.00))
print(solution(-0.000))