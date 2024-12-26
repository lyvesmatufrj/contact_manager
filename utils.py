def validate_phone(phone: str) -> bool:
    if len(phone) == 10 and phone.isdigit():
        return True
    else:
        return False
