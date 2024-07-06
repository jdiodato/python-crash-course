ordinal_numbers = list(range(1,10))
ind = ""

for o in ordinal_numbers:
    if o == 1:
        ind = "st"
    elif o == 2:
        ind = "nd"
    elif o == 3:
        ind = "rd"
    else:
        ind = 'th'

    print(f"{o}{ind}")

