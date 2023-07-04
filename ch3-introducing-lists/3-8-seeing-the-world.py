places = ["London", "Rome", "Quebec", "Glasgow", "Dublin"]

print("The original list:")
print(places)

print("\nThe list in alphabetical order:")
print(sorted(places))

print("\nThe sorted method didn't change the actual order of my list:")
print(places)

print("\nThe reverse method does change the order of a list:")
places.reverse()
print(places)

print("\nThe reverse function can be used a second time to revert the change:")
places.reverse()
print(places)

print("\nLike reverse, sort is also permanent:")
places.sort()
print(places)

print("\nSort also can take a reverse argument:")
places.sort(reverse=True)
print(places)

#print(sorted(places))

#print(places)

#print(sorted(places).reverse())
