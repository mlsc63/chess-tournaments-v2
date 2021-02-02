from list import ListObjet
from . import home_menu_controller

class SplitPlayers:
    def __init__(self, ):
        pass




class RoundInitialise:
    def __init__(self, tournament, round_model):
        self.tournament = tournament
        self.round_model = round_model


    def first_init(self):
        print('__Initailisation___')

        for i in self.tournament.get_players_instantiation_list():
            match_tuple = (i, "", "")
            self.round_model.add_match_list(match_tuple)

        # if self.round_model.get_name_round() == "Round 1":
            # print("Houlalal")




class RoundController:

    def __init__(self):
        self.list_tournaments = ListObjet.TOURNAMENT


    def __call__(self):

        index = 0
        print('___Rounds en cour___')

        # get objet in the list on list.py
        for tournament in self.list_tournaments:

            # If the tournament is done we don't display
            if tournament.get_status_tournament() == True:

                print(tournament.get_name_tournament())
                print(tournament.get_round_list())
                # get objet on the tournament model and get information with round model
                for round_in_tournament in tournament.get_round_list():
                    if round_in_tournament.get_status_round == True:
                        print(round_in_tournament)
                        # break -> we display only one
                        break

        input()
        return home_menu_controller.HomeMenuController()






