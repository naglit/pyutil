import re

def to_lower_snake_from_pascal(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()