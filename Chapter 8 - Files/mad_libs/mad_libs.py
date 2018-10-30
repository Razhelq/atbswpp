# The app replaces the key words from the text filled with inputed words


text_file = open('text_to_fill.txt')

words = text_file.read()
words = words.split(' ')
for word in words:
    if word == 'ADJECTIVE':
        words[words.index(word)] = input('Enter an adjective: ')
    elif word == 'NOUN':
        words[words.index(word)] = input('Enter a noun: ')
    elif word == 'VERB':
        words[words.index(word)] = input('Enter a verb: ')
    elif word == 'ADVERB':
        words[words.index(word)] = input('Enter a adverb: ')

new_text = open('new_text.txt', 'w')
new_text.write(' '.join(words))

new_text.close()
text_file.close()

new_text = open('new_text.txt')
print(new_text.read())