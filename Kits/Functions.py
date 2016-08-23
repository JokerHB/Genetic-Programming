def add(varList):
    sum = 0
    for _ in varList:
        sum += _
    return sum

def sub(varList):
    ans = varList[0]
    for _ in varList[1:]:
        ans -= _
    return ans

def mul(varList):
    ans = 1
    for _ in varList:
        ans *= _
    return ans

def mod(varList):
    ans = varList[0]
    for _ in varList[1:]:
        if _ == 0:
            ans %= 1
        else:
            ans %= _
    return ans

def fitnessFnc(varList):
    pass
