# Re-using my program from 3-4 and adding a line that prints the number of guests. 

# Patrick Flynn was the vocalist of Have Heart, a Boston hardcore band. https://en.wikipedia.org/wiki/Have_Heart.
# His current project is Fiddlehead. https://en.wikipedia.org/wiki/Fiddlehead_(band)

guests = ['Malcolm X', 'Patrick Flynn', 'Albert Einstein']
num_guests = len(guests)
message = ", I'd like to invite you to dinner on Friday!"

print(f"{guests[0]}" + message)
print(f"{guests[1]}" + message)
print(f"{guests[2]}" + message)

print(f"\nI've invited {num_guests} guests to dinner.")