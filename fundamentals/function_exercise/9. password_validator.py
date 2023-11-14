def password_validations(some_string):
    list_with_wrong_password = []
    if 6 > len(some_string) or len(some_string) > 10:
        list_with_wrong_password.append("Password must be between 6 and 10 characters")
    if not some_string.isalnum():
        list_with_wrong_password.append("Password must consist only of letters and digits")
    digit_counter = 0
    for character  in some_string:
        if character.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        list_with_wrong_password.append("Password must have at least 2 digits")
    return list_with_wrong_password


password = input()

errors_in_password = password_validations(password)
if not errors_in_password:
    print("Password is valid")
else:
    print('\n'.join(errors_in_password))

