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
        pck_duplicates.append(l[index:slice_ind])
        index = idx
    if l[index] == l[index - 1]:
        pck_duplicates[len(pck_duplicates) - 1].append(l[index])
    else:
        pck_duplicates.append(l[:-2:-1])
    return pck_duplicates

print(pack_duplicates(["a","a","a","a","b","c","c","a","a","d","e","e","e","e","f"])) # [['a', 'a', 'a', 'a'], ['b'], ['c', 'c'], ['a', 'a'], ['d'], ['e', 'e', 'e', 'e'], ['f']]
