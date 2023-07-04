# Using the list from my dinner guest programs to produce an index error.
# This snippet produces an IndexError because Python list indices start at 0. 
# guests[2] would correctly reference the 3rd element in the list, Albert Einstein.

guests = ['Malcolm X', 'Patrick Flynn', 'Albert Einstein']
print(guests[3])