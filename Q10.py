def get_name(email):
    name = email.split('@')[0]
    result = ""

    for char in name:
        if char.isalpha():
            result += char

    return result

print(get_name("Amrita07@gmail.com"))