def validate_password(password):
    if 6 > len(password) > 24:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True  
        elif char.isdigit():
            has_digit = True

    if not(has_upper and has_lower and has_digit):
        return False
    
    for i in range(len(password)- 2):
        if password[i] == password[i+1] == password[i+2]:
            return False
        
    allow_special = "!@#$%^&*()+=_-{}[]:;\"'?<>,."
    for char in password:
        if not(char.isalnum() or char in allow_special):
            return False
        
    return True

print(validate_password("Password123!"))
