from dataclasses import dataclass
import random
from utils.league_ranking import create_league_ranking
from utils.events import get_event_random_footballmoment, get_event_random_media, get_event_random_training, get_event_random_relationship, get_event_random_injury, tier_club
from utils.player import Player
from logic import choice_answer_club, choice_answer_event, random_choice_club, stat_update_event




@dataclass
class Season:

    id: int
    year: tuple[int, int]
    match: int 
    goals: int
    assists: int
    yellow_card: int
    note : float
    objective: str
    rank_league: list
    
  
    def display_season(self):
        """
          Formats the event for display in the terminal.
    
          Returns: Formatted text for the event.
        """
        print(f"""
      [{self.id}] 
      
      Season: {self.year}
      
      Match: {self.match}
      
      Goals: {self.goals}
      
      Assists: {self.assists}
      
      Carton jaune: {self.yellow_card}
      
      Note: {self.note}/10
      
      Objective: {self.objective}
      """)


def create_season(player: Player, year: str, id: int) -> Season :
    """
      Create new season depending on events.
        
      Args : player (:Player) / year: str
      
      Returns: season (:Season) -> object season
    """
    compt = 0
    
    event = get_event_random_training(player.post)
    print("\n\n================================================================== \n")
    if event is not None:
        event.display_event()
    effect = choice_answer_event(event)
    stat_update_event(effect, player.statistics)
    
    tier = "N"
    stats = player.statistics
    
    if stats["Forme"] <= 50:
        tier = "C"
    elif stats["Forme"] <= 45:
        tier = "B"
    elif stats["Forme"] <= 40:
        tier = "C"
    
    if tier != "N":
      event = get_event_random_injury(tier)
      print("\n\n================================================================== \n")
      if event is not None:
        event.display_event()
      stat_update_event(event.effect, player.statistics)
    
    post = player.post
    
    if tier == "A":
      match = random.randint(30, 40)
      yellow_card = random.randint(0, 10)
      match_play_ind = 9
      
      if post == "attacker":
          goals = random.randint(5, 25)
          assists = random.randint(5, 25)
      elif post == "midfielder":
          goals = random.randint(1, 10)
          assists = random.randint(5, 15)
      elif post == "defender":
          goals = random.randint(0, 5)
          assists = 0
      else:
        goals = 0
        assists = 0
    
    if tier == "B":
      match = random.randint(20, 30)
      yellow_card = random.randint(0, 7)
      match_play_ind = 7
      
      if post == "attacker":
          goals = random.randint(5, 20)
          assists = random.randint(5, 20)
      elif post == "midfielder":
          goals = random.randint(1, 10)
          assists = random.randint(5, 15)
      elif post == "defender":
          goals = random.randint(0, 3)
          assists = 0
      else:
        goals = 0
        assists = 0
      
    if tier == "C":
      match = random.randint(8, 15)
      yellow_card = random.randint(0, 3)
      match_play_ind = 4

      if post == "attacker":
          goals = random.randint(0, 8)
          assists = random.randint(0, 8)
      elif post == "midfielder":
          goals = random.randint(0, 3)
          assists = random.randint(0, 3)
      elif post == "defender":
          goals = random.randint(0, 2)
          assists = 0
      else:
        goals = 0
        assists = 0

    else:
      match = random.randint(40, 50)      
      yellow_card = random.randint(0, 15)
      match_play_ind = 10
      
      if post == "attacker":
          goals = random.randint(5, 30)
          assists = random.randint(5, 30)
      elif post == "midfielder":
          goals = random.randint(1, 10)
          assists = random.randint(5, 15)
      elif post == "defender":
          goals = random.randint(0, 5)
          assists = 0
      else:
        goals = 0
        assists = 0
    
    for i in range(match_play_ind):
      
      event = get_event_random_footballmoment(player.post)
      print("\n\n================================================================== \n")
      if event is not None:
        event.display_event()
      effect = choice_answer_event(event)
      if "+" in effect:
        compt += 1
      stat_update_event(effect, player.statistics)
      
      if i%2 == 0:
        event = get_event_random_media()
        print("\n\n================================================================== \n")
        if event is not None:
            event.display_event()
        effect = choice_answer_event(event)
        stat_update_event(effect, player.statistics)
      else:
        event = get_event_random_relationship()
        print("\n\n================================================================== \n")
        if event is not None:
            event.display_event()
        effect = choice_answer_event(event)
        stat_update_event(effect, player.statistics)
    
    
    if compt > 5:
      note = round(random.uniform(6, 9), 1)
    else:
      note = round(random.uniform(3, 5), 1)
    
    event = get_event_random_training(player.post)
    print("\n\n================================================================== \n")
    if event is not None:
        event.display_event()
    effect = choice_answer_event(event)
    stat_update_event(effect, player.statistics)
    
    
    tier_club_player = tier_club(player.club)
    
    rank_league = create_league_ranking(note, player)

    objective = "✅ "
    
    for club in rank_league:
      clubs_tier = tier_club(club)
      
      if tier_club_player == clubs_tier:
        if player.club != club:
          objective = "❌ "
          break
      break
    
    
    if tier_club_player == "S":
        objective += "Gagner le championnat."
    elif tier_club_player == "A":
        objective += "Finir top 3 du championnat."
    elif tier_club_player == "B":
        objective += "Finir top 5 du championnat."
    elif tier_club_player == "C":
        objective += "Finir top 10 du championnat."
    else:
        objective += "Etre promu en division supérieure"
    
    season = Season (
        id,
        year,
        match,
        goals,
        assists,
        yellow_card,
        note,
        objective,
        rank_league,
      )
    
    return season