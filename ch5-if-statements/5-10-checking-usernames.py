usernames = ['john', 'jayden', 'admin', 'joseph', 'al']
usernames_lower = []
new_users = ['jasmin', 'ashley', 'kayla', 'john', 'brandon']

usernames_lower = [u.lower() for u in usernames]

for n in new_users:
    if n.lower() in usernames_lower:
        print("Username taken. You'll need to enter a new one.")
    else:
        print("That username is available.")