from dataclasses import dataclass
import random
from utils.events import get_event_random_footballmoment, get_event_random_media
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
    for _ in range(10):
      
      event = get_event_random_footballmoment(player.post)
      if event is not None:
        event.display_event()
      effect = choice_answer_event(event)
      stat_update_event(effect, player.statistics)
      
      event = get_event_random_media()
      if event is not None:
          event.display_event()
      effect = choice_answer_event(event)
      stat_update_event(effect, player.statistics)
      
      match = random.randint(30, 50)
      yellow_card = random.randint(2, 15)
      note = round(random.uniform(3, 9), 1)
      objective = "Gagner au moins 10 matchs dans la saison."
      year = "2024/2025"
      id = 1
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