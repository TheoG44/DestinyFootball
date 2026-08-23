from dataclasses import dataclass

@dataclass
class Player:
    age: int 
    reputation: float
    nationality: str
    post: str
    statistics: dict[str, int]
    club: str
    note : int
    salary: float
    distinction: list[str]
  
    def display_char(self):
      return f"The player has {self.age} years old. \nThe player has {self.reputation} stars. \nThe player was born in {self.nationality}. \nThe player is {self.post}. \nThe player has for stastistics :{self.statistics}. \nThe player is in {self.club}. \nThe player has {self.note} note. \nThe player has {self.salary} for salary. \nThe player is {self.distinction}."
      
      
    def display_age(self):
      return f"The player has {self.age} years old."


Leon_Marchand = Player(
    18,
    3.5,
    'France',
    'attacker',
    {
    "shooting": 12,
    "speed": 5,
    "mental": 43
    },
    'Bayern',
    82,
    2.0,
    []
)
print(Leon_Marchand.display_char())

def create_player():
  print("---- Creation de Joueur ----")
  name = input("Entrer votre prénom: ")
  post = input("Entrer votre poste: ")
  number = int(input("Entrer votre numéro: "))
  


create_player()