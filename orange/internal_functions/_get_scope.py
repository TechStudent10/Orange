import string

chars = string.ascii_letters + string.digits + "!@#$%^&*()_-=+[{]}\|;:'\"<,.>/?`~"

possible_scope_names = [
    'function'
]

def lindexsplit(some_list, *args):
    if args:
        args = (0,) + tuple(data+1 for data in args) + (len(some_list)+1,)

    my_list = []
    for start, end in zip(args, args[1:]):
        my_list.append(some_list[start:end])
    return my_list

def get_scope(lines, line_number):
    spaces = ""
    first_line = lines[line_number + 1]
    new_line = first_line
    for line_char in new_line:
        if line_char == ' ':
            spaces += ' '
        elif line_char in chars:
            break

    # print(new_line)

    # print('space count:', len(spaces))

    lines_split = lindexsplit(lines, line_number + 3)
    # print("split", lines_split[0])
    scope_lines = []
    in_scope = False
    for line in lines_split[0]:
        if line.split(':')[0] in possible_scope_names:
            in_scope = True
            continue
        if in_scope:
            # print("yeet", line)
            if line.startswith(spaces):
                scope_lines.append(line.lstrip(spaces))
            else:
                in_scope = False
                break

    return scope_lines

# print(lindexsplit(["oh yes", "no", "yeep", "jeep", "what", "hu", "hoi", "boi", "boi0", "boi1", "boi2", "boi3"], 3)[1])