# Import all internal functions
from .internal_functions.print import _print
from .internal_functions.input import _input
from .internal_functions.function import function

# Define keywords
KEYWORDS = {
    'print': _print,
    'input': _input,
    'function': function
}
