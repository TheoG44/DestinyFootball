from dataclasses import dataclass
from utils.player import Player
import sqlite3
import logging
import random

# ================================================================================ #

@dataclass
class MediaEvent:

    id: int
    title: str
    description: str
    answer_1: str
    effect_1: str
    comment_1: str
    answer_2: str
    effect_2: str
    comment_2: str
    type_event: str 
    type_effect: str
    probability: float



    def display_event(self):
        """
          Formats the event for display in the terminal.

          Returns: Formatted text for the event.
        """
        print(f"""
  🎙️{self.type_event} {self.id}

{self.title}

{self.description}

[1] {self.answer_1}

[2] {self.answer_2}

DEBUG : 
    - Comment1 : {self.comment_1} Effect : {self.effect_1}
    - Comment2 : {self.comment_2} Effect : {self.effect_2}
""")

def get_event_random_media() -> MediaEvent:
    """
      Recover an event from its id.
    
      Args: id (int)
    
      Returns: event (:MediaEvent) -> Object event
    """
    
    conn = sqlite3.connect("./data/events.db")
    c = conn.cursor()

    c.execute(
        "SELECT * FROM Media_Events ORDER BY RANDOM() LIMIT 1"
    )

    row = c.fetchone()
    conn.close()
    
    event = MediaEvent(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4],
        row[5],
        row[6],
        row[7],
        row[8],
        row[9],
        row[10],
        row[11]
    )
    logging.info("✅ GET MediaEvent: %s", event.id)
    return event

# ================================================================================ #

@dataclass
class RelationshipEvent:
    
    id: int
    title: str
    description: str
    answer_1: str
    effect_1: str
    comment_1: str
    answer_2: str
    effect_2: str
    comment_2: str
    type_event: str 
    type_effect: str
    probability: float



    def display_event(self):
        """
          Formats the event for display in the terminal.

          Returns: Formatted text for the event.
        """
        print(f"""
  👥{self.type_event} {self.id}

{self.title}

{self.description}

[1] {self.answer_1}

[2] {self.answer_2}

DEBUG : 
    - Comment1 : {self.comment_1} Effect : {self.effect_1}
    - Comment2 : {self.comment_2} Effect : {self.effect_2}
""")

def get_event_random_relationship() -> RelationshipEvent:
    """
      Recover an event from its id.
    
      Args: id (int)
    
      Returns: event (:RelationshipEvent) -> Object event
    """
    
    conn = sqlite3.connect("./data/events.db")
    c = conn.cursor()

    c.execute(
        "SELECT * FROM FootballMoment_Events ORDER BY RANDOM() LIMIT 1"
    )

    row = c.fetchone()
    conn.close()

    event = RelationshipEvent(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4],
        row[5],
        row[6],
        row[7],
        row[8],
        row[9],
        row[10],
        row[11]
    )
    logging.info("✅ GET RelationshipEvent: %s", event.id)
    return event


# ================================================================================ #

@dataclass
class FootballMomentEvent:
    
    id: int
    title: str
    description: str
    answer_1: str #safe
    effect_1: str # effet sur la reputation, Forme, Moral
    comment_1: str
    answer_2: str #normal
    effect_2: str
    comment_2: str
    answer_3: str #risque plus recompense
    effect_3: str
    comment_3: str
    post: str
    type_event: str
    probability: float 



    def display_event(self):
        """
          Formats the event for display in the terminal.

          Returns: Formatted text for the event.
        """
        print(f"""
  ⚽{self.type_event} {self.id}
  
{self.title}

{self.description}

[1] {self.answer_1}

[2] {self.answer_2}

[3] {self.answer_3}

DEBUG : 
    - Comment1 : {self.comment_1} Effect : {self.effect_1}
    - Comment2 : {self.comment_2} Effect : {self.effect_2}
    - Comment3 : {self.comment_3} Effect : {self.effect_3}
""")

def get_event_random_footballmoment(post: str) -> FootballMomentEvent:
    """
      Recover an event from its id.
    
      Args: id (int)
    
      Returns: event (:FootballMoment) -> Object event
    """
    
    conn = sqlite3.connect("./data/events.db")
    c = conn.cursor()

    c.execute(
        "SELECT * FROM FootballMoment_Events WHERE post = ? ORDER BY RANDOM() LIMIT 1",
        (post,)
    )

    row = c.fetchone()
    conn.close()

    event = FootballMomentEvent(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4],
        row[5],
        row[6],
        row[7],
        row[8],
        row[9],
        row[10],
        row[11],
        row[12],
        row[13],
        row[14]
    )
    
    logging.info("✅ GET FootballMomentEvent: %s", event.id)
    return event





# ================================================================================ #

@dataclass
class TrainingEvent:
    
    id: int
    title: str
    description: str
    answer_1: str # Entrainement serieux (+ de stats sup)
    effect_1: str 
    comment_1: str
    answer_2: str # Pas de nv stats + de mental et forme
    effect_2: str
    comment_2: str
    post: str # adapter au type de post
    type_event: str #type training
    probability: int



    def display_event(self):
        """
          Formats the event for display in the terminal.

          Returns: Formatted text for the event.
        """
        print(f"""
  👟{self.type_event} {self.id}
    
{self.title}

{self.description}

[1] {self.answer_1}

[2] {self.answer_2}

DEBUG : 
    - Comment1 : {self.comment_1} Effect : {self.effect_1}
    - Comment2 : {self.comment_2} Effect : {self.effect_2}
""")


def get_event_random_training(post: str) -> TrainingEvent:
    """
      Recover an event from its id.
    
      Args: id (int)
    
      Returns: event (:TrainingEvent) -> Object event
    """
    
    conn = sqlite3.connect("./data/events.db")
    c = conn.cursor()

    c.execute(
        "SELECT * FROM Training_Events WHERE post = ?",
        (post,)
    )

    row = c.fetchone()
    conn.close()

    event = TrainingEvent(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4],
        row[5],
        row[6],
        row[7],
        row[8],
        row[9],
        row[10],
        row[11]
    )
    
    logging.info("✅ GET TrainingEvent: %s", event.id)
    return event


# ================================================================================ #

@dataclass
class InjuryEvent:

    id: int
    title: str
    description: str
    effect: str
    comment: str
    type_event: str 
    tier: str #tier A,B et C (legere, moyenne, grave)
    probability: float



    def display_event(self):
        """
          Formats the event for display in the terminal.

          Returns: Formatted text for the event.
        """
        print(f"""
  🤕{self.type_event} {self.id} 

{self.title}

{self.description}

Gravity : {self.tier}

{self.comment}

DEBUG : Effect : {self.effect}

""")


def get_event_random_injury(tier: str) -> InjuryEvent:
    """
      Recover an event from its id.
    
      Args: stats (str) -> player.stats
    
      Returns: event (:InjuryEvent) -> Object event
    """
      
    conn = sqlite3.connect("./data/events.db")
    c = conn.cursor()
    
    c.execute(
        "SELECT * FROM Injury_Events WHERE tier = ?",
        (tier,)
    )

    row = c.fetchone()
    conn.close()

    event = InjuryEvent(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4],
        row[5],
        row[6],
        row[7]
    )
    
    logging.info("✅ GET InjuryEvent: %s", event.id)
    return event


# ================================================================================ #

@dataclass
class MercatoEvent:
    
    title: str
    club: str
    year: int
    salary: float
    description: str
    answer_1: str
    answer_2: str
    type_event: str 


    def display_event(self):
        """
          Formats the event for display in the terminal.

          Returns: Formatted text for the event.
        """
        print(f"""
  🤝{self.type_event} 
  
{self.title}

{self.description}

Contract term : {self.year}

Salary : {self.salary}$ /year

[1] {self.answer_1}

[2] {self.answer_2}

""")

def create_mercato_event(club: str) -> MercatoEvent :
    """
      Creates the MercatoEvent object.
                
      Args: club (str)
                
      Returns: event (MercatoEvent) -> MercatoEvent object
    """
    conn = sqlite3.connect("./data/clubs.db")
    c = conn.cursor()
    
    c.execute(
            "SELECT short_name, club_colors, country, tier FROM Clubs JOIN Leagues ON Clubs.league_id = Leagues.id WHERE short_name = ?",
        (club,) 
    )
    
    club_prm = c.fetchone()
    conn.close()
    
    match club_prm[3]:
        case "S":
          salary = round(random.uniform(10, 20), 2)
        case "A":
          salary = round(random.uniform(3, 10), 2)
        case "B":
          salary = round(random.uniform(3, 10), 2)
        case "C":
          salary = round(random.uniform(1, 4), 2)
        case "D2":
          salary = round(random.uniform(0.2, 0.9), 2)
    
    
    year = random.randint(2, 5)
    
    event = MercatoEvent (
      "Un Nouveaux club s'intéresse à vous !",
      club,
      year,
      salary,
      f"{club} vous propose un contrat de {year} ans avec un salaire de {salary}M €/y hors prime. Souhaitez vous accepter ce contrat ? ",
      "Accepter l'offre",
      "Refuser l'offre",
      "Mercato" 
    )
    
    logging.info("✅ GET MercatoEvent: %s", event.club)
    return event


def tier_club(club: str) -> str:
    """
      Return Tier of the club.
        
      Args: club (str)
        
      Returns: tier (str) -> ex(S,A,C,..)
    """
    conn = sqlite3.connect("./data/clubs.db")
    c = conn.cursor()
    
    c.execute(
            "SELECT tier FROM Clubs WHERE short_name = ?",
        (club,) 
    )
    
    tier = c.fetchone()
    tier = tier[0]
    
    conn.close()
    
    return tier
    
    
def random_club_sup(tier: str):
    """
      Randomly select a shooting club from the list above.
            
      Args: tier (str)
            
      Returns: club (str) -> short_name
    """
    conn = sqlite3.connect("./data/clubs.db")
    c = conn.cursor()
        
    match tier:
        case "S":
          tier = "S"
        case "A":
          tier = "S"
        case "B":
          tier = "A"
        case "C":
          tier = "B"
        case "D2":
          tier = "C"

    c.execute(
            "SELECT short_name FROM Clubs WHERE tier = ? ORDER BY RANDOM() LIMIT 1",
        (tier,) 
    )
    
    club = c.fetchone()
    club = club[0]
    conn.close()
    
    return club


def random_club_low(tier: str):
    """
      Randomly select a shooting club from the list below.
            
      Args: tier (str)
            
      Returns: club (str) -> short_name
    """
    conn = sqlite3.connect("./data/clubs.db")
    c = conn.cursor()
        
    match tier:
        case "S":
          tier = "A"
        case "A":
          tier = "B"
        case "B":
          tier = "C"
        case "C":
          tier = "D2"
        case "D2":
          tier = "D2"

    c.execute(
            "SELECT short_name FROM Clubs WHERE tier = ? ORDER BY RANDOM() LIMIT 1",
        (tier,) 
    )
    
    club = c.fetchone()
    club = club[0]
    conn.close()
    
    return club


def choice_answer_mercato(event: MercatoEvent, player: Player):
    """
      Retrieve the selected effect.
          
      Args: event (:MediaEvent)
          
      Returns: effect (str) -> effect selected
    """
    choice = int(input("Choissisez votre réponse (1. ou 2.): "))
    
    if choice == 1:
      player.club = event.club
      print(f"\nVous faite désormais parti de {event.club}.")
    elif choice == 2:
      print(f"\nVous avez fait le choix de rester à {player.club}.")
    else:
      print("Error")
    
    # Update remaining contract player and salary
    player.contract = event.year
    player.salary = event.salary
    

def create_extension_club_event(club: str) -> MercatoEvent :
    """
      Creates the MercatoEvent object.
                
      Args: club (str)
                
      Returns: event (MercatoEvent) -> MercatoEvent object
    """
    conn = sqlite3.connect("./data/clubs.db")
    c = conn.cursor()
    
    c.execute(
            "SELECT short_name, club_colors, country, tier FROM Clubs JOIN Leagues ON Clubs.league_id = Leagues.id WHERE short_name = ?",
        (club,) 
    )
    
    club_prm = c.fetchone()
    conn.close()
    
    match club_prm[3]:
        case "S":
          salary = round(random.uniform(10, 20), 2)
        case "A":
          salary = round(random.uniform(3, 10), 2)
        case "B":
          salary = round(random.uniform(3, 10), 2)
        case "C":
          salary = round(random.uniform(1, 4), 2)
        case "D2":
          salary = round(random.uniform(0.2, 0.9), 2)
    
    
    year = random.randint(2, 5)
    
    event = MercatoEvent (
      "Votre club veut vous prolonger.",
      club,
      year,
      salary,
      f"{club} vous propose un nouveau contrat de {year} ans avec un salaire de {salary}M €/y hors prime. Souhaitez vous accepter ce contrat ? ",
      "Accepter l'offre",
      "Refuser l'offre",
      "Mercato" 
    )
    
    logging.info("✅ GET MercatoEvent: %s", event.club)
    return event