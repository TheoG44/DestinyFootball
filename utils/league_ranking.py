from utils.player import Player
import sqlite3
import random

def create_league_ranking(note: float, player: Player) :
    """
      Function for create new player.
      
      Args : note (float) -> season note / player (Player) -> object player
          
      Returns: table (tuple) -> ranking league
    """
    club = player.club
    
    conn = sqlite3.connect("./data/clubs.db")
    c = conn.cursor()
    
    c.execute(
            "SELECT league_id FROM Clubs WHERE short_name = ?",
              (club,)
        )
    
    league = c.fetchone()
    league = league[0]
    
    c.execute(
          "SELECT short_name, tier FROM Clubs WHERE league_id = ?",
            (league,)
      )
    
    row = c.fetchall() 
    conn.close()
    
    #trier alea le row
    random.shuffle(row)
    
    rank = {"S": 0,"A": 1,"B": 2,"C": 3, "D2": 4}
    
    # Si la note > 6 de season alors club premier de ses tier
    if note > 6:
      result = sorted(
        row,
        key=lambda x: (rank[x[1]], x[0].lower() != club.lower())
      )
      ranking = [x[0] for x in result]
    # trier par tier mais aleatoirement
    else:
      ranking = [club for club, tier in sorted(row, key=lambda x: rank[x[1]])]
    
    
    return ranking


  
  
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
        
        print(table)


