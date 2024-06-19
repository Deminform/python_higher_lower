import random
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

celebrities_followers = {
    "Cristiano Ronaldo": 583000000,
    "Lionel Messi": 466000000,
    "Selena Gomez": 426000000,
    "Dwayne Johnson": 379000000,
    "Kylie Jenner": 387000000,
    "Kim Kardashian": 362000000,
    "Ariana Grande": 362000000,
    "Beyoncé": 325000000,
    "Justin Bieber": 292000000,
    "Taylor Swift": 272000000,
    "Neymar": 212000000,
    "Kendall Jenner": 284000000,
    "National Geographic": 278000000,
    "Jennifer Lopez": 250000000,
    "Nicki Minaj": 227000000,
    "Khloe Kardashian": 297000000,
    "Miley Cyrus": 202000000,
    "Kourtney Kardashian": 217000000,
    "Kevin Hart": 178000000,
    "Virat Kohli": 256000000,
    "Zendaya": 182000000,
    "Katy Perry": 195000000,
    "Demi Lovato": 150000000,
    "Cardi B": 169000000,
    "LeBron James": 153000000,
    "Billie Eilish": 113000000,
    "Shakira": 88000000,
    "Chris Hemsworth": 59000000,
    "Emma Watson": 71000000,
    "Tom Holland": 70000000
}
is_play_game = True
score = 0

# метод возвращает случайную знаменитость
def take_name() -> list:
    star_list = list(celebrities_followers.keys())
    name = random.choice(star_list)
    value = celebrities_followers.pop(name)
    return name, value

def print_answer(yes_or_no, name_1, value_1, name_2, value_2):
    print(f'\n{yes_or_no}{name_1} have {value_1} followers \
                  \nVS\n{name_2} have {value_2} followers\n')


while is_play_game:
    celebrity_1_name, celebrity_1_value = take_name()
    celebrity_2_name, celebrity_2_value = take_name()
    
    while True:
        print(f'\n\nCompare A: {celebrity_1_name}\n\nVS\n\nAgainst B: {celebrity_2_name}\n\n')

        answer = None
        while answer not in ['A', 'B']:
            answer = input('Who has more followers? Type "A" or type "B": ').upper()
            if answer in ['A', 'B']:
                break

        if answer == 'A' and celebrity_1_value > celebrity_2_value or answer == 'B' and celebrity_2_value > celebrity_1_value:
            clear()
            score += 1
            print_answer('You`re right!\n', celebrity_1_name, celebrity_1_value, celebrity_2_name, celebrity_2_value)
            
            if answer == "A":
                celebrity_2_name, celebrity_2_value = take_name()
            else:
                celebrity_1_name, celebrity_1_value = take_name()
        else:
            clear()
            print_answer(f'Wrong answer. You`re score: {score}.\n', celebrity_1_name, celebrity_1_value, celebrity_2_name, celebrity_2_value)
            break

    one_more = None
    while one_more not in ['y', 'n']:
        one_more = input('Play again?: "y" or "n" ').lower()
        if one_more == 'n':
            is_play_game = False
            break
        elif one_more == 'y':
            break
