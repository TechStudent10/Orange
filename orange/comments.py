# print(new_args)
# print(name)
# print(value)
# if name == 'function':
#     function = {}
#     function_name = val_not_convert.split(',')[0]
#     function_lines = []
#     current_num = line_number + 1
#     current_space_count = 0
#     while 1:
#         function_line = code_lines[current_num]
#         print('func line:', function_line)
#         if len(function_lines) == 0:
#             print('no function lines')
#             space_count = 0
#             print('no space count')
#             for char in function_line:
#                 if char == ' ':
#                     print('char is a space character')
#                     space_count += 1
#                 elif char == '  ':
#                     print('char is a tab character')
#                     space_count += 4

#             current_space_count = space_count
#             print('current space_count:', current_space_count)

#         if function_line.startswith(' '*current_space_count):
#             print('function line starts with space with space count')
#             function_lines.append(function_line.strip(' '*current_space_count))
#         elif function_line.startswith("}"):
#             print('function lines end')
#             break
    
#     function['name'] = function_name
#     function['lines'] = function_lines
#     print(function)
#     functions[function_name] = function
# print(val_not_convert)
# value = get_value(val_not_convert, line_number=line_number + 1, variables=variables)
# print("val", value)

# if name=="blah": print(new_args)
# print(line_split)
# function: functionName, ( name, another ) {
#     print: name
# }
# execute: "functionName", "another"
# from .internal_functions import print
