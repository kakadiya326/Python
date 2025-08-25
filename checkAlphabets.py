character = input('Enter any letter:')
if character>='a' and character<='z':
    print('Lower case')
elif character>='A' and character<='Z':
    print('Upper case')
elif character>='0' and character<='9':
    print('Digit')
elif character==" ":
    print('Space')
else:
    print('Special symbol')