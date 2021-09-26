from . import constants

from .internal_functions._get_value import get_value

functions = constants.KEYWORDS

variables = {}

def parse(code):
    code_lines = code.split('\n')

    for line_number in range(len(code_lines)):
        line = code_lines[line_number]
        if line == '':
            continue
        line_split = line.split(':')
        # print(line_split)
        name = line_split[0]
        del line_split[0]
        val_not_convert = ':'.join(line_split)
        if val_not_convert.startswith(' '):
            val_not_convert = val_not_convert[1:]
        value = get_value(val_not_convert, line_number=line_number + 1, variables=variables)
        # print("val", value)
        if name in constants.KEYWORDS:
            if name.startswith(' '):
                name = name[1:]
            
            if name == 'print':
                functions['print'](value)
        else:
            variables[name] = value
