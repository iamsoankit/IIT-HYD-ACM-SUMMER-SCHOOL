def sort_by_position(strings, pos, max_pos):
    if ((pos > max_pos) or (len(strings) <= 1)):
        return strings
    table_a = []
    table_c = []
    table_g = []
    table_t = []
    table_none = []
    sorted_strings = []

    for i in range(0, len(strings)):
        if (pos >= len(strings[i])):
            table_none.append(strings[i])
        elif (strings[i][pos] == 'A'):
            table_a.append(strings[i])
        elif (strings[i][pos] == 'C'):
            table_c.append(strings[i])
        elif (strings[i][pos] == 'G'):
            table_g.append(strings[i])
        else:
            table_t.append(strings[i])

    # Make all recursive calls here
    sorted_strings += sort_by_position(table_a, pos + 1, max_pos)
    sorted_strings += sort_by_position(table_c, pos + 1, max_pos)
    sorted_strings += sort_by_position(table_g, pos + 1, max_pos)
    sorted_strings += sort_by_position(table_t, pos + 1, max_pos)
    sorted_strings += table_none

    # Concatenate the sorted tables into the sortedStrings array.
    return sorted_strings

fname = "inputStrings.txt"
with open(fname) as reader:
    lines = reader.readlines()
    strings = [x.strip() for x in lines]

m = 0
for string in strings:
    m = max(m, len(string))

strings = sort_by_position(strings, 0, m - 1)

print('\n')
for string in strings:
    print(string)
