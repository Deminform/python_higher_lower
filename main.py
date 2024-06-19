import random
import game_data
import art
import os

is_game_on = True
score = 0

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def take_one_person(list: list):
    lenght = len(list)
    index = random.randint(0, lenght - 1)
    person = list.pop(index)
    return person
    
def print_persons(msg: str, person: dict):
    person_name = person['name']
    person_decs = person['description']
    person_country = person['country']
    print(f'{msg}: {person_name}, a {person_decs}, from {person_country}.')

while is_game_on:
    person_1 = take_one_person(game_data.data)
    person_2 = take_one_person(game_data.data)
    clear()

    while len(game_data.data) != 0:
        print(f'\n{art.logo}\n')
        if score > 0:
            print(f'You`re right! Cirrent score: {score}.')
        
        print_persons('Compare A', person_1)
        print(f'\n{art.vs}\n')
        print_persons('Against B', person_2)

        answer = None
        while answer not in ['A', 'B']:
            answer = input('Who has more followers? Type "A" or "B": ').upper()

        if answer == 'A' and person_1['follower_count'] > person_2['follower_count'] or \
            answer == 'B' and person_2['follower_count'] > person_1['follower_count']:
            score += 1
            clear()
            if answer == 'A':
                person_2 = take_one_person(game_data.data)
            else:
                person_1 = take_one_person(game_data.data)
        else:
            clear()
            print(f'\n{art.logo}\nSorry, that`s wrong. Final score: {score}')
            break

    play_more = None
    while play_more not in ['y', 'n']:
        play_more = input('Play more? Type "y" or "n": ').lower()
        if play_more == 'n':
            is_game_on = False