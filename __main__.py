from utils.player import create_player, Player
from logic import random_choice_club, stat_update_event, choice_answer_event, display_color_club, choice_answer_club, new_year
from utils.events import get_event_random_media, get_event_random_footballmoment, tier_club, random_club_low, random_club_sup, create_mercato_event, choice_answer_mercato, MediaEvent
from utils.season import create_season, Season
from utils.league_ranking import create_league_ranking, display_league_ranking
import logging

logging.basicConfig(
    level=logging.INFO,                 
    filename="app.log",                     
    filemode="w",                          
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def Game():
  logging.info("Game started")
  id_season = 0
  compt_season = 0
  year = "2024/2025"

  # ===== Create player object ===== #

  print("\n ================================================================== \n")
  player = create_player()
  logging.info("✅ Player created: %s", player.name)

  # ===== Choice of starting club ===== #
  
  print("\n ================================================================== \n")
  club_list: str = random_choice_club()
  display_color_club(club_list)
  player.club = choice_answer_club(club_list)
  logging.info("✅ Player joined club: %s", player.club)
  player.display_player()


  # ===== Season Sequence ===== #
  
  while compt_season < 4:
    
    year = new_year(year)
    logging.info("✅ New season started: %s", year)

    compt_season += 1
    player.contract -= 1
    id_season += 1
    
    player.net_worth = round(player.salary + player.net_worth, 3)
    
    # ===== Choice Offer extension from club ===== #
    if player.contract == 0:
        ...
        # demande de prolongation du club
    
    
    print("\n ================================================================== \n")
    
    season = create_season(player, year, id_season)
    season.display_season()
    display_league_ranking(season.rank_league)
    
    
    # ===== Choice Offer from a new club ===== #
    if season.note < 3:
      club_offer = create_mercato_event(random_club_low(tier_club(player.club)))
      club_offer.display_event()
      choice_answer_mercato(club_offer, player)
      logging.info("✅ Player joined club: %s", player.club)
    elif season.note > 6:
      club_offer = create_mercato_event(random_club_sup(tier_club(player.club)))
      club_offer.display_event()
      choice_answer_mercato(club_offer, player)
      logging.info("✅ Player joined club: %s", player.club)

    player.display_player()


  print("Fin de partie, vous avez pris votre retraite !")
  logging.info("✅ End Game: %s", player)


Game()