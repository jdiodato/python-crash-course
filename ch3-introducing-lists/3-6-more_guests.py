guests = ['Malcolm X', 'Patrick Flynn', 'Albert Einstein']
message = ", I'd like to invite you to dinner on Friday!"

print(f"{guests[0]}{message}.")
print(f"{guests[1]}{message}.")
print(f"{guests[2]}{message}.")

print(f"\nOh no! {guests[-1]} isn't able to make it.")
guests.pop()
guests.append("Wolfgang Amadeus Mozart")
print("I need to print some new invitations.\n")

print(f"{guests[0]}{message}.")
print(f"{guests[1]}{message}.")
print(f"{guests[2]}{message}.\n")

print("Good news! I've found a larger dinner table, so we can invite more guests.")

guests.insert(0, "Vincent D'Onofrio")
guests.insert(2, "Alan Turing")
guests.append("Willie McCallum")

print("I'll print the invitations one last time...\n")

print(f"{guests[0]}{message}.")
print(f"{guests[1]}{message}.")
print(f"{guests[2]}{message}.")
print(f"{guests[3]}{message}.")
print(f"{guests[4]}{message}.")
print(f"{guests[5]}{message}.")


