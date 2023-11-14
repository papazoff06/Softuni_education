usernames = input().split(', ')


def is_length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def is_letter(username):
    for letter in username:
        if not (letter.isalnum() or  letter == '-' or  letter == '_'):
            return False
    return True


def no_redundant(username):
    if ' ' in username:
        return False
    return True


def is_whole_true(username):
    if is_length(username) and is_letter(username) and no_redundant(username):
        return True
    return False


for username in usernames:
    if is_whole_true(username):
        print(username)
