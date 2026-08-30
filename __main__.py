from utils.player import create_player, Player
from logic import random_choice_club, stat_update_event, choice_answer_event, display_color_club, choice_answer_club
from utils.events import get_event_random_media, get_event_random_footballmoment, tier_club, random_club_low, random_club_sup, create_mercato_event, choice_answer_mercato, MediaEvent
from utils.season import create_season, Season
from utils.league_ranking import create_league_ranking
import random


# ===== Create player object ===== #

#player = create_player()
player = Player(
      "theo lecon",
      16, 
      "France", 
      "attacker",
      22, 
      {"Technical": 70, "Physical": 70, "Speed": 70, "Strike": 70, "Defence": 50, "Vision": 60, "Cold_blood": 70, "Discipline": 60, "Relationship_coach": 50, "Locker_room": 50, "Reputation": 0, "Mental": 50, "Forme": 50},
      "Levante",
      99.0,
      0.001,
      ["yo"],
      3,
      0
    )

player.display_player()



# ===== Choice of starting club ===== #

print("\n ================================================================== \n")
club_list: str = random_choice_club()
display_color_club(club_list)
player.club = choice_answer_club(club_list)

player.display_player()

# ===== Choice Offer from a new club ===== #

print("\n ================================================================== \n")
club_offer = create_mercato_event(random_club_sup(tier_club(player.club)))
club_offer.display_event()
choice_answer_mercato(club_offer, player)

player.display_player()

# ===== New Season ===== #

##### RAJOUTER FONCTION POUR AFFICHER LA REPONSE CHOISIS DE LEVENT #####

print("\n\n================================================================== \n")

season = create_season(player)
season.display_season()

# Display random ranking league
print(create_league_ranking(player))