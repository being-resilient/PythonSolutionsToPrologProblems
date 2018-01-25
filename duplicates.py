dup_removed = []

def duplicates(l):
    for element in l:
        if element not in dup_removed:
            dup_removed.append(element)
    return dup_removed

print(duplicates(["a","a","a","a","b","c","c","a","a","d","e","e","e","e"]))