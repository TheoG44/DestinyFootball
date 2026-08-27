from dataclasses import dataclass

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
      [{self.id}] {self.name}
      
      Season: {self.year}
      
      Match: {self.match}
      
      Goals: {self.goals}
      
      Assists: {self.assists}
      
      Carton jaune: {self.yellow_card}
      
      Note: {self.note}/10
      
      Objective: {self.salary}
      """)