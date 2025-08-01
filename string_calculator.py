from exceptions import NegativeNumberError

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    
    clean_numbers = numbers.replace("\n", ",")
    
    parts = clean_numbers.split(",")
    
    negatives = []
    for part in parts:
        number = int(part)
        if number < 0:
            negatives.append(number)
    
    if len(negatives) > 0:
        negative_str = ", ".join(map(str, negatives))
        error_msg = f"negative numbers not allowed: {negative_str}"
        raise NegativeNumberError(error_msg)
    
    result = 0
    for part in parts:
        result += int(part)
    
    return result