#Solution One, Runtime = O(n*logn)
'''
def listify(string_one, string_two):
    s_list = list()
    k_list = list()

    for letter in string_one:
        s_list.append(letter)

    for letter in string_two:
        k_list.append(letter)

    return (s_list, k_list)

def is_permutation(list_one, list_two):
    list_one.sort()
    list_two.sort()

    i = 0
    while i < len(list_one):
        if list_one[i] != list_two[i]:
            return False

        i += 1

    return True


if __name__ == "__main__":
    s = "program"
    k = "rogramp"

    s_list, k_list = listify(s, k)

    print(is_permutation(s_list, k_list))
'''

#Solution Two, Runtime = O(n)
def create_hashmap(first_string):
    lookup_map = dict()
    for letter in first_string:
        lookup_map[letter] = letter

    return lookup_map


def is_permutation(lookup_map, string_two):
    for letter in string_two:
        if letter not in lookup_map:
            return False

    return True

if __name__ == "__main__":
    s = "program"
    k = "rogramp"

    if len(s) != len(k):
        print(False)
    else:
        print(is_permutation(create_hashmap(s), k))
