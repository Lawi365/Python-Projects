# Funny Name Generator.
# 2023-18-January
# project no 1. 2023
# code written by : Lawi365

# SudoCode.
"""
Load a list of first names
Load a list of surnames
Choose a first name at random
Assign the name to a variable
Choose surname at randm 
Assing the name to another variable.
Print the names to the screen in order and in red font
Ask the user to quit or play again
If user plays again:
    repeat
If user quits:
    end and exit
"""

import sys
import random
first_names = ['Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
               "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ", 'Chad', 'Chesterfield',
               'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
               'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
               'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
               'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
               'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
               'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
               'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
               'Pushmeet', 'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
               "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
               'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
               'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
               "Winston 'Jazz Hands'", 'Worms',
               'Butterbean', 'Buttermilk', 'Buttocks']

last_names = ['Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
              'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
              'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
              'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
              'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
              'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
              'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
              'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
              'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
              'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
              'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
              'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
              'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
              'Woolysocks']


def choose_random_firstname(first_names, last_name):
    """_summary_
        Generates random names from the given arrays
    Args:
        first_names (_type_): _description_an array of names
        last_name (_type_): _description_An array of names

    Returns:
        _type_: _description_returns tuple first_name , last_name
    """
    choice = random.randint(1, len(first_names) - 1)
    choice1 = random.randint(0, len(last_name) - 1)
    return first_names[choice], 'The '+last_name[choice1]

def main():
    """_summary_Displays names to screen.
    """
    while 1:
        f, l = choose_random_firstname(first_names, last_names)
        print(f'============================\n')
        print('   {} {} '.format(f, l), file=sys.stderr)
        print(f'\n===========================\n')

        print('New Name? press enter : press(n) to exit')
        try_again = input()
        if try_again.lower() == 'n':
            break

if __name__ == "__main__":
    main()