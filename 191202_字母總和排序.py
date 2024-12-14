def sort_dict(s):
    s_orginaial = [str(i) for i in s.split(' ')]
    s = [str(i).lower() for i in s.split(' ')]
    d = {}
    for i in range(len(s)):
        number = 0
        for j in s[int(i)]:
            number += ord(j)-96
            d[s_orginaial[i]] = number

    return [str(i) for i in dict(sorted(d.items(), key = lambda items:items[1])).keys()]
