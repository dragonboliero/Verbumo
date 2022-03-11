import random

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