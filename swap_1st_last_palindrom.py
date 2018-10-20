def pali():
    s = "me and mom asked uncle to meet dad python"
    res = s.split(" ")
    start = end = -1
    for k, i in enumerate(res):
        if i == i[::-1]:
            if start == -1:
                start = k
            if start != -1:
                end = k
    temp = res[start]
    res[start] = res[end]
    res[end] = temp
    print(" ".join(res))
pali()
