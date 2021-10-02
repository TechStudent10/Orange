from ._error import SyntaxError, VariableNotFound

def get_value(text, variables, line_number=0):
    if text == "":
        return

    if text.startswith('"') and text.endswith('"'):
        return text.lstrip('"').rstrip('"')
    elif text.startswith("'") and text.endswith("'"):
        return text.lstrip("'").rstrip("'")
    else:
        try:
            num = int(text)
            return num
        except ValueError:
            try:
                num = float(text)
                return num
            except ValueError:
                if text in variables:
                    return variables.get(text)
                else:
                    # return VariableNotFound(line_number=line_number)
                    return