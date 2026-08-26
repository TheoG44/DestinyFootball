from utils.player import create_player, Player
from logic import random_choice_club, stat_update_event, choice_answer_event, display_color_club, choice_answer_club
from utils.events import random_event, MediaEvent

player = create_player()
"""
theo_player = Player(
      "theo lecon",
      16, 
      "France", 
      "attacker",
      22, 
      {"Technical": 70, "Physical": 70, "Speed": 70, "Strike": 70, "Defence": 50, "Vision": 60, "Cold blood": 70, "Discipline": 60, "Relationship coach": 50, "Locker room": 50, "Reputation": 0, "Mental": 50},
      "PSG",
      99.0,
      0.001,
      ["yo"]
    )
"""
print("\n\n================================================================== \n")

club_list = random_choice_club()
display_color_club(club_list)

player.club = choice_answer_club(club_list)


print("\n\n================================================================== \n")

while True:
  event = random_event()

  if event is not None:
      print(event.display_event())
      
  effect = choice_answer_event(event)

  stat_update_event(effect, player.statistics) # type: ignore
  
  print(player.display_char())

