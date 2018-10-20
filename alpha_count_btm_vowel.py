def get_alphabet_count():
    s = 'hello'
    sindx = eidx = -1
    vowels = ['a', 'e', 'i', 'o', 'u']
    for key,i in enumerate(list(s)):
        if i in vowels:
            if sindx == -1:
                sindx=key
            if sindx > -1:
                eidx = key-1
    tmp = s[sindx:eidx]
    if len(tmp) < 2:
        return -1
    return len(tmp)

print(get_alphabet_count())
