message = input(">")
words = message.split(' ')
print(words)
emojis = {
    ":)": 'βΊοΈ',
    ";)": 'π',
    ":(": 'π'
}

output = ""
for word in words:
   output  += emojis.get(word, word) + " "
print(output)
