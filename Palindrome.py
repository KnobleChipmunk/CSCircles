def isPalindrome(S):
    h = int((len(S)) / 2)
    if S[0:h] == S[:h-1:-1] and len(S) % 2 == 0:
        return True
    elif S[0:h] == S[:h:-1] and len(S) % 2 != 0:
        return True
    else:
        return False
