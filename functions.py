import random

def pick_random_word(word_length):
    all_words = []
    with open(f'dictionaries/{word_length}.txt','r',encoding='utf-8') as dictionary:
            for line in dictionary:
                all_words.append(line.strip())

    return random.choice(all_words)
