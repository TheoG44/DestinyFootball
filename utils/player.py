from dataclasses import dataclass
import random

# ================================================================================ #

@dataclass
class Player:

    name: str
    age: int 
    nationality: str
    post: str
    number: int
    statistics: dict[str, int]
    club: str
    note : float
    salary: float
    distinction: list[str]
  
    def display_player(self):
        """
          Formats the event for display in the terminal.
    
          Returns: Formatted text for the event.
        """
        print(f"""
      [👤] {self.name}
      
      Age: {self.age}
      
      Country: {self.nationality}
      
      Post: {self.post}
      
      Jersey Number: {self.number}
      
      Statistics:
{self.display_statistics()}

      Club: {self.club}
      
      Note: {self.note}/100
      
      Salary: {self.salary}M€
      
      Distinction: {self.distinction}
      """)
    
    def display_statistics(self):
        table = (
          "┌────────────────────────┬───────┐\n"
          "│ Statistic              │ Value │\n"
          "├────────────────────────┼───────┤\n"
        )

        for stat, value in self.statistics.items():
          table += f"│ {stat:<22} │ {value:>5} │\n"

        table += "└────────────────────────┴───────┘"
        return table
    
    def display_name(self):
        return f"The player is {self.name}."


# ================================================================================ #


def create_player():
    """
      Function for create new player.
      
      Returns: player (:Player) -> new player
    """
    stats = {}

    print("---- ⚙️ Player Creation ⚙️ ----")
    
    name = input("Entrer votre prenom/nom (first_name name): ")
    nationality = input("Entrer votre nationalité: ")
    post = input("Entrer votre poste: ")
    while True: 
      try:
        number: int = int(input("Entrer votre numéro: "))
        if 0 < number <= 99:
          break
        else:
          print("number not 0 < number <= 99")
      except ValueError:
        print("Try again")
      
    
    if post == "attacker":
      stats = {
            "Technical": random.randint(60, 70),
            "Physical": random.randint(50, 70),
            "Speed": random.randint(50, 70),
            "Strike": random.randint(60, 70),
            "Defence": random.randint(30, 50),
            "Vision": random.randint(40, 60),
            "Cold blood": random.randint(50, 70),
            "Discipline": random.randint(40, 60),
            "Relationship coach": 50,
            "Locker room": 50,
            "Reputation": 0,
            "Mental": 50,
          }
    elif post == "midfielder":
      stats = {
            "Technical": random.randint(60, 70),
            "Physical": random.randint(50, 70),
            "Speed": random.randint(50, 60),
            "Strike": random.randint(40, 70),
            "Vision": random.randint(60, 70),
            "Defence": random.randint(40, 60),
            "Cold blood": random.randint(40, 60),
            "Discipline": random.randint(50, 70),
            "Relationship coach": 50,
            "Locker room": 50,
            "Reputation": 0,
            "Mental": 50,
          }
    elif post == "defender":
      stats = {
            "Technical": random.randint(50, 60),
            "Physical": random.randint(60, 70),
            "Speed": random.randint(50, 60),
            "Strike": random.randint(40, 60),
            "Vision": random.randint(40, 60),
            "Defence": random.randint(60, 70),
            "Cold blood": random.randint(50, 70),
            "Discipline": random.randint(50, 70),
            "Relationship coach": 50,
            "Locker room": 50,
            "Reputation": 0,
            "Mental": 50,
          }
    elif post == "goalkeeper":
      stats = {
            "Technical": random.randint(50, 60),
            "Physical": random.randint(60, 70),
            "Speed": random.randint(50, 60),
            "Strike": random.randint(40, 60),
            "Vision": random.randint(40, 60),
            "Defence": random.randint(60, 70),
            "Cold blood": random.randint(50, 70),
            "Discipline": random.randint(50, 70),
            "Relationship coach": 50,
            "Locker room": 50,
            "Reputation": 0,
            "Mental": 50,
          }
    else:
      print("❌ Error post")
      return -1
    
    som: int = 0
    for value in stats.values():
      som += value
    note: float = som / len(stats)  

    player = Player (
      name,
      16, 
      nationality, 
      post,
      number, 
      stats,
      '///',
      note,
      0.001,
      [],
    )
    
    print("\n\n✅ The player is created")
    print(player.display_char())
    
    return player
    
    