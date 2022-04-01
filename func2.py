def func2(strs,s,str):
    if (s<0 or len(strs)<s):
        print("operation is not possible")
    else:
        strs.insert(s, str)
    return
