pck_duplicates = []


def pack_duplicates(l):
    index = 0
    slice_ind = index
    idx = index
    
    while index < len(l) - 1:
        while l[idx + 1] == l[idx] and idx + 1 <= len(l) - 2:
            slice_ind += 1
            idx += 1
        else:
            slice_ind += 1
            idx += 1
        pck_duplicates.append([l[index], len(l[index:slice_ind])])
        index = idx
    if l[index] == l[index - 1]:
        pck_duplicates[len(pck_duplicates) - 1][1] += 1
    else:
        pck_duplicates.append([l[index], 1])
    return pck_duplicates

print(pack_duplicates(["a","a","a","a","b","c","c","a","a","d","e","e","e","e"])) # [['a', 4], ['b', 1], ['c', 2], ['a', 2], ['d', 1], ['e', 4]]
print(pack_duplicates(["a","a","a","a","b","c","c","a","a","d","e","e","e","e","f","g"])) # [['a', 4], ['b', 1], ['c', 2], ['a', 2], ['d', 1], ['e', 4], ['f', 1], ['g', 1]]
