def pass_length_validator(password):
    validator_counter = 0
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
    else:
        validator_counter += 1

    for digits in password:
        if not ((48 <= ord(digits) <= 57) or (48 <= ord(digits) <= 90) or (97 <= ord(digits) <= 122)):
            print("Password must consist only of letters and digits")
            break
    else:
        validator_counter += 1

    digits_counter = 0
    for digits in password:
        if 48 <= ord(digits) <= 57:
            digits_counter += 1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
    else:
        if validator_counter == 2:
            print("Password is valid")


pass_input = input()
pass_length_validator(pass_input)

