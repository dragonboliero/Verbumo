import random

conti = True
alphabet = ['a','ą','b','c','ć','d','e','ę','f','g','h','i','j','k','l','ł','m','n','ń','o','ó','p','r','s','t','u','w','x','y','z','ź','ż']
letters = []
word = ''

while conti:
    print('provide number of letters to generate a word: ')
    try:
        no_letters = input()
        with open(f'dictionaries/{no_letters}.txt','r',encoding='utf-8') as dictionary:
                for line in dictionary:
                    letters.append(line)
        word = random.choice(letters)
        print(word.strip())
        letters.clear()
    except ValueError:
        print('wrong value. It has to be a number')
    print('Do you wish to continue? Press n to stop')
    val = input()
    if val !='n':
        conti = True
    else:
        conti = False