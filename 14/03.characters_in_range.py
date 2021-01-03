def all_between_ascii(a, z):
    new_string = ""
    if ord(a) > ord(z):
        a, z = z, a
    for i in range(ord(a)+1, ord(z)):
         new_string += chr(i) + " "
    return new_string


start = input()
end = input()

print(all_between_ascii(start, end))
