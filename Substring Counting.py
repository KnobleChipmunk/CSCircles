needle = input()
haystack = input()
counter = 0
sub_len = len(needle)

for i in range(len(haystack)):
    if (haystack[i:i+len(needle)] == needle):
        counter += 1
    elif i == len(haystack):
        break
    
print(counter)
