import os
import requests

url = input("please enter a valid url:")

response = requests.get('https://'+url)
text = response.text
valid_characters = "abcdefghijklmnopqrstuvwxyz"
valid_characters += valid_characters.upper()

for c in text:
    if c not in valid_characters:
        text = text.replace(c, ' ')
words = text.split(' ')

counter = {}
for word in words:
    if word not in counter:
        counter[word] = 1
    else:
        counter[word] += 1


for word, count in counter.items():
    print(word, count)