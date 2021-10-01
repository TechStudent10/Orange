from .internal_functions._get_value import get_value
from .keywords import KEYWORDS

variables = {}
functions = {}

def parse(code):
    code_lines = code.split('\n')

    for line_number in range(len(code_lines)):
        line = code_lines[line_number]
        if line == '':
            continue
        line_split = line.split(':')
        name = line_split[0]
        if name.startswith('#'):
            continue

        del line_split[0]
        val_not_convert = ':'.join(line_split)
        args = val_not_convert.split(',')
        new_args = []
        for arg in args:
            if arg.startswith(' '):
                arg = arg[1:]

            new_arg = get_value(arg, variables=variables, line_number=line_number)
            new_args.append(new_arg)

        
        if val_not_convert.startswith(' '):
            val_not_convert = val_not_convert[1:]
        
        val_not_convert = ',' + val_not_convert
        if name in KEYWORDS:
            if name.startswith(' '):
                name = name[1:]
            
            KEYWORDS[name](new_args, variables=variables)
        else:
            variables[name] = ' '.join(new_args)
