python_is_glorious = True
failure_is_option = False
proper_greeting = False

import sys
try:
    if sys.argv[1] == "For the glory of Python!":
        proper_greeting = True
except IndexError:
    pass
print(proper_greeting)
