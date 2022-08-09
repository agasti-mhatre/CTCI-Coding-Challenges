def strings_equal(string_one, string_two):
    changes = 1
    i = 0
    while i < len(string_one):
        if string_one[i] != string_two[i]:
            changes -= 1
        
        i += 1

    if changes >= 0:    
        return True
    else:
        return False

def strings_not_equal(string_one, string_two):
    changes = 1
    i = 0
    j = 0
    while (j < len(string_two)) and (i < len(string_one)):
        if string_one[i] != string_two[j]:
            i += 1
            changes -= 1
            continue
        
        i += 1
        j += 1 

    if changes >= 0:    
        return True
    else:
        return False


if __name__ == "__main__":
    string_one = "bakes"
    string_two = "pales"

    if len(string_one) == len(string_two):
        one_away = strings_equal(string_one, string_two)
    elif len(string_one) == (len(string_two) - 1):
        one_away = strings_not_equal(string_two, string_one)
    elif len(string_two) == (len(string_one) - 1):
        one_away = strings_not_equal(string_one, string_two)
    else:
        one_away = False


print(one_away)