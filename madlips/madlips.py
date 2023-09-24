import os
file_path = os.path.join(
    './madlips/', 'story.txt')


with open(file_path, "r") as f:
    story = f.read()

story_copy = story

words = set()

# adjective1 = input("Type in first adjective: ")

while '<' in story_copy and '>' in story_copy:

    first = story_copy.find('<')
    second = story_copy.find('>')
    to_replace = story_copy[first:second + 1]

    words.add(to_replace)

    story_copy = story_copy.replace(to_replace, "x")


answeres = {}

for word in words:
    answer = input(f'Give me a word for {word}: ')
    answeres[word] = answer


for word, replacement in answeres.items():
    story = story.replace(word, replacement)

print(story)
