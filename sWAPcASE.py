def swap_case(s):
    s_mod = ''
    for letter in s:
        if letter.isupper():
            s_mod += (letter.lower())
            continue
        if letter.islower():
            s_mod += (letter.upper())
            continue
        else:
            s_mod += letter
            continue
    return s_mod
print(swap_case('HackerRank.com presents "Pythonist 2".'))