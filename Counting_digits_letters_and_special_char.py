st = input('Enter the string: ')
d,l,o = 0,0,0
for characters in st:
    if characters.isdigit():
        d += 1
    elif characters.isalpha():
        l += 1
    else:
        o +=1
print(f"Digits: {d}")
print(f"Letters: {l}")
print(f"Other characters: {o}")