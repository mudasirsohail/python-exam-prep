import streamlit as st

questions = [
    {
        "question": "What type of error is raised by 10 / 0?",
        "options": ["ValueError", "ZeroDivisionError", "IndexError", "ArithmeticError"],
        "answer": "ZeroDivisionError"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "What is the output of `print(type([]))`?",
        "options": ["<class 'list'>", "<class 'array'>", "<class 'tuple'>", "<class 'dict'>"],
        "answer": "<class 'list'>"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["^", "*", "**", "^^"],
        "answer": "**"
    },
    {
        "question": "What is the result of `'Hello'.lower()`?",
        "options": ["hello", "HELLO", "Hello", "hELLO"],
        "answer": "hello"
    },
    {
        "question": "How to create a virtual environment in Python?",
        "options": ["venv", "virtualenv", "pyenv", "All of these"],
        "answer": "All of these"
    },
    {
        "question": "Which method is used to add an element to a list?",
        "options": ["append()", "add()", "insert()", "push()"],
        "answer": "append()"
    },
    {
        "question": "What is the purpose of `__init__` method?",
        "options": ["Class destructor", "Object initializer", "Module importer", "Exception handler"],
        "answer": "Object initializer"
    },
    {
        "question": "Which of these is NOT a valid variable name?",
        "options": ["my_var", "_var", "var3", "3var"],
        "answer": "3var"
    },
    {
        "question": "What does the `break` keyword do?",
        "options": ["Pause program", "Exit loop", "Skip iteration", "Handle errors"],
        "answer": "Exit loop"
    },
    {
        "question": "Which collection is ordered and unchangeable?",
        "options": ["list", "set", "tuple", "dict"],
        "answer": "tuple"
    },
    {
        "question": "What is the output of `bool('False')`?",
        "options": ["True", "False", "Error", "None"],
        "answer": "True"
    },
    {
        "question": "Which module is used for regular expressions?",
        "options": ["re", "regex", "pyre", "string"],
        "answer": "re"
    },
    {
        "question": "What is the result of `3 * 'a'`?",
        "options": ["aaa", "3a", "TypeError", "a3"],
        "answer": "aaa"
    },
    {
        "question": "Which method returns a dictionary's keys?",
        "options": ["keys()", "items()", "values()", "all()"],
        "answer": "keys()"
    },
    {
        "question": "What does `open('file.txt', 'w')` do?",
        "options": ["Read file", "Write file", "Append file", "Delete file"],
        "answer": "Write file"
    },
    {
        "question": "Which is used for floating point division?",
        "options": ["/", "//", "%", "**"],
        "answer": "/"
    },
    {
        "question": "What is `sys.argv` used for?",
        "options": ["System arguments", "File handling", "Math operations", "GUI creation"],
        "answer": "System arguments"
    },
    {
        "question": "Which decorator is used for class methods?",
        "options": ["@classmethod", "@staticmethod", "@method", "@classfunc"],
        "answer": "@classmethod"
    },
    {
        "question": "What does `'a' in {'a': 1}` return?",
        "options": ["True", "False", "1", "KeyError"],
        "answer": "True"
    },
        {
        "question": "Which of the following is NOT a feature of Python bytecode?",
        "options": [
            "Platform-independent",
            "Requires a Python interpreter to run",
            "Can be executed without any interpreter",
            "Stored in `.pyc` files"
        ],
        "answer": "Can be executed without any interpreter"
    },
    {
        "question": "What will be the output of the following code:\n\nx: int = 100\nprint(x.bit_length())",
        "options": [
            "Error due to incorrect type hinting",
            "Prints the number of bits required to represent 100",
            "Prints the value 100",
            "Raises a runtime error"
        ],
        "answer": "Prints the number of bits required to represent 100"
    },
    {
        "question": "In Python, what is the main purpose of the `dis` module?",
        "options": [
            "To decode strings",
            "To display variable types",
            "To disassemble Python bytecode",
            "To disable functions"
        ],
        "answer": "To disassemble Python bytecode"
    },
    {
        "question": "Why is indentation mandatory in Python?",
        "options": [
            "It helps with auto-completion",
            "It makes the program shorter",
            "It defines code blocks and structure",
            "It’s only required in loops"
        ],
        "answer": "It defines code blocks and structure"
    },
    {
        "question": "Which of the following demonstrates Duck Typing in Python?",
        "options": [
            "Defining types with `int`, `str`, etc.",
            "Checking object type before calling a method",
            "Calling a method without checking type, assuming it exists",
            "Using `isinstance()` to verify types"
        ],
        "answer": "Calling a method without checking type, assuming it exists"
    },
    {
        "question": "What is true about Python being dynamically typed?",
        "options": [
            "All types must be declared before execution",
            "Variables change their types only during compilation",
            "Type is determined at runtime",
            "Python does not support type hinting"
        ],
        "answer": "Type is determined at runtime"
    },
    {
        "question": "Which command compiles a Python file into bytecode?",
        "options": [
            "python compile Test.py",
            "python -m compileall Test.py",
            "compile Test.py",
            "python3 --bytecode Test.py"
        ],
        "answer": "python -m compileall Test.py"
    },
    {
        "question": "What is the role of the `__pycache__` folder?",
        "options": [
            "Stores logs of previous executions",
            "Caches web data",
            "Stores compiled bytecode (.pyc files)",
            "Stores class definitions"
        ],
        "answer": "Stores compiled bytecode (.pyc files)"
    },
    {
        "question": "Which of the following features is NOT fully supported in object-based languages?",
        "options": [
            "Encapsulation",
            "Object creation",
            "Inheritance",
            "Method definition"
        ],
        "answer": "Inheritance"
    },
    {
        "question": "In this example, what concept is being shown?\n\ndef call_function(func, name) -> str:\n    return func(name)",
        "options": [
            "Object-oriented programming",
            "Dynamic typing",
            "First-class functions",
            "Bytecode compilation"
        ],
        "answer": "First-class functions"
    },
    {
        "question": "What is the correct output of this code?\n\nage: int = input(\"Enter your age: \")\nprint(\"type(age) =\", type(age))",
        "options": [
            "<class 'int'>",
            "<class 'str'>",
            "Error due to type mismatch",
            "No output"
        ],
        "answer": "<class 'str'>"
    },
    {
        "question": "What does Python do during Lexical Analysis phase of compilation?",
        "options": [
            "Converts code into bytecode",
            "Breaks code into tokens like keywords and identifiers",
            "Optimizes the code for memory usage",
            "Runs the program line by line"
        ],
        "answer": "Breaks code into tokens like keywords and identifiers"
    },
    {
        "question": "Which of the following is NOT true about Python bytecode?",
        "options": [
            "It is stored in `.pyc` files",
            "It is tied to a specific CPU architecture like x86",
            "It is executed by the Python interpreter",
            "It can be found in the `__pycache__` folder"
        ],
        "answer": "It is tied to a specific CPU architecture like x86"
    },
    {
        "question": "What happens if you mix tabs and spaces in Python indentation?",
        "options": [
            "Code runs faster",
            "It improves readability",
            "SyntaxError occurs",
            "Python ignores indentation style"
        ],
        "answer": "SyntaxError occurs"
    },
    {
        "question": "Why is Python ideal for Agentic AI applications, according to the lesson?",
        "options": [
            "Because it supports only procedural programming",
            "Because it’s a compiled language",
            "Due to its rich ecosystem and ability to integrate NLP, RL, and automation",
            "Because it works only on Windows"
        ],
        "answer": "Due to its rich ecosystem and ability to integrate NLP, RL, and automation"
    },
    {
        "question": "Which of the following is NOT a feature of Python bytecode?",
        "options": [
            "Platform-independent",
            "Requires a Python interpreter to run",
            "Can be executed without any interpreter",
            "Stored in .pyc files"
        ],
        "answer": "Can be executed without any interpreter"
    },
    {
        "question": "What will be the output of the following code?\n\nx: int = 100 \nprint(x.bit_length())",
        "options": [
            "Error due to incorrect type hinting",
            "Prints the number of bits required to represent 100",
            "Prints the value 100",
            "Raises a runtime error"
        ],
        "answer": "Prints the number of bits required to represent 100"
    },
    {
        "question": "In Python, what is the main purpose of the dis module?",
        "options": [
            "To decode strings",
            "To display variable types",
            "To disassemble Python bytecode",
            "To disable functions"
        ],
        "answer": "To disassemble Python bytecode"
    },
    {
        "question": "Why is indentation mandatory in Python?",
        "options": [
            "It helps with auto-completion",
            "It makes the program shorter",
            "It defines code blocks and structure",
            "It’s only required in loops"
        ],
        "answer": "It defines code blocks and structure"
    },
    {
        "question": "Which of the following demonstrates Duck Typing in Python?",
        "options": [
            "Defining types with int, str, etc.",
            "Checking object type before calling a method",
            "Calling a method without checking type, assuming it exists",
            "Using isinstance() to verify types"
        ],
        "answer": "Calling a method without checking type, assuming it exists"
    },
    {
        "question": "What is true about Python being dynamically typed?",
        "options": [
            "All types must be declared before execution",
            "Variables change their types only during compilation",
            "Type is determined at runtime",
            "Python does not support type hinting"
        ],
        "answer": "Type is determined at runtime"
    },
    {
        "question": "Which command compiles a Python file into bytecode?",
        "options": [
            "python compile Test.py",
            "python -m compileall Test.py",
            "compile Test.py",
            "python3 --bytecode Test.py"
        ],
        "answer": "python -m compileall Test.py"
    },
    {
        "question": "What is the role of the __pycache__ folder?",
        "options": [
            "Stores logs of previous executions",
            "Caches web data",
            "Stores compiled bytecode (.pyc files)",
            "Stores class definitions"
        ],
        "answer": "Stores compiled bytecode (.pyc files)"
    },
    {
        "question": "Which of the following features is NOT fully supported in object-based languages?",
        "options": [
            "Encapsulation",
            "Object creation",
            "Inheritance",
            "Method definition"
        ],
        "answer": "Inheritance"
    },
    {
        "question": "In this example, what concept is being shown?\n\ndef call_function(func, name) -> str:\n    return func(name)",
        "options": [
            "Object-oriented programming",
            "Dynamic typing",
            "First-class functions",
            "Bytecode compilation"
        ],
        "answer": "First-class functions"
    },
    {
        "question": "What is the correct output of this code?\n\nage: int = input(\"Enter your age: \")\nprint(\"type(age) =\", type(age))",
        "options": [
            "<class 'int'>",
            "<class 'str'>",
            "Error due to type mismatch",
            "No output"
        ],
        "answer": "<class 'str'>"
    },
    {
        "question": "What does Python do during Lexical Analysis phase of compilation?",
        "options": [
            "Converts code into bytecode",
            "Breaks code into tokens like keywords and identifiers",
            "Optimizes the code for memory usage",
            "Runs the program line by line"
        ],
        "answer": "Breaks code into tokens like keywords and identifiers"
    },
    {
        "question": "Which of the following is NOT true about Python bytecode?",
        "options": [
            "It is stored in .pyc files",
            "It is tied to a specific CPU architecture like x86",
            "It is executed by the Python interpreter",
            "It can be found in the __pycache__ folder"
        ],
        "answer": "It is tied to a specific CPU architecture like x86"
    },
    {
        "question": "What happens if you mix tabs and spaces in Python indentation?",
        "options": [
            "Code runs faster",
            "It improves readability",
            "SyntaxError occurs",
            "Python ignores indentation style"
        ],
        "answer": "SyntaxError occurs"
    },
    {
        "question": "Why is Python ideal for Agentic AI applications, according to the lesson?",
        "options": [
            "Because it supports only procedural programming",
            "Because it’s a compiled language",
            "Due to its rich ecosystem and ability to integrate NLP, RL, and automation",
            "Because it works only on Windows"
        ],
        "answer": "Due to its rich ecosystem and ability to integrate NLP, RL, and automation"
    },
    {
        "question": "Which of the following is NOT a numeric type in Python?",
        "options": ["float", "complex", "char", "int"],
        "answer": "char"
    },
    {
        "question": "What is the output of type(3 + 4j) in Python?",
        "options": ["<class 'int'>", "<class 'complex'>", "<class 'float'>", "<class 'number'>"],
        "answer": "<class 'complex'>"
    },
    {
        "question": "Which attribute returns the real part of a complex number z = 2 + 3j?",
        "options": ["z.realpart", "real(z)", "z.real", "z.re"],
        "answer": "z.real"
    },
    {
        "question": "Which of the following is a valid Boolean value in Python?",
        "options": ["Yes", "False", "No", "Off"],
        "answer": "False"
    },
    {
        "question": "Which of the following string definitions is used for multi-line text?",
        "options": ["'Hello'", "\"Hello\"", "'''Hello'''", "\"Hello'Python\""],
        "answer": "'''Hello'''"
    },
    {
        "question": "Which of these Python types is immutable?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "answer": "Tuple"
    },
    {
        "question": "What does the expression range(1, 10, 2) generate?",
        "options": ["1 to 10 in steps of 1", "1 to 9 in steps of 2", "1 to 9 in steps of 1", "2 to 10 in steps of 2"],
        "answer": "1 to 9 in steps of 2"
    },
    {
        "question": "Which of the following collections only allows unique elements?",
        "options": ["List", "Set", "Tuple", "Dictionary"],
        "answer": "Set"
    },
    {
        "question": "What is the correct data type for {\"name\": \"Ali\", \"age\": 25}?",
        "options": ["List", "Set", "Tuple", "Dictionary"],
        "answer": "Dictionary"
    },
    {
        "question": "Which of the following is an immutable binary type?",
        "options": ["bytearray", "bytes", "set", "memoryview"],
        "answer": "bytes"
    },
    {
        "question": "What does the method decode('utf-8') do on a bytearray?",
        "options": ["Encodes the data", "Converts it to integer", "Converts bytes to string", "Deletes the bytes"],
        "answer": "Converts bytes to string"
    },
    {
        "question": "Which of the following returns the memory address of an object?",
        "options": ["mem_address()", "location()", "id()", "addr()"],
        "answer": "id()"
    },
    {
        "question": "In Python, None is equivalent to which of the following in Boolean context?",
        "options": ["True", "\"null\"", "1", "False"],
        "answer": "False"
    },
    {
        "question": "Which of the following is NOT a falsy value in Python?",
        "options": ["None", "0", "\" \"", "[]"],
        "answer": "\" \""
    },
    {
        "question": "Which function is used to check if a variable belongs to a specific data type?",
        "options": ["type_of()", "isinstance()", "checktype()", "typeof()"],
        "answer": "isinstance()"
    },
    {
        "question": "What is an operand in Python?",
        "options": ["A symbol like + or -", "A value or variable that an operator acts on", "A special keyword", "A statement"],
        "answer": "A value or variable that an operator acts on"
    },
    {
        "question": "Which of the following is a unary operator?",
        "options": ["+", "-", "*", "=="],
        "answer": "-"
    },
    {
        "question": "Which of the following is a binary operator?",
        "options": ["+", "not", "~", "-"],
        "answer": "+"
    },
    {
        "question": "What does not True evaluate to?",
        "options": ["True", "False", "Error", "None"],
        "answer": "False"
    },
    {
        "question": "Which operator is used to invert bits in Python?",
        "options": ["!", "not", "~", "--"],
        "answer": "~"
    },
    {
        "question": "What does 5 // 2 return in Python?",
        "options": ["2.5", "2", "0", "1"],
        "answer": "2"
    },
    {
        "question": "Which operator returns the remainder?",
        "options": ["/", "//", "%", "**"],
        "answer": "%"
    },
    {
        "question": "What is the result of 2 ** 3?",
        "options": ["5", "6", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Which operator checks if two values are equal?",
        "options": ["==", "=", "is", "equals"],
        "answer": "=="
    },
    {
        "question": "What does != mean?",
        "options": ["Assignment", "Not equal", "Less than", "Modulus"],
        "answer": "Not equal"
    },
    {
        "question": "What will True and False return?",
        "options": ["False", "True", "None", "Error"],
        "answer": "False"
    },
    {
        "question": "Which is a logical OR operation?",
        "options": ["and", "or", "not", "xor"],
        "answer": "or"
    },
    {
        "question": "Which of the following is an assignment operator?",
        "options": ["=", "==", ":=", "+"],
        "answer": "="
    },
    {
        "question": "What does x += 3 mean?",
        "options": ["x = 3", "x = x + 3", "x =+ 3", "x == 3"],
        "answer": "x = x + 3"
    },
    {
        "question": "What is the walrus operator used for?",
        "options": ["Loops", "Assignment and evaluation", "Comparison", "Multiplication"],
        "answer": "Assignment and evaluation"
    },
    {
        "question": "What does is compare?",
        "options": ["Value", "Memory location", "Type", "Length"],
        "answer": "Memory location"
    },
    {
        "question": "Which of the following returns True for same reference?",
        "options": ["x is y", "x == y", "x = y", "x !== y"],
        "answer": "x is y"
    },
    {
        "question": "What does in operator do?",
        "options": ["Adds elements", "Checks membership", "Compares length", "Sorts list"],
        "answer": "Checks membership"
    },
    {
        "question": "What does not in check?",
        "options": ["Identity", "Type", "Non-membership", "Truth value"],
        "answer": "Non-membership"
    },
    {
        "question": "Which of the following will be True?\nmy_list = [1, 2, 3]\n2 in my_list",
        "options": ["True", "False", "Error", "None"],
        "answer": "True"
    },
     {
        "question": "What are keywords in Python?",
        "options": ["User-defined variables", "Reserved words with special meanings", "Loops", "Print statements"],
        "answer": "Reserved words with special meanings"
    },
    {
        "question": "Can keywords be used as variable names?",
        "options": ["Yes", "No", "Sometimes", "Only inside functions"],
        "answer": "No"
    },
    {
        "question": "Which of the following is a Python keyword?",
        "options": ["func", "variable", "return", "assign"],
        "answer": "return"
    },
    {
        "question": "Which module helps to list all Python keywords?",
        "options": ["os", "sys", "keyword", "builtins"],
        "answer": "keyword"
    },
    {
        "question": "What is the correct way to define a variable?",
        "options": ["int x = 5", "x = 5", "var x = 5", "define x 5"],
        "answer": "x = 5"
    },
    {
        "question": "Which is an invalid variable name?",
        "options": ["_age", "name_1", "1name", "userName"],
        "answer": "1name"
    },
    {
        "question": "Which character is not allowed in a variable name?",
        "options": ["_", "digit", "-", "letter"],
        "answer": "-"
    },
    {
        "question": "Which of the following is case-sensitive in Python?",
        "options": ["Keywords only", "Variable names", "Functions only", "None"],
        "answer": "Variable names"
    },
    {
        "question": "What does del x do in Python?",
        "options": ["Hides x", "Renames x", "Deletes x from memory", "Unassigns type only"],
        "answer": "Deletes x from memory"
    },
    {
        "question": "Which naming style is recommended for variables and functions in Python?",
        "options": ["camelCase", "snake_case", "PascalCase", "kebab-case"],
        "answer": "snake_case"
    },
    {
        "question": "What is __init__ an example of?",
        "options": ["Global function", "Special method", "Constant", "Mangled variable"],
        "answer": "Special method"
    },
    {
        "question": "Which of the following is a constant naming style?",
        "options": ["pi = 3.14", "PI = 3.14", "Pi = 3.14", "piNum = 3.14"],
        "answer": "PI = 3.14"
    },
    {
        "question": "What is the correct way to define a multi-line string in Python?",
        "options": ["\"Hello, World!\"", "'''Hello, World!'''", "Hello, World!", "“Hello, World!”"],
        "answer": "'''Hello, World!'''"
    },
    {
        "question": "What is the output of print(r'Hello\\tWorld')?",
        "options": ["Hello World", "Hello\\tWorld", "Error", "Hello World"],
        "answer": "Hello\\tWorld"
    },
    {
        "question": "Strings in Python are:",
        "options": ["Mutable", "Immutable", "Changeable", "Variable"],
        "answer": "Immutable"
    },
    {
        "question": "Which escape sequence represents a tab space?",
        "options": ["\\n", "\\t", "\\b", "\\r"],
        "answer": "\\t"
    },
    {
        "question": "What does \\u0041 represent?",
        "options": ["Unicode character A", "Hexadecimal 41", "Newline character", "None"],
        "answer": "Unicode character A"
    },
    {
        "question": "What is the result of 'Hello' + 'World'?",
        "options": ["Hello World", "HelloWorld", "Hello+World", "Error"],
        "answer": "HelloWorld"
    },
    {
        "question": "What is the output of 'Python'[0]?",
        "options": ["y", "P", "o", "Error"],
        "answer": "P"
    },
    {
        "question": "What is the result of len(' Hello ')?",
        "options": ["6", "7", "8", "5"],
        "answer": "7"
    },
    {
        "question": "What does .upper() do to a string?",
        "options": ["Converts to lowercase", "Converts to uppercase", "Capitalizes", "Swaps case"],
        "answer": "Converts to uppercase"
    },
    {
        "question": "What is the result of 'Hello, World!'.split('l')?",
        "options": ["['He', '', 'o, Wor', 'd!']", "['Hello', 'World']", "['He', 'o']", "['H', 'e', 'l', 'l', 'o']"],
        "answer": "['He', '', 'o, Wor', 'd!']"
    },
    {
        "question": "Which method replaces a substring?",
        "options": ["change()", "edit()", "replace()", "update()"],
        "answer": "replace()"
    },
    {
        "question": "What is the result of 'Python'.count('o')?",
        "options": ["2", "1", "0", "3"],
        "answer": "1"
    },
    {
        "question": "Which method joins list items with a string separator?",
        "options": ["merge()", "glue()", "join()", "attach()"],
        "answer": "join()"
    },
    {
        "question": "The find() method returns:",
        "options": ["Boolean value", "Index of first occurrence", "Total count", "Error if not found"],
        "answer": "Index of first occurrence"
    },
    {
        "question": "What is returned by 'Hello'.find('x')?",
        "options": ["0", "Error", "-1", "None"],
        "answer": "-1"
    },
    {
        "question": "What does %d format in a string?",
        "options": ["Decimal (Integer)", "Floating-point", "Character", "String"],
        "answer": "Decimal (Integer)"
    },
    {
        "question": "What is the modern and recommended way of string formatting?",
        "options": ["%", ".format()", "f-strings", "Template"],
        "answer": "f-strings"
    },
    {
        "question": "What is the output of f\"My name is {'Ali'}\"?",
        "options": ["My name is Ali", "f\"My name is Ali\"", "Error", "My name is 'Ali'"],
        "answer": "My name is Ali"
    },
    {
        "question": "What will happen if placeholders and variables mismatch in formatting?",
        "options": ["Nothing", "Error", "Zero output", "All placeholders ignored"],
        "answer": "Error"
    },
    {
        "question": "str.format() uses:",
        "options": ["Positional and keyword arguments", "Only keyword arguments", "Only position", "No arguments"],
        "answer": "Positional and keyword arguments"
    },
    {
        "question": "What is interning in Python?",
        "options": ["Importing modules", "Sharing memory for identical strings", "Declaring variables", "Casting types"],
        "answer": "Sharing memory for identical strings"
    },
    {
        "question": "Which strings are automatically interned?",
        "options": ["Long strings", "Identifiers and short strings", "Numbers only", "Dynamically created strings"],
        "answer": "Identifiers and short strings"
    },
    {
        "question": "Which function forces interning?",
        "options": ["str.intern()", "force()", "sys.intern()", "intern()"],
        "answer": "sys.intern()"
    },
    {
        "question": "Dynamically created strings are:",
        "options": ["Automatically interned", "Stored in string pool", "Not interned by default", "Always immutable"],
        "answer": "Not interned by default"
    },
    {
        "question": "a = 'hello'; b = 'hello' → a is b returns?",
        "options": ["False", "Error", "True", "Depends on length"],
        "answer": "True"
    },
    {
        "question": "What is implicit type casting?",
        "options": ["Manually changing type", "Changing types at runtime", "Automatically converting compatible types", "Converting to string"],
        "answer": "Automatically converting compatible types"
    },
    {
        "question": "What is the output of int('123')?",
        "options": ["'123'", "123", "Error", "12.3"],
        "answer": "123"
    },
    {
        "question": "What does float('3.14') return?",
        "options": ["3", "3.14", "'3.14'", "Error"],
        "answer": "3.14"
    },
    {
        "question": "What is the output of bool('')?",
        "options": ["True", "False", "Error", "0"],
        "answer": "False"
    },
    {
        "question": "What is the result of list(('a', 'b'))?",
        "options": ["('a', 'b')", "{'a', 'b'}", "['a', 'b']", "Error"],
        "answer": "['a', 'b']"
    },
    {
        "question": "What does the if statement do in Python?",
        "options": ["Loops through a list", "Executes code based on a condition", "Compares two values", "Defines a function"],
        "answer": "Executes code based on a condition"
    },
    {
        "question": "Which of the following is a correct comparison operator?",
        "options": ["=>", "=!", "!=", "equal"],
        "answer": "!="
    },
    {
        "question": "What is the output of: 5 > 3 and 2 < 4?",
        "options": ["False", "True", "Error", "None"],
        "answer": "True"
    },
    {
        "question": "What does not do in Python?",
        "options": ["Converts value to int", "Repeats loop", "Reverses a condition", "Ends a loop"],
        "answer": "Reverses a condition"
    },
    {
        "question": "What is the output of this code? num = -2 if num > 0: print('Positive') else: print('Not positive')",
        "options": ["Positive", "Not positive", "0", "Error"],
        "answer": "Not positive"
    },
    {
        "question": "The elif keyword is used:",
        "options": ["Instead of if", "For infinite loop", "For multiple conditions", "For error handling"],
        "answer": "For multiple conditions"
    },
    {
        "question": "Which of the following is not a valid logical operator?",
        "options": ["and", "or", "xor", "not"],
        "answer": "xor"
    },
    {
        "question": "In a nested if, when is the inner if executed?",
        "options": ["Always", "Only if outer condition is False", "Only if outer condition is True", "It is ignored"],
        "answer": "Only if outer condition is True"
    },
    {
        "question": "In Python 3.10+, which structure simplifies if-elif chains?",
        "options": ["match-case", "switch", "loop-case", "match-if"],
        "answer": "match-case"
    },
    {
        "question": "What is the wildcard/default case in match-case?",
        "options": ["else", "_", "None", "default"],
        "answer": "_"
    },
    {
        "question": "What does a for loop do?",
        "options": ["Repeats code based on a condition", "Repeats code for each item in a sequence", "Defines a function", "Declares variables"],
        "answer": "Repeats code for each item in a sequence"
    },
    {
        "question": "What will range(5) generate?",
        "options": ["[0, 1, 2, 3, 4]", "[1, 2, 3, 4, 5]", "[0, 2, 4, 6, 8]", "Infinite numbers"],
        "answer": "[0, 1, 2, 3, 4]"
    },
    {
        "question": "What does the while loop require?",
        "options": ["List", "Range", "Condition", "Tuple"],
        "answer": "Condition"
    },
    {
        "question": "What is the output of the following code? for i in range(3): print('Hi')",
        "options": ["Hi Hi Hi", "Hi 3", "0 1 2", "Error"],
        "answer": "Hi Hi Hi"
    },
    {
        "question": "What does the break keyword do?",
        "options": ["Skips one iteration", "Continues to next loop", "Stops the loop", "Reverses the loop"],
        "answer": "Stops the loop"
    },
    {
        "question": "What is the function of continue?",
        "options": ["Terminates loop", "Skips the current iteration", "Restarts program", "Ends if-else block"],
        "answer": "Skips the current iteration"
    },
    {
        "question": "A loop inside another loop is called:",
        "options": ["Inner loop", "Duplicate loop", "Nested loop", "Double loop"],
        "answer": "Nested loop"
    },
    {
        "question": "How many times will the inner loop run? for i in range(2): for j in range(3): print(i, j)",
        "options": ["2", "3", "6", "5"],
        "answer": "6"
    },
    {
        "question": "Which loop should you use when the number of iterations is unknown?",
        "options": ["for", "range", "while", "switch"],
        "answer": "while"
    },
    {
        "question": "What is the result of for _ in range(3): print(_)?",
        "options": ["Error", "0 0 0", "0 1 2", "None"],
        "answer": "0 1 2"
    },
    {
        "question": "When does the else block of a for loop run?",
        "options": ["Only if loop breaks", "Always", "Only if loop finishes without break", "Only if a condition is False"],
        "answer": "Only if loop finishes without break"
    },
    {
        "question": "What will this code print? for i in range(3): if i == 1: break else: print('Done')",
        "options": ["Done", "Nothing", "i values", "Error"],
        "answer": "Nothing"
    },
    {
        "question": "What is the output of: for i in range(3): print(i) else: print('Finished')",
        "options": ["0 1 2", "0 1 2 Finished", "Finished", "Nothing"],
        "answer": "0 1 2 Finished"
    },
    {
        "question": "Which keyword skips the current iteration but continues the loop?",
        "options": ["stop", "skip", "break", "continue"],
        "answer": "continue"
    },
    {
        "question": "Which loop is ideal for iterating a known number of times?",
        "options": ["while", "for", "if", "elif"],
        "answer": "for"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["^", "**", "//", "%"],
        "answer": "**"
    },
    {
        "question": "What will be returned for grading_system(85) in the given grading function?",
        "options": ["A+", "A", "B", "C"],
        "answer": "A"
    },
    {
        "question": "What will grading_system(45) return?",
        "options": ["C", "D", "F", "Invalid"],
        "answer": "F"
    },
    {
        "question": "What does calculator() function do in the example?",
        "options": ["Adds only", "Performs all math operations", "Divides only", "Exits immediately"],
        "answer": "Performs all math operations"
    },
    {
        "question": "What is the output of: num = 24 for i in range(1, num+1): if num % i == 0: print(i)",
        "options": ["Prime factors", "All factors", "Just 24", "None"],
        "answer": "All factors"
    },
    {
        "question": "What is the primary characteristic of a list in Python?",
        "options": ["Immutable", "Ordered and mutable", "Unordered and immutable", "Immutable and unindexed"],
        "answer": "Ordered and mutable"
    },
    {
        "question": "What is the result of fruits[0] if fruits = [\"apple\", \"banana\", \"cherry\"]?",
        "options": ["banana", "cherry", "apple", "error"],
        "answer": "apple"
    },
    {
        "question": "Which method adds one item to the end of a list?",
        "options": ["extend()", "insert()", "append()", "add()"],
        "answer": "append()"
    },
    {
        "question": "What does fruits.pop(1) do?",
        "options": ["Removes 'fruits'", "Removes and returns item at index 1", "Adds item at index 1", "Removes the last item"],
        "answer": "Removes and returns item at index 1"
    },
    {
        "question": "Which method removes an item by value?",
        "options": ["pop()", "delete()", "remove()", "clear()"],
        "answer": "remove()"
    },
    {
        "question": "What is the output of fruits[0:2] for fruits = ['apple', 'banana', 'cherry']?",
        "options": ["['apple', 'banana']", "['banana', 'cherry']", "['cherry']", "Error"],
        "answer": "['apple', 'banana']"
    },
    {
        "question": "What happens if you call remove() on a non-existent item?",
        "options": ["Returns None", "Does nothing", "Raises ValueError", "Removes the first item"],
        "answer": "Raises ValueError"
    },
    {
        "question": "What is the difference between append() and extend()?",
        "options": ["No difference", "extend adds one item", "append adds multiple items", "append adds one item, extend adds multiple"],
        "answer": "append adds one item, extend adds multiple"
    },
    {
        "question": "Which method sorts a list in ascending order?",
        "options": ["sort()", "reverse()", "order()", "arrange()"],
        "answer": "sort()"
    },
    {
        "question": "What will words.sort(key=len) do?",
        "options": ["Sorts alphabetically", "Sorts by string length", "Sorts by ASCII", "Throws error"],
        "answer": "Sorts by string length"
    },
    {
        "question": "Tuples in Python are:",
        "options": ["Mutable", "Immutable", "Changeable", "Dictionary keys only"],
        "answer": "Immutable"
    },
    {
        "question": "What is the result of tuple1[0]?",
        "options": ["Error", "Index 1 value", "First element", "None"],
        "answer": "First element"
    },
    {
        "question": "How do you create a tuple from a list?",
        "options": ["list()", "convert()", "tuple()", "dict()"],
        "answer": "tuple()"
    },
    {
        "question": "Which method is used to count items in a tuple?",
        "options": ["length()", "count()", "size()", "tally()"],
        "answer": "count()"
    },
    {
        "question": "Can tuples be used as dictionary keys?",
        "options": ["Yes", "No", "Only strings", "Only lists"],
        "answer": "Yes"
    },
    {
        "question": "What happens if you try tuple1[0] = 'new'?",
        "options": ["Changes the value", "Adds an element", "Raises TypeError", "Replaces tuple"],
        "answer": "Raises TypeError"
    },
    {
        "question": "What does tuple1 + tuple2 do?",
        "options": ["Merges both tuples", "Subtracts values", "Throws error", "Returns the first tuple"],
        "answer": "Merges both tuples"
    },
    {
        "question": "What will tuple1 * 2 do?",
        "options": ["Multiply elements", "Duplicate each item", "Repeat the tuple", "None"],
        "answer": "Repeat the tuple"
    },
    {
        "question": "Tuple methods include:",
        "options": ["sort, index", "append, extend", "count, index", "pop, insert"],
        "answer": "count, index"
    },
    {
        "question": "Which of the following is invalid with a tuple?",
        "options": ["Accessing an element", "Using in operator", "Appending new value", "Counting values"],
        "answer": "Appending new value"
    },
    {
        "question": "What is a dictionary in Python?",
        "options": ["Indexed, immutable collection", "Key-value unordered collection", "Ordered, mutable key-value collection", "Only accepts numbers"],
        "answer": "Ordered, mutable key-value collection"
    },
    {
        "question": "Which symbol is used to define a dictionary?",
        "options": ["[]", "()", "{}", "<>"],
        "answer": "{}"
    },
    {
        "question": "What will person.get('email', 'not found') return if key doesn't exist?",
        "options": ["Error", "None", "'not found'", "False"],
        "answer": "'not found'"
    },
    {
        "question": "Which method removes a key and returns its value?",
        "options": ["delete()", "remove()", "pop()", "discard()"],
        "answer": "pop()"
    },
    {
        "question": "How to get only dictionary keys?",
        "options": ["person.items()", "person.keys()", "person.values()", "person.get()"],
        "answer": "person.keys()"
    },
    {
        "question": "What does update() method do?",
        "options": ["Replaces the dictionary", "Adds or updates items", "Clears dictionary", "Returns length"],
        "answer": "Adds or updates items"
    },
    {
        "question": "What is the result of using the same key twice in a dictionary?",
        "options": ["Error", "Adds both", "Keeps last value", "Keeps first value"],
        "answer": "Keeps last value"
    },
    {
        "question": "What happens with del dict['key']?",
        "options": ["Adds key", "Removes key without return", "Returns deleted key", "Raises error"],
        "answer": "Removes key without return"
    },
    {
        "question": "Which method returns all key-value pairs as tuples?",
        "options": ["items()", "keys()", "values()", "tuples()"],
        "answer": "items()"
    },
    {
        "question": "What happens after dict.clear()?",
        "options": ["All keys removed", "Only values removed", "Nothing", "Error"],
        "answer": "All keys removed"
    },
    {
        "question": "What is a nested dictionary?",
        "options": ["Dictionary with numeric keys", "Dictionary inside a list", "Dictionary with another dictionary as value", "List of dictionaries"],
        "answer": "Dictionary with another dictionary as value"
    },
    {
        "question": "What does len(dict) return?",
        "options": ["Size in bytes", "Number of keys", "Number of values", "Number of pairs"],
        "answer": "Number of keys"
    },
    {
        "question": "Which function checks if a key exists in dictionary?",
        "options": ["has_key()", "exists()", "in", "find()"],
        "answer": "in"
    },
    {
        "question": "What is dictionary comprehension used for?",
        "options": ["Filtering lists", "Creating dictionaries in one line", "Compressing data", "Importing modules"],
        "answer": "Creating dictionaries in one line"
    },
    {
        "question": "What is the output of: {x: x*2 for x in [1, 2, 3]}",
        "options": ["{1:2, 2:4, 3:6}", "{1,2,3}", "[2,4,6]", "Error"],
        "answer": "{1:2, 2:4, 3:6}"
    },
    {
        "question": "Which of the following is not a property of a Python set?",
        "options": ["Unordered", "Indexed", "Mutable", "Unchangeable"],
        "answer": "Indexed"
    },
    {
        "question": "What will be the type of an empty set created using {}?",
        "options": ["set", "dict", "list", "frozenset"],
        "answer": "dict"
    },
    {
        "question": "Sets can store which type(s) of data?",
        "options": ["Only immutable types", "Only mutable types", "Both mutable and immutable types", "Only strings and integers"],
        "answer": "Only immutable types"
    },
    {
        "question": "What happens if you try to add a list to a set?",
        "options": ["It is converted to tuple", "It is ignored", "TypeError is raised", "It is flattened"],
        "answer": "TypeError is raised"
    },
    {
        "question": "Which method is used to remove all elements from a set?",
        "options": ["delete()", "clear()", "empty()", "remove()"],
        "answer": "clear()"
    },
    {
        "question": "What will my_set.pop() do?",
        "options": ["Remove the first element", "Remove the last element", "Remove a random element", "Raise an error"],
        "answer": "Remove a random element"
    },
    {
        "question": "remove() raises an error if the element does not exist. Which one does not?",
        "options": ["pop()", "discard()", "delete()", "clear()"],
        "answer": "discard()"
    },
    {
        "question": "Which of the following is used to combine sets and return a new set with unique values?",
        "options": ["merge()", "union()", "join()", "update()"],
        "answer": "union()"
    },
    {
        "question": "What does difference_update() do?",
        "options": ["Adds common elements", "Removes multiple matching elements", "Swaps set content", "Returns new set only"],
        "answer": "Removes multiple matching elements"
    },
    {
        "question": "Which method modifies the set by keeping only items present in another set?",
        "options": ["retain()", "intersection_update()", "union()", "pop()"],
        "answer": "intersection_update()"
    },
    {
        "question": "Can a set hold a tuple?",
        "options": ["Yes", "No", "Only if it’s numeric", "Only if tuple is hashable"],
        "answer": "Yes"
    },
    {
        "question": "What does hashing help with in a set?",
        "options": ["Indexing", "Sorting", "Fast lookup and storage", "Removing duplicates only"],
        "answer": "Fast lookup and storage"
    },
    {
        "question": "What is rehashing?",
        "options": ["Recalculating sum", "Resizing hash table for sets", "Reloading from memory", "Sorting the set"],
        "answer": "Resizing hash table for sets"
    },
    {
        "question": "Why do elements change order in a set?",
        "options": ["They are sorted internally", "Due to hashing and rehashing", "Python randomizes them", "They follow insertion order"],
        "answer": "Due to hashing and rehashing"
    },
    {
        "question": "Which complexity is average for lookup in a Python set?",
        "options": ["O(n)", "O(log n)", "O(1)", "O(n^2)"],
        "answer": "O(1)"
    },
    {
        "question": "Which one is immutable?",
        "options": ["set", "frozenset", "list", "tuple"],
        "answer": "frozenset"
    },
    {
        "question": "Can a frozenset be used as a dictionary key?",
        "options": ["No", "Only if it contains strings", "Yes", "Only in Python 3.10+"],
        "answer": "Yes"
    },
    {
        "question": "What method can frozenset use?",
        "options": ["add()", "union()", "update()", "discard()"],
        "answer": "union()"
    },
    {
        "question": "How can you create a frozenset?",
        "options": ["{}", "set()", "frozenset()", "tuple()"],
        "answer": "frozenset()"
    },
    {
        "question": "Which method is not available in frozenset?",
        "options": ["add()", "union()", "intersection()", "difference()"],
        "answer": "add()"
    },
    {
        "question": "What does symmetric_difference() do?",
        "options": ["Returns common elements", "Returns elements unique to both sets", "Returns empty set", "None of the above"],
        "answer": "Returns elements unique to both sets"
    },
    {
        "question": "issubset() returns True when:",
        "options": ["All elements of set A are in set B", "At least one element is common", "Sets are equal", "A has more elements"],
        "answer": "All elements of set A are in set B"
    },
    {
        "question": "issuperset() returns True when:",
        "options": ["Any one element is in both", "All elements of other set are in current set", "Sets are equal", "Set is not empty"],
        "answer": "All elements of other set are in current set"
    },
    {
        "question": "What is the result of intersection()?",
        "options": ["Union of sets", "Common elements", "Difference", "Empty set"],
        "answer": "Common elements"
    },
    {
        "question": "Which of these is valid for both set and frozenset?",
        "options": ["add()", "remove()", "copy()", "update()"],
        "answer": "copy()"
    },
    {
        "question": "What does Python use to track object references?",
        "options": ["Manual memory management", "Reference counting", "Indexing", "Garbage bins"],
        "answer": "Reference counting"
    },
    {
        "question": "When is an object eligible for garbage collection?",
        "options": ["When it's too large", "When reference count is zero", "After 1 minute", "When memory is full"],
        "answer": "When reference count is zero"
    },
    {
        "question": "What is the use of gc.collect()?",
        "options": ["Delete files", "Free up all memory", "Trigger manual garbage collection", "Clear lists"],
        "answer": "Trigger manual garbage collection"
    },
    {
        "question": "Python GC is:",
        "options": ["Manual only", "Automatic and periodic", "OS dependent", "Deprecated"],
        "answer": "Automatic and periodic"
    },
    {
        "question": "What issue can still occur despite GC?",
        "options": ["Unused variable remains", "Circular references", "SyntaxError", "File not found"],
        "answer": "Circular references"
    },
    {
        "question": "What is a module in Python?",
        "options": ["A GUI toolkit", "A type of function", "A file containing Python code", "A reserved keyword"],
        "answer": "A file containing Python code"
    },
    {
        "question": "Which of the following is a built-in module in Python?",
        "options": ["mymodule", "custommath", "math", "utils"],
        "answer": "math"
    },
    {
        "question": "Which command is used to install third-party modules?",
        "options": ["python install", "pip install", "mod install", "py get"],
        "answer": "pip install"
    },
    {
        "question": "Which of the following is a valid import statement?",
        "options": ["get math", "use math", "import math", "open math"],
        "answer": "import math"
    },
    {
        "question": "How do you import only the sqrt function from math?",
        "options": ["import math.sqrt", "import sqrt from math", "from math import sqrt", "include math.sqrt"],
        "answer": "from math import sqrt"
    },
    {
        "question": "What does import numpy as np do?",
        "options": ["Imports NumPy without alias", "Prevents import errors", "Imports NumPy with alias 'np'", "Creates a new module"],
        "answer": "Imports NumPy with alias 'np'"
    },
    {
        "question": "What happens when you use from math import *?",
        "options": ["Only pi is imported", "All math functions are imported into global namespace", "Creates a new module", "Imports nothing"],
        "answer": "All math functions are imported into global namespace"
    },
    {
        "question": "Which import method is not recommended for large modules?",
        "options": ["import module", "from module import function", "from module import *", "import module as alias"],
        "answer": "from module import *"
    },
    {
        "question": "Which pi is used after from math import * and then from numpy import *?",
        "options": ["math.pi", "numpy.pi", "built-in pi", "None"],
        "answer": "numpy.pi"
    },
    {
        "question": "Wildcard import affects which of the following most?",
        "options": ["Speed", "Namespace readability", "Syntax", "Compilation time"],
        "answer": "Namespace readability"
    },
    {
        "question": "What is a function in Python?",
        "options": ["Data storage", "Looping block", "Reusable block of code", "Static method only"],
        "answer": "Reusable block of code"
    },
    {
        "question": "Which is a built-in function?",
        "options": ["my_function()", "print()", "sum_nums()", "define()"],
        "answer": "print()"
    },
    {
        "question": "Which type of function is created using def?",
        "options": ["Lambda", "User-defined", "Anonymous", "Global"],
        "answer": "User-defined"
    },
    {
        "question": "What does the return statement do in a function?",
        "options": ["Ends the loop", "Sends back a result to caller", "Exits program", "Prints a variable"],
        "answer": "Sends back a result to caller"
    },
    {
        "question": "What is the output of def add(x=1,y=2): return x+y; print(add())?",
        "options": ["0", "3", "1", "Error"],
        "answer": "3"
    },
    {
        "question": "Which symbol is used for variable-length positional arguments?",
        "options": ["**", "*", "&", "#"],
        "answer": "*"
    },
    {
        "question": "What type is *args inside the function?",
        "options": ["list", "tuple", "dict", "int"],
        "answer": "tuple"
    },
    {
        "question": "What does **kwargs return?",
        "options": ["tuple", "list", "dictionary", "set"],
        "answer": "dictionary"
    },
    {
        "question": "Which of these is a keyword-only argument?",
        "options": ["x, y", "args", "num=5 after a '' in parameter list", "z/"],
        "answer": "num=5 after a '' in parameter list"
    },
    {
        "question": "What happens if you try to pass positional-only args using keywords?",
        "options": ["They are accepted", "Raises TypeError", "Ignores them", "Assigns default values"],
        "answer": "Raises TypeError"
    },
    {
    "question": "What is the default scope of a function-defined variable?",
    "options": ["Global", "Local", "Built-in", "External"],
    "answer": "Local"
  },
  {
    "question": "How do you modify an enclosing variable inside a nested function?",
    "options": ["global", "nonlocal", "static", "override"],
    "answer": "nonlocal"
  },
  {
    "question": "Which scope resolution rule does Python follow?",
    "options": ["GLEB", "LEGB", "GE", "GBL"],
    "answer": "LEGB"
  },
  {
    "question": "Which variable is affected by global keyword?",
    "options": ["Local variable", "Global variable", "Function parameter", "Class attribute"],
    "answer": "Global variable"
  },
  {
    "question": "What makes a function a generator?",
    "options": ["Using return", "Using yield", "Having loops", "Recursion"],
    "answer": "Using yield"
  },
  {
    "question": "Which is an advantage of generator functions?",
    "options": ["Slower", "Stores all data", "Memory efficient", "Uses global scope"],
    "answer": "Memory efficient"
  },
  {
    "question": "What does yield do?",
    "options": ["Ends function", "Pauses and resumes the function", "Loops infinitely", "Returns multiple values"],
    "answer": "Pauses and resumes the function"
  },
  {
    "question": "What is the result of calling next() on a generator after exhaustion?",
    "options": ["None", "Repeats values", "Raises StopIteration", "Starts from beginning"],
    "answer": "Raises StopIteration"
  },
  {
    "question": "Which keyword is used to define anonymous functions?",
    "options": ["def", "lambda", "return", "func"],
    "answer": "lambda"
  },
  {
    "question": "What is required in a recursive function to avoid infinite recursion?",
    "options": ["Loop", "Base case", "return", "yield"],
    "answer": "Base case"
  },
  {
    "question": "What is the return type of a lambda function?",
    "options": ["None", "String", "Expression result", "Function name"],
    "answer": "Expression result"
  },
  {
    "question": "What does exception handling in Python help prevent?",
    "options": ["Syntax errors", "Program crashes", "Compiler warnings", "Type conversions"],
    "answer": "Program crashes"
  },
  {
    "question": "Which Python construct is used to handle exceptions?",
    "options": ["loop", "try-final", "try-except", "error-catch"],
    "answer": "try-except"
  },
  {
    "question": "Why is exception handling important?",
    "options": ["Makes code longer", "Prevents abrupt termination", "Forces type safety", "Avoids imports"],
    "answer": "Prevents abrupt termination"
  },
  {
    "question": "What happens if an exception is not handled?",
    "options": ["It gets ignored", "Program crashes", "It logs to system", "Python retries"],
    "answer": "Program crashes"
  },
  {
    "question": "What is the role of the finally block?",
    "options": ["Runs only if an exception occurs", "Runs if try succeeds", "Always executes", "Skips execution on error"],
    "answer": "Always executes"
  },
  {
    "question": "Where should code be placed if it might cause an error?",
    "options": ["Inside the try block", "Inside the else block", "Before import", "After return"],
    "answer": "Inside the try block"
  },
  {
    "question": "Which block runs only when there is no exception?",
    "options": ["finally", "try", "else", "error"],
    "answer": "else"
  },
  {
    "question": "Which block is used to catch exceptions?",
    "options": ["try", "except", "else", "finally"],
    "answer": "except"
  },
  {
    "question": "What will except Exception as e: do?",
    "options": ["Raise exception", "Catch any exception and store in e", "Ignore all errors", "Stop execution"],
    "answer": "Catch any exception and store in e"
  },
  {
    "question": "Which keyword allows you to manually raise an error?",
    "options": ["error", "raise", "except", "break"],
    "answer": "raise"
  },
  {
        "question": "What type of error is raised by 10 / 0?",
        "options": ["ValueError", "ZeroDivisionError", "IndexError", "ArithmeticError"],
        "answer": "ZeroDivisionError"
    },
    {
        "question": "What kind of error occurs if input is not a number?",
        "options": ["NameError", "ValueError", "IndexError", "ImportError"],
        "answer": "ValueError"
    },
    {
        "question": "Which error occurs if you try to divide by a string?",
        "options": ["ValueError", "KeyError", "TypeError", "AttributeError"],
        "answer": "TypeError"
    },
    {
        "question": "How to catch all unexpected exceptions?",
        "options": ["except Error", "except Exception", "except BaseException", "except All"],
        "answer": "except Exception"
    },
    {
        "question": "What is a good use of finally block?",
        "options": ["Initialize variables", "Check condition", "Close files / clean up", "Skip input"],
        "answer": "Close files / clean up"
    },
    {
        "question": "Which keyword defines a custom exception class?",
        "options": ["exception", "class", "def", "raise"],
        "answer": "class"
    },
    {
        "question": "What must a custom exception inherit from?",
        "options": ["RuntimeError", "Exception", "object", "error"],
        "answer": "Exception"
    },
    {
        "question": "What happens when raise ValueError(...) is executed?",
        "options": ["Continues execution", "Raises an exception", "Ignores it", "Logs the error"],
        "answer": "Raises an exception"
    },
    {
        "question": "Which statement is used to create your own error?",
        "options": ["def error", "raise CustomError", "error.raise", "custom(error)"],
        "answer": "raise CustomError"
    },
    {
        "question": "What is the output of raise SystemExit(\"Bye!\") if unhandled?",
        "options": ["Nothing", "Terminates program", "Logs warning", "Goes to finally"],
        "answer": "Terminates program"
    },
    {
        "question": "What should you always do after opening a file?",
        "options": ["Ignore it", "Close it in finally", "Save it again", "Leave it for GC"],
        "answer": "Close it in finally"
    },
    {
        "question": "Which is a consequence of NOT using exception handling?",
        "options": ["Longer code", "System instability", "Better readability", "Faster execution"],
        "answer": "System instability"
    },
    {
        "question": "Why should raw error messages be avoided in user programs?",
        "options": ["They are slow", "They reveal sensitive info", "They help hackers", "They waste memory"],
        "answer": "They reveal sensitive info"
    },
    {
        "question": "What’s the problem with this: except: (generic except)?",
        "options": ["It’s too specific", "It hides error type", "It stops code", "It slows runtime"],
        "answer": "It hides error type"
    },
    {
        "question": "Which keyword signals a function never returns?",
        "options": ["never", "NoReturn", "void", "exit"],
        "answer": "NoReturn"
    },
    {
        "question": "What happens when a function with -> NoReturn runs?",
        "options": ["Returns None", "Raises exception or loops forever", "Logs message", "Terminates input"],
        "answer": "Raises exception or loops forever"
    },
    {
        "question": "Which module provides NoReturn type hint?",
        "options": ["os", "typing", "math", "sys"],
        "answer": "typing"
    },
    {
        "question": "Which alternative can be used when not using NoReturn?",
        "options": ["int", "None", "str", "void"],
        "answer": "None"
    },
    {
        "question": "Why is NoReturn useful?",
        "options": ["To decorate functions", "To use in loops", "For static analysis", "For default return"],
        "answer": "For static analysis"
    },
    {
        "question": "What happens if try block raises an error and except catches it?",
        "options": ["Code crashes", "Code in except executes", "else executes", "finally skips"],
        "answer": "Code in except executes"
    },
    {
        "question": "What if an error occurs, but only try and else are defined?",
        "options": ["Runs else", "Crashes with uncaught error", "Handles it", "Skips try"],
        "answer": "Crashes with uncaught error"
    },
    {
        "question": "What happens after raise ValueError(\"Oops\") in try-except-finally?",
        "options": ["Only finally runs", "Only try runs", "except and finally run", "Code skips all"],
        "answer": "except and finally run"
    }
]

if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

st.title("Python MCQ Quiz")
st.write(f"Test your Python knowledge with these  questions!")

with st.form(key='quiz_form'):
    for idx, question in enumerate(questions):
        st.markdown(f"### Question {idx + 1}")
        st.write(question['question'])
        key = f"q{idx}"
        value = st.radio(
            "Select your answer:",
            options=question['options'],
            key=key,
            index=None
        )
        st.session_state.answers[idx] = value
    submitted = st.form_submit_button("Submit Quiz")

if submitted:
    st.session_state.submitted = True
    score = 0
    for idx, question in enumerate(questions):
        if st.session_state.answers.get(idx) == question['answer']:
            score += 1
    
    st.markdown("---")
    st.subheader(f"Score: {score}/{len(questions)}")
    
    for idx, question in enumerate(questions):
        st.markdown(f"### Question {idx + 1}")
        st.write(question['question'])
        st.write(f"Your answer: {st.session_state.answers.get(idx, 'Unanswered')}")
        st.write(f"Correct answer: {question['answer']}")
        st.markdown("---")
