def national_code_validator(national_code: str) -> bool:
    if not national_code:
        return False

    if national_code.startswith('9'):
        return len(national_code) == 12 and national_code.startswith('9') and national_code.isdigit()
    else:
        if len(national_code) != 10 or not national_code.isdigit():
            return False

    check = int(national_code[9])
    s = sum(int(national_code[x]) * (10 - x) for x in range(9)) % 11
    return (s < 2 and check == s) or (s >= 2 and check == 11 - s)
