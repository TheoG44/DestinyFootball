from dataclasses import dataclass

@dataclass
class achievements:
  
    title: list[str]
    stats_season: list[list]
    ...
    
    
    
    def display_event(self):
          """
            Formats the achievements for display in the terminal.
    
            Returns: Formatted text for the archievements.
          """
          print(f"""
          
          {self.title}  
                
""")