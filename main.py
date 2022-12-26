class Games:
    amount_of_guns = 23
    there_is_characters = 'Yes'


class Shooters(Games):
    shotguns = 'large-caliber'
    amount_of_clips = 10
    gamers_age = 18


class Fortnite(Shooters):
    gamers_age = 20
    what_are_the_weapons = 'Shotguns, sniper riffles, pistols'




    def __init__(self):
        print(f'What are the weapons:{self.what_are_the_weapons}')
        print(f'Gamers age:{self.gamers_age}')
        print(f'Shotguns:{self.shotguns}')
        print(f'Amount of guns: {self.amount_of_guns}')
        print(f'Is there charecters: {self.there_is_characters}')
        print(f'Amount of clips:{self.amount_of_clips}')


games = Fortnite()
