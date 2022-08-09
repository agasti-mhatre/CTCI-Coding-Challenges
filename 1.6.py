def count_characters(a_string):
    list_string = []
    i = 0
    j = 0
    count = 1
    compressed_string = "" 
    while i < len(a_string):
        j = i + 1
        if j < len(a_string):
            if a_string[i] == a_string[j]:
                count += 1
            else:
                list_string.append("{}{}".format(a_string[i], str(count)))
                count = 1
        else:
            list_string.append("{}{}".format(a_string[i], str(count)))

        i += 1

    compressed_string = "".join(list_string)

    if len(compressed_string) < len(a_string):
        return compressed_string
    else:
        return a_string



if __name__ == "__main__":
    the_string = "aabcccccaaa"

    print(count_characters(the_string))
