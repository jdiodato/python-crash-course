# already meets the requirements for exercise 6-4

glossary = {
    'variable': 'a named value stored in memory',
    'list': 'a collection of items stored in a particular order',
    'syntax': 'the language we use to write computer code.',
    'comment': 'a code annotation intended for the programmer to read.'
}

for k, v in glossary.items():
    print(f"{k.title()}: {v}")
