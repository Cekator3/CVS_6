def func1(strs, s):
    if len(strs) % 2 == 0:
        strs.insert(len(strs)/2, s)
    else:
        strs.insert(len(strs)/2, s)
    return strs

def func2(strs,s,str):
    if (s<0 or len(strs)<s):
        print("operation is not possible")
    else:
        strs.insert(s, str)
    return
