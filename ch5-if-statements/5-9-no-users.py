usernames = []

if usernames:
    for u in usernames:
        if u == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {u.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")