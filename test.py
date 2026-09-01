ranking = ['Barça', 'Real Madrid', 'Atleti', 'Sevilla FC', 'Villarreal', 'Valencia', 'Real Betis', 'Getafe', 'Athletic', 'Real Sociedad', 'Celta', 'Elche', 'Málaga', 'Levante', 'Osasuna', 'Rayo Vallecano', 'Santander', 'Espanyol', 'Deportivo', 'Alavés']

def display_league_ranking(ranking: list):
        table = (
          "┌──────────────────────┐\n"
          "│ Ranking              │\n"
          "├──────────────────────┤\n"
        )

        for team in ranking:
          table += f"│ {team:<20} │\n"
          table += f"├──────────────────────┤\n"

        table += "└──────────────────────┘"
        
        return table
      
      
print(display_league_ranking(ranking))


      
      