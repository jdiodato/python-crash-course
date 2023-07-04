# For this program, I use a list of some musical instruments that I play or have played to use all list functions introduced here.
# Functions: insert, pop, append, del/remove, sort, reverse, len, 

instruments = ['Great Highland bagpipe', 'recorder', 'bass', 'guitar']

print("These are some instruments that I play or have played:")
print(instruments)

print("\nLet me add the violin to the list! It was the first instrument I ever played, back in 5th grade.")
instruments.insert(0, "violin")
print(instruments)

print("\nI dabbled in guitar, but never really got too into it. I'll remove it from my list.")
instruments.pop()
print(instruments)

print("\nI've been learning two kids of bagpipe. Let me add the Irish uilleann pipes to the list.")
instruments.append('uilleann pipes')
print(instruments)

print("\nMaybe I should focus on one type of bagpipe for now. Let me remove one from the list.")
instruments.remove("Great Highland bagpipe")
print(instruments)

print("\nMy list currently has " + str(len(instruments)) + " instruments!")
print("I can sort them alphabetically:")
instruments.sort()
print(instruments)

print("\nI can also reverse the list order")
instruments.reverse()
print(instruments)



