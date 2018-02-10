def postalValidate(S):
    X = chr(32)
    S = S.replace(X, '')
    if len(S) != 6:
        return False
    for i in S:
        for n in S:
            if S.isalpha() or S.isdigit():
                return False
            elif S[0].isdigit():
                return False
            elif S[2].isdigit():
                return False
            elif S[4].isdigit():
                return False
            elif S[1].isalpha():
                return False
            elif S[3].isalpha():
                return False
            elif S[5].isdigit() == False:
                return False            
            else:
                 break
        return S.upper()
