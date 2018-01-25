new_flattened = []

def flatten(l):
    for element in l:
        if isinstance(element, list):
            flatten(element)
        else:
            new_flattened.append(element)
    return new_flattened

print(flatten([a, [b, [c, d], e]])) # ['a', 'b', 'c', 'd', 'e']
print(flatten(["a", ["b", ["c",["s", "d", "e", ["w", "k"]] ,"d"], "e"]])) # ['a', 'b', 'c', 's', 'd', 'e', 'w', 'k', 'd', 'e']
