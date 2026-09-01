from dataclasses import dataclass
import random
from utils.events import get_event_random_footballmoment, get_event_random_media, get_event_random_training, get_event_random_relationship, get_event_random_injury, tier_club
from utils.player import Player
from logic import choice_answer_club, choice_answer_event, random_choice_club, stat_update_event, new_year

year = "2024/2025"
id = 0

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
        
def create_season(player: Player) -> Season :
    """
      Create new season depending on events.
        
      Args : player (:Player)
      
      Returns: season (:Season) -> object season
    """
    
    event = get_event_random_training(player.post)
    if event is not None:
        event.display_event()
    effect = choice_answer_event(event)
    stat_update_event(effect, player.statistics)
    
    
    stats = player.statistics
    
    if stats["Forme"] <= 50:
        tier = "C"
    elif stats["Forme"] <= 45:
        tier = "B"
    elif stats["Forme"] <= 40:
        tier = "C"
    event = get_event_random_injury(tier)
    if event is not None:
      event.display_event()
    stat_update_event(event.effect, player.statistics)
    
    if event.tier == "A":
      match = random.randint(30, 40)
      yellow_card = random.randint(0, 10)
    if event.tier == "B":
      match = random.randint(20, 30)
      yellow_card = random.randint(0, 7)
    if event.tier == "C":
      match = random.randint(0, 15)
      yellow_card = random.randint(0, 3)
    else:
      match = random.randint(40, 50)      
      yellow_card = random.randint(0, 15)

    
    for i in range(10):
      
      event = get_event_random_footballmoment(player.post)
      if event is not None:
        event.display_event()
      effect = choice_answer_event(event)
      stat_update_event(effect, player.statistics)
      
      if i%2 == 0:
        event = get_event_random_media()
        if event is not None:
            event.display_event()
        effect = choice_answer_event(event)
        stat_update_event(effect, player.statistics)
      else:
        event = get_event_random_relationship()
        if event is not None:
            event.display_event()
        effect = choice_answer_event(event)
        stat_update_event(effect, player.statistics)
      
    
    
    note = round(random.uniform(3, 9), 1)
    
    tier_c = tier_club(player.club)
    if tier_c == "S":
      objective = "Gagner le championnat."
    elif tier_c == "A":
      objective = "Finir top 3 du championnat."
    elif tier_c == "B":
      objective = "Finir top 5 du championnat."
    elif tier_c == "C":
      objective = "Finir top 10 du championnat."
    else:
      objective = "Etre promu en division supérieure."
    
    
    global year
    year = new_year(year)
    
    global id
    id += 1

    post = player.post
    if post == "attacker":
      goals = random.randint(5, 35)
      assists = random.randint(5, 35)
    elif post == "midfielder":
      goals = random.randint(1, 10)
      assists = random.randint(5, 15)
    elif post == "defender":
      goals = random.randint(0, 5)
      assists = 0
    else:
      goals = 0
      assists = 0
    
    event = get_event_random_training(player.post)
    if event is not None:
        event.display_event()
    effect = choice_answer_event(event)
    stat_update_event(effect, player.statistics)
    
      
    season = Season (
        id,
        year,
        match,
        goals,
        assists,
        yellow_card,
        note,
        objective,
      )
      
    return season