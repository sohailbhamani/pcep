#! /usr/bin/env python3.7

message = input('Enter a message: ')
print('Lowercase: ' + message.lower())
print('Uppercase: ' + message.upper())
print('Capitalized: ' + message.capitalize())
print('Title Case: ' + message.title())
words = message.split()
print('Words: ' + str(message.split()))

sortedWords = sorted(words)
print('Sorted via the sorted method: ')
print(sortedWords)

print('Alphabetic First Word: ' + sortedWords[0])
print('Alphabetic Last Word: ' + sortedWords[-1])

words.sort()
print('sorted vis the .sort function: ')
print(words)
print('Alphabetic First Wordx2: ' + words[0])
words.sort(reverse = True)
print('Alphabetic last Wordx2: ' + words[0])
