favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

should_take = ['sisko', 'jake', 'nog', 'edward', 'odo']

for name in should_take:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for completing the survey!")
    else:
        print(f"{name.title()}, please complete the survey.")