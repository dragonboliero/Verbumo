import requests
import bs4 as bs

new_dictio = []



counter = 0
old_dictio = []
with open("5.txt",'r',encoding='utf-8') as test:
    for line in test:
        old_dictio.append(line.strip())
        
for word in old_dictio:
    word_address = f"https://scrabble123.pl/slownik-scrabble/{word}"
    dictionary = requests.get(word_address)
    text = str(dictionary.content)
    if "nie istnieje w grze scrabble" in text:
        pass
    else:
        word = word + "\n"
        new_dictio.append(word)
    print(counter)
    counter = counter + 1 
print(new_dictio)
with open("new_dictio.txt","w",encoding='utf-8') as file:
    for word in new_dictio:
        file.write(word)