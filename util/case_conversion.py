import re

def to_lower_snake_from_pascal(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def to_pascal_from_snake(snake_str: str) -> str:
    return ''.join(word.capitalize() for word in snake_str.split('_'))

def capitalize_first_char(input_string: str) -> str:
    return input_string.title()