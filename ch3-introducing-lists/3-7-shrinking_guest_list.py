# This is one of many exercises that I've completed as intended by the authors based on what we know at this point in the book.
# However, many of the exercises can be greatly simplified with the addition of loops. 

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
print(f"{guests[5]}{message}.\n")

print("Alas, I've just been informed that my new table won't arrive in time for dinner - I only have room for two guests!\n")

removed_guest = guests.pop()
print(f"{removed_guest}, I'm sorry that I can't invite you to dinner this week.")

removed_guest = guests.pop()
print(f"{removed_guest}, I'm sorry that I can't invite you to dinner this week.")

removed_guest = guests.pop()
print(f"{removed_guest}, I'm sorry that I can't invite you to dinner this week.")

removed_guest = guests.pop()
print(f"{removed_guest}, I'm sorry that I can't invite you to dinner this week.\n")

print(f"{guests[0]} and {guests[1]}, you both are still invited!")

guests.remove(guests[0])
guests.remove(guests[0])
print(guests)

