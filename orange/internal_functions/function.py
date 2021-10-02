from ._get_scope import get_scope

def function(args, variables, lines, line_number, functions):
    line = lines[line_number]
    function_lines = get_scope(lines, line_number)
    line_split = line.split(':')
    del line_split[0]
    if line_split[0].startswith(' '):
        line_split[0] = line_split[0][1:]

    new_line = line_split[0].split(' ')
    func_name = new_line[0]
    del new_line[0]
    func_args = ' '.join(new_line).lstrip('(').rstrip(')')
    func_args_list = func_args.split(",")
    new_args = []
    for arg in func_args_list:
        new_arg = arg
        if new_arg.startswith(' '):
            new_arg = new_arg[1:]

        new_args.append(new_arg)

    functions[func_name] = {
        'name': func_name,
        'args': new_args
    }
    print(functions)
