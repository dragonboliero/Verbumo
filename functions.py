from cgitb import text
import random
import requests
import html5lib
from bs4 import BeautifulSoup as bs

def pick_random_word(name):
    all_words = []
    with open(f'dictionaries/{name}.txt','r',encoding='utf-8') as dictionary:
            for line in dictionary:
                all_words.append(line.strip().upper())

    return random.choice(all_words)

def words_dictionary(name):
    all_words = []
    with open(f'dictionaries/{name}.txt','r',encoding='utf-8') as dictionary:
            for line in dictionary:
                all_words.append(line.strip().upper())
    
    return all_words

def get_dictionary_entry(name):
    cleared_meainings = ""
    entry_address = f"https://sjp.pwn.pl/szukaj/{name}.html"
    entry_page=requests.get(entry_address)
    soup = bs(entry_page.content,'html.parser')
    #print(soup.prettify)
    meanings = soup.find_all("div",{"class":"znacz"})
    text_meanings = str(meanings)
    if len(text_meanings)!=2:
        text_meanings = text_meanings.split("«")
        counter = 0
        for item in text_meanings:
            if "»" not in item:
                text_meanings.pop(counter)
                counter+=1
        counter = 1
        for split_item in text_meanings:
            if ("»</div>") in split_item:
                split_item = split_item.split("»</div>")
                new_meaining = f"[b]{counter}.[/b] {split_item[0]}"
                cleared_meainings = cleared_meainings + new_meaining + "\n"
                counter +=1
        #print(cleared_meainings) 
    else:
        meanings = soup.find_all("div",{"class":"ribbon-element"})
        text_meanings = str(meanings)
        if len(text_meanings)!=2:
            text_meanings = text_meanings.split("«")
            text_meanings = text_meanings[1].split("»")
            cleared_meainings = "[b]1.[/b] " + text_meanings[0]
        else:
            print('nothing found')

    return(cleared_meainings)

#get_dictionary_entry("tutaj")

dictio  = words_dictionary("correct_answers")
counter = 1
for i in range(1453,len(dictio)):
    print(dictio[i])
    print(get_dictionary_entry(dictio[i]))
    counter+=1
    input()