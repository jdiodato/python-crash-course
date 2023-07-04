guests = ['Malcolm X', 'Patrick Flynn', 'Albert Einstein']
message = ", I'd like to invite you to dinner on Friday!"

print(f"{guests[0]}" + message)
print(f"{guests[1]}" + message)
print(f"{guests[2]}" + message)

print(f"\nOh no! {guests[-1]} isn't able to make it.")
guests.pop()
guests.append("Wolfgang Amadeus Mozart")
print("I need to print some new invitations.\n")

print(f"{guests[0]}" + message)
print(f"{guests[1]}" + message)
print(f"{guests[2]}" + message)


